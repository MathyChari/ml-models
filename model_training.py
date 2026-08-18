"""
Machine Learning Classification Models Training and Evaluation
Author: ML Assignment 2
Purpose: Train and evaluate 5 classification models with detailed metrics
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, roc_auc_score, precision_score, 
                             recall_score, f1_score, matthews_corrcoef,
                             confusion_matrix, classification_report, roc_curve)
import warnings
warnings.filterwarnings('ignore')

# Set random seed for reproducibility
np.random.seed(42)

class MLModelComparison:
    """
    Class to handle complete ML model training, evaluation, and comparison
    """
    
    def __init__(self, data_path, target_column, test_size=0.2):
        """
        Initialize the model comparison framework
        
        Args:
            data_path: Path to the CSV dataset
            target_column: Name of target column
            test_size: Ratio of test data (default: 0.2)
        """
        self.data = pd.read_csv(data_path)
        self.target_column = target_column
        self.test_size = test_size
        self.results = {}
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.scaler = None
        
    def explore_data(self):
        """Display dataset information and statistics"""
        print("="*80)
        print("DATA EXPLORATION")
        print("="*80)
        print(f"\nDataset Shape: {self.data.shape}")
        print(f"Number of Features: {self.data.shape[1] - 1}")
        print(f"Number of Instances: {self.data.shape[0]}")
        
        print("\nColumn Data Types:")
        print(self.data.dtypes)
        
        print("\nMissing Values:")
        print(self.data.isnull().sum())
        
        print(f"\nTarget Variable Distribution:")
        print(self.data[self.target_column].value_counts())
        
        print("\nBasic Statistics:")
        print(self.data.describe())
    
    def preprocess_data(self):
        """
        Preprocess data: encode categorical variables, scale features
        """
        print("\n" + "="*80)
        print("DATA PREPROCESSING")
        print("="*80)
        
        # Separate features and target
        X = self.data.drop(columns=[self.target_column])
        y = self.data[self.target_column]
        
        # Round quality to nearest integer (convert continuous to discrete)
        y = y.round().astype(int)
        
        # Handle categorical variables
        label_encoders = {}
        for col in X.select_dtypes(include=['object']).columns:
            le = LabelEncoder()
            X[col] = le.fit_transform(X[col].astype(str))
            label_encoders[col] = le
            print(f"Encoded column: {col}")
        
        # Encode target variable if categorical
        if y.dtype == 'object':
            le_target = LabelEncoder()
            y = le_target.fit_transform(y)
            label_encoders['target'] = le_target
            print(f"Encoded target variable")
        
        # Train-test split with stratification
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=self.test_size, random_state=42
        )
        
        print(f"\nTrain set size: {len(self.X_train)}")
        print(f"Test set size: {len(self.X_test)}")
        
        # Feature scaling
        self.scaler = StandardScaler()
        self.X_train_scaled = self.scaler.fit_transform(self.X_train)
        self.X_test_scaled = self.scaler.transform(self.X_test)
        
        print("Features scaled using StandardScaler")
    
    def train_models(self):
        """
        Train all 5 classification models
        """
        print("\n" + "="*80)
        print("MODEL TRAINING")
        print("="*80)
        
        models = {
            'Logistic Regression': LogisticRegression(
                max_iter=1000, random_state=42, solver='lbfgs'
            ),
            'Decision Tree': DecisionTreeClassifier(
                random_state=42, max_depth=15
            ),
            'K-Nearest Neighbor': KNeighborsClassifier(
                n_neighbors=5
            ),
            'Naive Bayes': GaussianNB(),
            'Random Forest (Ensemble)': RandomForestClassifier(
                n_estimators=100, random_state=42, n_jobs=-1
            )
        }
        
        for model_name, model in models.items():
            print(f"\nTraining {model_name}...", end=" ")
            
            # Train model
            model.fit(self.X_train_scaled, self.y_train)
            
            # Make predictions
            y_pred = model.predict(self.X_test_scaled)
            y_pred_proba = model.predict_proba(self.X_test_scaled)[:, 1] \
                if hasattr(model, 'predict_proba') else None
            
            # Store model and predictions
            self.results[model_name] = {
                'model': model,
                'y_pred': y_pred,
                'y_pred_proba': y_pred_proba
            }
            
            print("✓ Complete")
    
    def evaluate_models(self):
        """
        Evaluate all models using 6 metrics
        """
        print("\n" + "="*80)
        print("MODEL EVALUATION")
        print("="*80)
        
        metrics_data = []
        
        for model_name, result in self.results.items():
            y_pred = result['y_pred']
            y_pred_proba = result['y_pred_proba']
            
            # Calculate metrics
            accuracy = accuracy_score(self.y_test, y_pred)
            precision = precision_score(
                self.y_test, y_pred, average='weighted', zero_division=0
            )
            recall = recall_score(
                self.y_test, y_pred, average='weighted', zero_division=0
            )
            f1 = f1_score(
                self.y_test, y_pred, average='weighted', zero_division=0
            )
            mcc = matthews_corrcoef(self.y_test, y_pred)
            
            # AUC calculation
            try:
                if len(np.unique(self.y_test)) == 2:
                    auc = roc_auc_score(self.y_test, y_pred_proba)
                else:
                    auc = roc_auc_score(
                        self.y_test, 
                        result['model'].predict_proba(self.X_test_scaled),
                        multi_class='ovr', average='weighted'
                    )
            except:
                auc = 0.0
            
            # Store metrics
            metrics_data.append({
                'Model': model_name,
                'Accuracy': accuracy,
                'AUC': auc,
                'Precision': precision,
                'Recall': recall,
                'F1 Score': f1,
                'MCC': mcc
            })
            
            self.results[model_name]['metrics'] = {
                'Accuracy': accuracy,
                'AUC': auc,
                'Precision': precision,
                'Recall': recall,
                'F1 Score': f1,
                'MCC': mcc
            }
        
        self.metrics_df = pd.DataFrame(metrics_data)
        
        print("\n" + "-"*80)
        print("METRICS COMPARISON TABLE")
        print("-"*80)
        print(self.metrics_df.to_string(index=False))
        
        # Find best model
        best_model = self.metrics_df.loc[
            self.metrics_df['Accuracy'].idxmax(), 'Model'
        ]
        best_accuracy = self.metrics_df['Accuracy'].max()
        
        print("\n" + "-"*80)
        print(f"🏆 BEST MODEL: {best_model} (Accuracy: {best_accuracy:.4f})")
        print("-"*80)
    
    def detailed_analysis(self):
        """
        Print detailed analysis for each model
        """
        print("\n" + "="*80)
        print("DETAILED MODEL ANALYSIS")
        print("="*80)
        
        for model_name, result in self.results.items():
            print(f"\n{'='*80}")
            print(f"MODEL: {model_name}")
            print(f"{'='*80}")
            
            # Print metrics
            print("\nMetrics:")
            for metric, value in result['metrics'].items():
                print(f"  {metric}: {value:.4f}")
            
            # Print confusion matrix
            cm = confusion_matrix(self.y_test, result['y_pred'])
            print(f"\nConfusion Matrix:\n{cm}")
            
            # Print classification report
            print("\nClassification Report:")
            print(classification_report(
                self.y_test, result['y_pred'], zero_division=0
            ))
    
    def save_results(self, output_file='model_metrics.csv'):
        """
        Save metrics to CSV file
        """
        self.metrics_df.to_csv(output_file, index=False)
        print(f"\n✓ Metrics saved to {output_file}")
    
    def visualize_results(self):
        """
        Create visualizations for model comparison
        """
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        fig.suptitle('Model Performance Comparison', fontsize=16, fontweight='bold')
        
        metrics = ['Accuracy', 'AUC', 'Precision', 'Recall', 'F1 Score', 'MCC']
        
        for idx, metric in enumerate(metrics):
            ax = axes[idx // 3, idx % 3]
            
            values = self.metrics_df[metric]
            colors = plt.cm.viridis(np.linspace(0, 1, len(values)))
            
            bars = ax.bar(range(len(values)), values, color=colors)
            ax.set_xticks(range(len(values)))
            ax.set_xticklabels(
                [m.replace(' ', '\n') for m in self.metrics_df['Model']],
                rotation=45, ha='right', fontsize=8
            )
            ax.set_ylabel('Score')
            ax.set_title(metric)
            ax.set_ylim([0, 1])
            
            # Add value labels on bars
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height,
                       f'{height:.3f}', ha='center', va='bottom', fontsize=8)
        
        plt.tight_layout()
        plt.savefig('model_comparison.png', dpi=300, bbox_inches='tight')
        print("\n✓ Visualization saved to model_comparison.png")
        plt.show()

def main():
    """
    Main execution function
    """
    print("\n" + "🤖 MACHINE LEARNING MODELS COMPARISON 🤖".center(80))
    print("="*80 + "\n")
    
    # Configuration
    data_path = 'wine.csv'      # Change to your dataset
    target_column = 'quality'          # Change to your target column
    test_size = 0.2
    
    # Initialize comparison framework
    ml_comparison = MLModelComparison(data_path, target_column, test_size)
    
    # Execute pipeline
    ml_comparison.explore_data()
    ml_comparison.preprocess_data()
    ml_comparison.train_models()
    ml_comparison.evaluate_models()
    ml_comparison.detailed_analysis()
    ml_comparison.save_results()
    ml_comparison.visualize_results()
    
    print("\n" + "="*80)
    print("✓ ANALYSIS COMPLETE")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
