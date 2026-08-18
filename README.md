# Machine Learning Classification Models Comparison

## Problem Statement

The objective of this project is to implement and compare multiple machine learning classification models on a real-world dataset. This project demonstrates a complete end-to-end machine learning workflow including data preprocessing, model training, evaluation, and deployment of an interactive web application.

The goal is to:
1. Implement 5 different classification algorithms
2. Evaluate each model using 6 different performance metrics
3. Compare model performance on the same dataset
4. Build an interactive Streamlit web application for model evaluation
5. Deploy the application on Streamlit Community Cloud for accessibility

This project serves as a practical demonstration of MLOps best practices including version control, reproducibility, and cloud deployment.

---

## Dataset Description

**Dataset Name:** Wine Quality Dataset

**Source:** Kaggle

**Dataset Link:** [https://www.kaggle.com/datasets/boiniabhiram/wine-quality-dataset?resource=download]

### Dataset Characteristics:
- **Number of Instances:** [Your instance count]
- **Number of Features:** [Your feature count]
- **Target Variable:** [Your target column name and classes]
- **Problem Type:** Binary / Multi-class Classification
- **Missing Values:** [Describe any missing data handling]
- **Class Distribution:** [Describe if balanced or imbalanced]

### Features Overview:
- **Numerical Features:** [List relevant numerical features]
- **Categorical Features:** [List relevant categorical features]
- **Feature Engineering:** [Any transformations applied]

### Data Preprocessing Steps:
1. **Handling Missing Values:** Used [method] to handle missing data
2. **Categorical Encoding:** Applied Label Encoding to categorical variables
3. **Feature Scaling:** Applied StandardScaler for numerical features
4. **Train-Test Split:** 80-20 split with stratification for class balance
5. **Normalization:** All features standardized to zero mean and unit variance

---

## GitHub Repository Link

**Repository:** [https://github.com/your-username/your-repo-name](your-github-repo-link)

### Repository Structure:
```
project-folder/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── test_data.csv            # Test dataset for evaluation
├── model/
│   ├── logistic_regression.py    # Model training scripts
│   ├── decision_tree.py
│   ├── knn.py
│   ├── naive_bayes.py
│   ├── random_forest.py
│   └── model_comparison.ipynb    # Jupyter notebook with complete analysis
└── results/
    └── model_metrics.csv    # Exported metrics
```

### Repository Contents:
- ✓ Complete source code with detailed comments
- ✓ requirements.txt with all dependencies
- ✓ Clear README.md documentation
- ✓ Test data (CSV) used in experiments
- ✓ Model training and evaluation code
- ✓ Streamlit application configuration

---

## Models Used

### 1. Logistic Regression
- **Description:** Linear classification model using logistic function
- **Type:** Linear Model
- **Hyperparameters:** max_iter=1000, solver='lbfgs'
- **Use Case:** Baseline model, efficient for binary and multiclass problems

### 2. Decision Tree Classifier
- **Description:** Tree-based model that splits data recursively
- **Type:** Tree-based Model
- **Hyperparameters:** max_depth=15, random_state=42
- **Use Case:** Interpretable model, captures non-linear relationships

### 3. K-Nearest Neighbor (KNN)
- **Description:** Instance-based learning using k closest neighbors
- **Type:** Instance-based Model
- **Hyperparameters:** n_neighbors=5
- **Use Case:** Simple baseline, sensitive to feature scaling

### 4. Naive Bayes
- **Description:** Probabilistic model based on Bayes' theorem
- **Type:** Probabilistic Model
- **Implementation:** Gaussian Naive Bayes
- **Use Case:** Fast training, works well with smaller datasets

### 5. Random Forest (Ensemble)
- **Description:** Ensemble of decision trees with bootstrap aggregating
- **Type:** Ensemble Model
- **Hyperparameters:** n_estimators=100, n_jobs=-1
- **Use Case:** High performance, reduces overfitting, feature importance

---

## Evaluation Metrics

Six key metrics are used to evaluate all models:

1. **Accuracy**: Percentage of correct predictions
   - Formula: (TP + TN) / (TP + TN + FP + FN)
   - Best for: Balanced datasets

2. **AUC Score**: Area Under the Receiver Operating Characteristic Curve
   - Range: 0 to 1 (higher is better)
   - Best for: Imbalanced datasets, probabilistic predictions

3. **Precision**: Ratio of true positives among predicted positives
   - Formula: TP / (TP + FP)
   - Best for: When false positives are costly

4. **Recall**: Ratio of true positives among actual positives
   - Formula: TP / (TP + FN)
   - Best for: When false negatives are costly

5. **F1 Score**: Harmonic mean of precision and recall
   - Formula: 2 * (Precision * Recall) / (Precision + Recall)
   - Best for: Imbalanced datasets, overall balance

6. **MCC (Matthews Correlation Coefficient)**: Correlation between predicted and actual
   - Range: -1 to 1 (higher is better)
   - Best for: Imbalanced datasets, binary classification

---

## Model Performance Comparison

### Metrics Comparison Table

| ML Model Name | Accuracy | AUC | Precision | Recall | F1 Score | MCC |
|---|---|---|---|---|---|---|
| Logistic Regression | 0.5294 | 0.7060 | 0.4979 | 0.5294 | 0.5107 | 0.2268 |
| Decision Tree | 0.6206 | 0.7145 | 0.6306 | 0.6206 | 0.6216 | 0.4185 |
| K-Nearest Neighbor | 0.5706 | 0.7238 | 0.5502 | 0.5706 | 0.5559 | 0.3000 |
| Naive Bayes | 0.5000 | 0.6816 | 0.5104 | 0.5000 | 0.5041 | 0.2289 |
| Random Forest (Ensemble) | 0.6735 | 0.8302 | 0.6542 | 0.6735 | 0.6585 | 0.4707 |


---

## Model Performance Observations

### Performance Analysis by Model

| ML Model | Observations |
|---|---|
| **Logistic Regression** | <ul><li>Provides baseline performance with good training speed</li><li>[Add your observation about performance on your dataset]</li><li>[Note any strengths/weaknesses observed]</li></ul> |
| **Decision Tree** | <ul><li>Captures non-linear patterns in data</li><li>[Add your observation about performance on your dataset]</li><li>[Note if overfitting is observed]</li></ul> |
| **K-Nearest Neighbor** | <ul><li>Simple yet effective for classification tasks</li><li>[Add your observation about performance on your dataset]</li><li>[Note sensitivity to feature scaling]</li></ul> |
| **Naive Bayes** | <ul><li>Probabilistic approach with fast training</li><li>[Add your observation about performance on your dataset]</li><li>[Note performance characteristics]</li></ul> |
| **Random Forest (Ensemble)** | <ul><li>Ensemble approach provides robust predictions</li><li>[Add your observation about performance on your dataset]</li><li>[Note if it achieves best performance]</li></ul> |
| **Overall Winner for Dataset** | <ul><li>**Best Performing Model:** [Model Name]</li><li>**Reason:** [Explain why this model performs best]</li><li>**Key Advantage:** [Highlight the key strength]</li><li>**Recommendation:** [Suggest when to use this model]</li></ul> |

### Key Observations:

1. **Best Accuracy Model:** 
   - [Model name] achieved the highest accuracy of [X]%
   - This suggests [interpretation about data characteristics]

2. **Most Balanced Model (F1 Score):**
   - [Model name] provided the best balance between precision and recall
   - Suitable for [use case description]

3. **Overfitting Analysis:**
   - [Which models showed overfitting tendencies]
   - [Evidence from metrics]

4. **Computational Efficiency:**
   - [Fastest model]: [Model name]
   - [Most stable model]: [Model name]

5. **Dataset Characteristics:**
   - The dataset [characteristics] made [Model name] most suitable
   - [Other important findings]

---

## Streamlit Application

### Features Implemented

✓ **CSV Dataset Upload**: Upload your test data directly in the application  
✓ **Model Selection**: Dropdown to select and view individual model performance  
✓ **Metrics Display**: View all 6 metrics in tabular format  
✓ **Confusion Matrix**: Visual representation of model predictions  
✓ **Classification Report**: Detailed per-class performance metrics  
✓ **Performance Visualizations**: Charts comparing model performance  
✓ **Data Export**: Download metrics and results as CSV  

### How to Use the Application

1. **Upload Data**: Click on the sidebar file uploader and select your CSV file
2. **Configure Settings**: 
   - Select the target column from your dataset
   - Choose the test size ratio (recommended: 0.2)
3. **Train Models**: Click "Train All Models" to train all 5 models
4. **Explore Results**:
   - **Metrics Comparison Tab**: View all models' metrics side-by-side
   - **Model Details Tab**: Select individual model for detailed analysis
   - **Visualizations Tab**: View charts and comparative graphs
   - **About Tab**: Learn about each model type

---

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

### Local Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

5. **Access the application:**
   - Open your browser and go to `http://localhost:8501`

---

## Cloud Deployment (Streamlit Community Cloud)

### Deployment Steps

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Initial commit: ML models comparison app"
   git push origin main
   ```

2. **Deploy to Streamlit Cloud:**
   - Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
   - Sign in with your GitHub account
   - Click "New App"
   - Select your repository and branch
   - Set app path to `app.py`
   - Click "Deploy"

3. **Share the Link:**
   - Once deployed, Streamlit provides a shareable URL
   - Share this URL for evaluation

**Live Deployment Link:** [https://your-app-name.streamlit.app](your-deployment-link)

---

## Results & Conclusion

### Summary
This project successfully implements and compares 5 different machine learning classification models. The analysis reveals that [best model] provides the best performance with an accuracy of [X]% and F1 score of [Y], making it the recommended model for this dataset.

### Key Findings
1. [Finding 1]
2. [Finding 2]
3. [Finding 3]

### Recommendations
- Use [Model] for production deployment
- [Model] is suitable for [specific use case]
- Further improvements could include [suggestions]

---

## Technologies Used

- **Python 3.8+**: Programming language
- **Scikit-learn**: Machine learning algorithms
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib & Seaborn**: Data visualization
- **Streamlit**: Web application framework
- **Git/GitHub**: Version control
- **Streamlit Community Cloud**: Cloud deployment

---

## Author & Submission

**Student Name:** [Your Name]  
**Course:** M.Tech (AIML/DSE) - Machine Learning  
**Institution:** BITS Pilani  
**Submission Date:** [Date]  
**Assignment:** ML Assignment 2  

---

## References

1. Scikit-learn Documentation: https://scikit-learn.org/
2. Streamlit Documentation: https://docs.streamlit.io/
3. Dataset Source: [Your dataset source]
4. Machine Learning Concepts: [Any textbooks or references used]

---

## License

This project is created for educational purposes as part of BITS Pilani's M.Tech program.

---

**Last Updated:** [Date]  
**Status:** ✓ Completed and Deployed
