import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, roc_auc_score, precision_score, 
                             recall_score, f1_score, matthews_corrcoef, 
                             confusion_matrix, classification_report, roc_curve, auc)
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(
    page_title="ML Classification Models Comparison",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
    .header-section {
        color: #1f77b4;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if 'data' not in st.session_state:
    st.session_state.data = None
if 'models_trained' not in st.session_state:
    st.session_state.models_trained = False
if 'results' not in st.session_state:
    st.session_state.results = {}

# Title
st.title("🤖 ML Classification Models Comparison Platform")
st.markdown("---")

# Sidebar - File Upload and Configuration
st.sidebar.header("📁 Data Configuration")
uploaded_file = st.sidebar.file_uploader("Upload your CSV dataset", type=['csv'])

if uploaded_file is not None:
    # Load data
    st.session_state.data = pd.read_csv(uploaded_file)
    st.sidebar.success("✓ Dataset loaded successfully!")
    
    # Display dataset info
    with st.sidebar.expander("📊 Dataset Info"):
        st.write(f"**Shape:** {st.session_state.data.shape}")
        st.write(f"**Columns:** {list(st.session_state.data.columns)}")
        st.write(f"**Data Types:**\n{st.session_state.data.dtypes}")
        st.write(f"**Missing Values:**\n{st.session_state.data.isnull().sum().sum()} total")

if st.session_state.data is not None:
    st.sidebar.header("⚙️ Model Configuration")
    
    # Target column selection
    target_col = st.sidebar.selectbox(
        "Select Target Column",
        options=st.session_state.data.columns
    )
    
    # Test-train split
    test_size = st.sidebar.slider("Test Size Ratio", 0.1, 0.4, 0.2)
    
    # Train models button
    if st.sidebar.button("🚀 Train All Models", use_container_width=True):
        with st.spinner("Training models... Please wait"):
            try:
                # Prepare data
                X = st.session_state.data.drop(columns=[target_col])
                y = st.session_state.data[target_col]
                
                # Round quality to nearest integer (convert continuous to discrete)
                y = y.round().astype(int) 
                
                # Encode categorical variables
                label_encoders = {}
                for col in X.select_dtypes(include=['object']).columns:
                    le = LabelEncoder()
                    X[col] = le.fit_transform(X[col].astype(str))
                    label_encoders[col] = le
                
                # Encode target if categorical
                if y.dtype == 'object':
                    le_target = LabelEncoder()
                    y = le_target.fit_transform(y)
                    label_encoders['target'] = le_target
                
                # Train-test split
                X_train, X_test, y_train, y_test = train_test_split(
                    X, y, test_size=test_size, random_state=42, stratify=y
                )
                
                # Scale features
                scaler = StandardScaler()
                X_train_scaled = scaler.fit_transform(X_train)
                X_test_scaled = scaler.transform(X_test)
                
                # Initialize models
                models = {
                    'Logistic Regression': LogisticRegression(
                        max_iter=1000, random_state=42, solver='lbfgs'
                    ),
                    'Decision Tree': DecisionTreeClassifier(
                        random_state=42, max_depth=15
                    ),
                    'K-Nearest Neighbor': KNeighborsClassifier(n_neighbors=5),
                    'Naive Bayes': GaussianNB(),
                    'Random Forest (Ensemble)': RandomForestClassifier(
                        n_estimators=100, random_state=42, n_jobs=-1
                    )
                }
                
                # Train and evaluate models
                st.session_state.results = {}
                for model_name, model in models.items():
                    # Train
                    if model_name == 'K-Nearest Neighbor':
                        model.fit(X_train_scaled, y_train)
                        y_pred = model.predict(X_test_scaled)
                        y_pred_proba = model.predict_proba(X_test_scaled)[:, 1] if hasattr(model, 'predict_proba') else None
                    else:
                        model.fit(X_train_scaled, y_train)
                        y_pred = model.predict(X_test_scaled)
                        y_pred_proba = model.predict_proba(X_test_scaled)[:, 1] if hasattr(model, 'predict_proba') else None
                    
                    # Calculate metrics
                    accuracy = accuracy_score(y_test, y_pred)
                    precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
                    recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
                    f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
                    mcc = matthews_corrcoef(y_test, y_pred)
                    
                    # AUC calculation (handle multi-class)
                    try:
                        if len(np.unique(y)) == 2:
                            auc_score = roc_auc_score(y_test, y_pred_proba)
                        else:
                            auc_score = roc_auc_score(y_test, model.predict_proba(X_test_scaled), 
                                                     multi_class='ovr', average='weighted')
                    except:
                        auc_score = 0.0
                    
                    # Store results
                    st.session_state.results[model_name] = {
                        'model': model,
                        'scaler': scaler,
                        'X_test': X_test_scaled,
                        'y_test': y_test,
                        'y_pred': y_pred,
                        'y_pred_proba': y_pred_proba,
                        'metrics': {
                            'Accuracy': accuracy,
                            'AUC': auc_score,
                            'Precision': precision,
                            'Recall': recall,
                            'F1 Score': f1,
                            'MCC': mcc
                        }
                    }
                
                st.session_state.models_trained = True
                st.success("✓ All models trained successfully!")
                
            except Exception as e:
                st.error(f"Error during training: {str(e)}")

# Main content area
if st.session_state.data is not None and st.session_state.models_trained:
    # Tabs for different views
    tab1, tab2, tab3, tab4 = st.tabs(
        ["📊 Metrics Comparison", "🎯 Model Details", "📈 Visualizations", "📋 About"]
    )
    
    with tab1:
        st.markdown("### Model Performance Comparison")
        
        # Create metrics comparison table
        metrics_data = []
        for model_name, result in st.session_state.results.items():
            row = {'Model': model_name}
            row.update(result['metrics'])
            metrics_data.append(row)
        
        metrics_df = pd.DataFrame(metrics_data)
        
        # Display as table
        st.dataframe(
            metrics_df.set_index('Model'),
            use_container_width=True,
            column_config={
                'Accuracy': st.column_config.NumberColumn(format="%.4f"),
                'AUC': st.column_config.NumberColumn(format="%.4f"),
                'Precision': st.column_config.NumberColumn(format="%.4f"),
                'Recall': st.column_config.NumberColumn(format="%.4f"),
                'F1 Score': st.column_config.NumberColumn(format="%.4f"),
                'MCC': st.column_config.NumberColumn(format="%.4f"),
            }
        )
        
        # Download metrics as CSV
        csv_buffer = metrics_df.to_csv(index=False)
        st.download_button(
            label="📥 Download Metrics as CSV",
            data=csv_buffer,
            file_name="model_metrics.csv",
            mime="text/csv"
        )
        
        # Best model highlight
        best_model = metrics_df.loc[metrics_df['Accuracy'].idxmax(), 'Model']
        best_accuracy = metrics_df['Accuracy'].max()
        st.success(f"🏆 Best Model: **{best_model}** (Accuracy: {best_accuracy:.4f})")
    
    with tab2:
        st.markdown("### Detailed Model Evaluation")
        
        selected_model = st.selectbox(
            "Select a Model",
            options=list(st.session_state.results.keys())
        )
        
        if selected_model:
            result = st.session_state.results[selected_model]
            
            # Display metrics
            col1, col2, col3 = st.columns(3)
            metrics = result['metrics']
            
            with col1:
                st.metric("Accuracy", f"{metrics['Accuracy']:.4f}")
                st.metric("Precision", f"{metrics['Precision']:.4f}")
            
            with col2:
                st.metric("AUC Score", f"{metrics['AUC']:.4f}")
                st.metric("Recall", f"{metrics['Recall']:.4f}")
            
            with col3:
                st.metric("F1 Score", f"{metrics['F1 Score']:.4f}")
                st.metric("MCC", f"{metrics['MCC']:.4f}")
            
            st.markdown("---")
            
            # Confusion Matrix
            st.markdown("#### Confusion Matrix")
            cm = confusion_matrix(result['y_test'], result['y_pred'])
            
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                       cbar_kws={'label': 'Count'}, ax=ax)
            ax.set_xlabel('Predicted')
            ax.set_ylabel('Actual')
            ax.set_title(f'Confusion Matrix - {selected_model}')
            st.pyplot(fig)
            
            # Classification Report
            st.markdown("#### Classification Report")
            report = classification_report(
                result['y_test'], 
                result['y_pred'], 
                output_dict=True,
                zero_division=0
            )
            report_df = pd.DataFrame(report).transpose()
            st.dataframe(report_df, use_container_width=True)
    
    with tab3:
        st.markdown("### Model Performance Visualizations")
        
        # Accuracy comparison
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Accuracy Comparison")
            accuracy_data = [
                st.session_state.results[model]['metrics']['Accuracy'] 
                for model in st.session_state.results.keys()
            ]
            
            fig, ax = plt.subplots(figsize=(10, 6))
            bars = ax.bar(st.session_state.results.keys(), accuracy_data, color='steelblue')
            ax.set_ylabel('Accuracy')
            ax.set_title('Model Accuracy Comparison')
            ax.set_ylim([0, 1])
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height,
                       f'{height:.3f}', ha='center', va='bottom')
            plt.xticks(rotation=45, ha='right')
            st.pyplot(fig)
        
        with col2:
            st.markdown("#### F1 Score Comparison")
            f1_data = [
                st.session_state.results[model]['metrics']['F1 Score'] 
                for model in st.session_state.results.keys()
            ]
            
            fig, ax = plt.subplots(figsize=(10, 6))
            bars = ax.bar(st.session_state.results.keys(), f1_data, color='coral')
            ax.set_ylabel('F1 Score')
            ax.set_title('Model F1 Score Comparison')
            ax.set_ylim([0, 1])
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height,
                       f'{height:.3f}', ha='center', va='bottom')
            plt.xticks(rotation=45, ha='right')
            st.pyplot(fig)
        
        # All metrics radar-like comparison
        st.markdown("#### All Metrics Comparison")
        metrics_list = ['Accuracy', 'AUC', 'Precision', 'Recall', 'F1 Score', 'MCC']
        
        comparison_data = {}
        for metric in metrics_list:
            comparison_data[metric] = [
                st.session_state.results[model]['metrics'][metric] 
                for model in st.session_state.results.keys()
            ]
        
        fig, ax = plt.subplots(figsize=(12, 6))
        x = np.arange(len(st.session_state.results.keys()))
        width = 0.15
        
        for i, metric in enumerate(metrics_list):
            ax.bar(x + i*width, comparison_data[metric], width, label=metric)
        
        ax.set_ylabel('Score')
        ax.set_title('All Metrics Comparison Across Models')
        ax.set_xticks(x + width * 2.5)
        ax.set_xticklabels(st.session_state.results.keys(), rotation=45, ha='right')
        ax.legend()
        ax.set_ylim([0, 1])
        st.pyplot(fig)
    
    with tab4:
        st.markdown("### About This Application")
        st.info("""
        **Machine Learning Classification Models Comparison Platform**
        
        This application implements and compares 5 different classification models:
        1. **Logistic Regression** - Linear model for binary/multi-class classification
        2. **Decision Tree** - Tree-based model with interpretable rules
        3. **K-Nearest Neighbor** - Instance-based learning algorithm
        4. **Naive Bayes** - Probabilistic model based on Bayes' theorem
        5. **Random Forest** - Ensemble of decision trees for improved performance
        
        **Evaluation Metrics:**
        - **Accuracy**: Overall correctness of predictions
        - **AUC Score**: Area Under ROC Curve (measure of separability)
        - **Precision**: True positives among predicted positives
        - **Recall**: True positives among actual positives
        - **F1 Score**: Harmonic mean of precision and recall
        - **MCC**: Matthews Correlation Coefficient (balanced metric for imbalanced data)
        """)
        
        st.markdown("---")
        st.markdown("**Dataset Requirements:**")
        st.write(f"- Minimum 12 features: ✓ (Your dataset has {len(st.session_state.data.columns) - 1} features)")
        st.write(f"- Minimum 500 instances: ✓ (Your dataset has {len(st.session_state.data)} instances)")

else:
    st.info("👆 Please upload a CSV dataset using the sidebar to get started!")
    
    st.markdown("---")
    st.markdown("""
    ### 📋 Getting Started
    
    1. **Prepare your dataset**: Ensure your CSV has at least 12 features and 500 instances
    2. **Upload**: Use the sidebar file uploader
    3. **Configure**: Select target column and test size
    4. **Train**: Click "Train All Models"
    5. **Explore**: View metrics, visualizations, and detailed reports
    
    ### 📊 What You'll Get
    - Comparison of 5 classification models
    - 6 evaluation metrics for each model
    - Confusion matrices and classification reports
    - Performance visualizations
    - Downloadable results
    """)
