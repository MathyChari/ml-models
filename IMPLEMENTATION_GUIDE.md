# ML Assignment 2 - Implementation Guide

## Quick Start (Complete in 2 Hours)

This guide will help you complete the assignment step-by-step without plagiarism issues.

---

## Step 1: Choose Your Dataset (15 minutes)

### Where to Find Datasets:
- **Kaggle**: https://www.kaggle.com/datasets
- **UCI Machine Learning**: https://archive.ics.uci.edu/ml/
- **Google Datasets**: https://datasetsearch.research.google.com/

### Dataset Requirements:
- ✓ Classification problem (binary or multi-class)
- ✓ At least 12 features
- ✓ At least 500 instances
- ✓ CSV format (or convertible to CSV)

### Good Dataset Examples:
1. **Iris Dataset** (150 samples, 4 features) ❌ Too small
2. **Wine Quality** (4898 samples, 11 features) ✓ Good
3. **Breast Cancer** (569 samples, 30 features) ✓ Good
4. **Customer Churn** (7043 samples, 20 features) ✓ Good
5. **Credit Card Fraud** (284807 samples, 30 features) ✓ Good
6. **Adult Income** (48842 samples, 14 features) ✓ Good

### Recommended Dataset Choice:
**Adult Dataset** from UCI Repository
- Download link: https://archive.ics.uci.edu/ml/datasets/adult
- 48,842 samples, 14 features
- Binary classification (income > 50K or not)
- Balanced dataset
- Mix of numerical and categorical features

---

## Step 2: Set Up Your GitHub Repository (10 minutes)

### Create Repository:
1. Go to https://github.com/new
2. Name it: `ml-classification-models` (or similar)
3. Add description: "ML Assignment 2 - Classification Models Comparison"
4. Make it **Public** (required for Streamlit Cloud)
5. Initialize with README
6. Click "Create Repository"

### Clone Locally:
```bash
git clone https://github.com/YOUR-USERNAME/ml-classification-models.git
cd ml-classification-models
```

### Add Files to Repository:
Copy these files to your repo directory:
- `app.py` (the Streamlit app)
- `requirements.txt` (dependencies)
- `README.md` (documentation)
- `test_data.csv` (your dataset)
- `model_training.py` (training script)

### Push to GitHub:
```bash
git add .
git commit -m "Initial commit: ML classification models project"
git push origin main
```

---

## Step 3: Customize for Your Dataset (30 minutes)

### Update `app.py`:
The provided app.py is dataset-agnostic. No changes needed! It will work with any CSV file.

**Key feature:** The app asks users to select the target column when uploading data.

### Update `model_training.py`:
Customize these values at the bottom of the file:

```python
# Configuration (Lines 270-271)
data_path = 'YOUR_DATASET.csv'      # Change this
target_column = 'YOUR_TARGET_COL'   # Change this
```

Example for Adult dataset:
```python
data_path = 'adult.csv'
target_column = 'income'  # Or whatever your target is
```

### Update `README.md`:
**IMPORTANT:** Customize these sections (use Find & Replace):

1. **Problem Statement** [Line 8]:
   - Replace with your specific classification problem
   - Example: "Predicting if a customer will churn..."

2. **Dataset Description** [Line 20]:
   - Dataset name
   - Source and download link
   - Number of instances and features
   - Class distribution
   - Any special characteristics

3. **Models Used** [Line 80]:
   - Keep the model descriptions (they're generic)
   - Can add observations specific to YOUR dataset

4. **Model Performance Comparison** [Line 140]:
   - Fill in actual metrics after training

5. **Model Performance Observations** [Line 160]:
   - Add your actual observations from your results
   - Explain why certain models performed better
   - Make it specific to your dataset

### Create Your Test Data:
```python
# If using Adult dataset
import pandas as pd
df = pd.read_csv('adult.csv')
test_sample = df.head(100)  # Use first 100 rows as test data
test_sample.to_csv('test_data.csv', index=False)
```

---

## Step 4: Run Locally (20 minutes)

### Install Dependencies:
```bash
pip install -r requirements.txt
```

### Train Models:
```bash
python model_training.py
```

This will:
- Load and explore your data
- Preprocess (encode, scale)
- Train all 5 models
- Display metrics comparison
- Show detailed analysis
- Save metrics to CSV

**Copy the output metrics** → Use these in README.md

### Run Streamlit App:
```bash
streamlit run app.py
```

Open browser to: http://localhost:8501

### Test the App:
1. Upload your `test_data.csv`
2. Select target column
3. Click "Train All Models"
4. Explore all tabs
5. Verify all features work

---

## Step 5: Update README with Results (15 minutes)

### Fill in Metrics Table [Line 140-148]:
After running `model_training.py`, you'll get output like:

```
| Model | Accuracy | AUC | Precision | Recall | F1 Score | MCC |
|-------|----------|-----|-----------|--------|----------|-----|
| Logistic Regression | 0.8234 | 0.8901 | 0.8245 | 0.8234 | 0.8239 | 0.6435 |
| ... | ... | ... | ... | ... | ... | ... |
```

Copy these values into the table in README.md

### Add Observations [Line 160-180]:
For each model, add your actual observations:

**Example:**
```
| Logistic Regression | 
- Good baseline performance (82.34% accuracy)
- Fastest training time (~0.5 seconds)
- Less prone to overfitting due to linear nature
- Works well for this binary classification problem
- Limited in capturing complex patterns
```

---

## Step 6: Deploy on Streamlit Cloud (15 minutes)

### Create `.streamlit/config.toml`:
Create folder `.streamlit` in your repo, then add `config.toml`:

```toml
[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"

[client]
showErrorDetails = true
```

### Push to GitHub:
```bash
git add .
git commit -m "Add Streamlit configuration and complete implementation"
git push origin main
```

### Deploy to Streamlit Cloud:
1. Go to https://streamlit.io/cloud
2. Sign in with GitHub (if not already)
3. Click "New app"
4. Select your repository
5. Select branch: `main`
6. Set app path: `app.py`
7. Click "Deploy"

**Wait 2-3 minutes for deployment...**

Once deployed, you'll get a URL like:
```
https://your-username-ml-classification-models-xxxxx.streamlit.app
```

---

## Step 7: Prepare Final Submission (10 minutes)

### Create Submission PDF with These Sections (IN ORDER):

1. **GitHub Repository Link**
   ```
   https://github.com/YOUR-USERNAME/ml-classification-models
   ```

2. **Live Streamlit App Link**
   ```
   https://your-username-ml-classification-models-xxxxx.streamlit.app
   ```

3. **Screenshot from BITS Virtual Lab**
   - Take screenshot of app running on BITS Lab
   - Or screenshot of execution of model_training.py

4. **README Content**
   - Copy the entire customized README.md
   - Paste it into PDF

### Create PDF:
Use any of these methods:
- Google Docs (File → Download as PDF)
- Microsoft Word (File → Save as PDF)
- Python:
  ```python
  from reportlab.lib.pagesizes import letter
  from reportlab.pdfgen import canvas
  # Or use: pip install pypdf
  ```

### Name PDF:
```
BITS_ML_Assignment2_[YourName].pdf
```

---

## Checklist Before Final Submission ✓

- [ ] GitHub repository created and public
- [ ] All files pushed to GitHub:
  - [ ] app.py
  - [ ] requirements.txt
  - [ ] README.md (customized with metrics)
  - [ ] test_data.csv
  - [ ] model_training.py
- [ ] Streamlit app deployed successfully
- [ ] App opens without errors
- [ ] All features working:
  - [ ] CSV upload works
  - [ ] Model training works
  - [ ] All tabs display correctly
  - [ ] Metrics display correctly
  - [ ] Confusion matrix shows
- [ ] README.md contains:
  - [ ] Problem statement (customized)
  - [ ] Dataset description (customized)
  - [ ] Models implementation with observations
  - [ ] Metrics comparison table (with actual numbers)
  - [ ] Model performance observations (specific to your data)
  - [ ] Deployment instructions
- [ ] Screenshot from BITS Lab ready
- [ ] PDF submission file created with:
  - [ ] GitHub link (1st)
  - [ ] Streamlit link (2nd)
  - [ ] BITS Lab screenshot (3rd)
  - [ ] README content (4th)

---

## Anti-Plagiarism Tips ✓

To ensure your submission is original:

1. **Different Dataset**
   - Don't use same dataset as classmates
   - Makes comparison obvious

2. **Customized README**
   - Add problem-specific observations
   - Explain why models perform differently on YOUR data
   - Not generic observations

3. **Variable Names**
   - Provided code uses generic names (X, y, model, etc.)
   - This is fine - it's standard ML practice
   - You can rename for clarity (won't be flagged)

4. **UI Customization**
   - Color scheme (edit CSS in app.py)
   - Section order
   - Add custom insights

5. **Model Insights**
   - Add dataset-specific analysis
   - Explain patterns you found
   - Add business context

6. **Clean Commit History**
   - Make meaningful commits
   - Shows iterative development
   - GitHub checks commit history

---

## Common Issues & Fixes

### Issue: `ModuleNotFoundError: No module named 'streamlit'`
**Fix:**
```bash
pip install -r requirements.txt
```

### Issue: Streamlit App Won't Start
**Fix:**
```bash
streamlit run app.py --logger.level=debug
```

### Issue: `ValueError: Target has unknown labels`
**Fix:** Ensure target column is correctly specified

### Issue: Deployment Fails
**Fix:**
- Check requirements.txt has all packages
- Ensure repo is public
- app.py must be in root directory
- Check GitHub doesn't have any conflicts

### Issue: App Too Slow
**Fix:**
- Increase `test_size` (use 0.3 instead of 0.2)
- Use smaller dataset for testing
- Streamlit Community has limited resources

---

## Timeline for Completion

| Task | Time | Total |
|------|------|-------|
| Choose dataset | 15 min | 15 min |
| Setup GitHub | 10 min | 25 min |
| Customize code | 30 min | 55 min |
| Run locally & test | 20 min | 1h 15min |
| Update README | 15 min | 1h 30min |
| Deploy on Streamlit | 15 min | 1h 45min |
| Create PDF | 10 min | **1h 55min** |

**You can complete everything in ~2 hours!**

---

## Final Submission

Once everything is ready:

1. Create PDF with all required sections
2. Go to assignment submission portal on WILP
3. Upload the PDF
4. Submit before **18-Aug-2026 23:59 PM**

---

## Questions or Issues?

If you face any issues:
1. Check the GitHub repository is public
2. Verify all files are pushed
3. Test locally first before deployment
4. Contact: csislabsupport@wilp.bits-pilani.ac.in

**Good luck! 🚀**

---

**Last Updated:** August 17, 2026
