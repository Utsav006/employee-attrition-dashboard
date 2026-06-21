# Employee Attrition Prediction System 🏢📊

**Predictive HR Intelligence Dashboard**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.4.0-orange.svg)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-2.0.0-red.svg)](https://xgboost.readthedocs.io/)
[![Status](https://img.shields.io/badge/Status-Live-success.svg)](https://employee-attrition-dashboard.onrender.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 Project Overview

The **Employee Attrition Prediction System** is an enterprise-grade machine learning application designed to help Human Resource departments proactively identify employees at high risk of leaving the organization. By analyzing multidimensional operational and psychometric data, this system shifts HR management from a reactive *"exit-interview"* paradigm to a proactive, data-driven retention strategy.

> 🌐 **Live Deployment:** [https://employee-attrition-dashboard.onrender.com](https://employee-attrition-dashboard.onrender.com)

*This project was developed as a Capstone Project for the **AIML Summer Internship 2026**, hosted at IIHMF, MNNIT Allahabad, Prayagraj, Uttar Pradesh, India.*

---

## 🚀 Key Features

- **Predictive Algorithmic Engine:** Deploys a highly calibrated **Logistic Regression** model as the Primary Engine (F1: **0.6374**, ROC-AUC: **0.7712**) for reliable attrition prediction.
- **Multi-Model Benchmarking:** Trains and evaluates three classifiers — Logistic Regression, XGBoost, and Random Forest — with live comparative performance displayed on the dashboard.
- **Class Imbalance Mitigation:** Implements the Synthetic Minority Over-sampling Technique (**SMOTE**) to mathematically balance training data and eliminate majority-class bias (~84% stayed vs ~16% left).
- **Interactive Dashboard:** A clean, dark-themed web interface titled *"Predictive HR Intelligence System"* built with Flask, featuring Predictive Parameters input, Diagnostic Outputs, and a Comparative Algorithm Performance panel.
- **Selectable Prediction Engine:** Users can switch between Logistic Regression, XGBoost, and Random Forest directly from the dashboard UI.
- **IBM HR Analytics Dataset:** Trained on the industry-standard IBM Watson HR dataset containing 1,470 employee records across 35 features.
- **Production-Ready Deployment:** Deployed live on **Render** using a **Gunicorn** WSGI server.

---

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| **Backend Framework** | Python 3.10+, Flask 3.0.0 |
| **Machine Learning** | Scikit-Learn 1.4.0, XGBoost 2.0.0 |
| **Imbalanced Data** | Imbalanced-Learn (SMOTE) |
| **Data Manipulation** | Pandas, NumPy |
| **Model Serialization** | Joblib (.pkl) |
| **Production Server** | Gunicorn |
| **Frontend** | HTML5, CSS3 |
| **Dataset** | IBM HR Analytics Employee Attrition |

---

## 📁 Project Structure

```
EMPLOYEE ATTRITION PREDICTION SYSTEM/
│
├── Dataset/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv   # IBM HR Analytics dataset
│
├── Documentation/
│   └── Employee_Attrition_Report.docx           # Project report
│
├── Flask_App/
│   ├── templates/
│   │   ├── index.html                           # Main prediction dashboard
│   │   └── about.html                           # About page
│   └── app.py                                   # Main Flask application
│
├── Model/
│   ├── attrition_model.pkl                      # Primary deployed model (Logistic Regression)
│   ├── lr_model.pkl                             # Logistic Regression model
│   ├── rf_model.pkl                             # Random Forest model
│   ├── xgb_model.pkl                            # XGBoost model
│   └── model_features.pkl                       # Saved feature list for inference
│
├── Notebook/
│   └── Attrition_Analysis.ipynb                 # EDA, training & evaluation notebook
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 📊 Dataset

**IBM HR Analytics Employee Attrition & Performance Dataset**

| Property | Details |
|---|---|
| **Source** | IBM Watson Analytics / Kaggle |
| **Records** | 1,470 employees |
| **Features** | 35 attributes |
| **Target** | `Attrition` (0 = Stayed, 1 = Left) |
| **Class Distribution** | ~1,233 Stayed (84%) · ~237 Left (16%) |

Key features used for prediction include: `Age`, `MonthlyIncome`, `JobLevel`, `OverTime`, `TotalWorkingYears`, `YearsAtCompany`, `YearsInCurrentRole`, `YearsWithCurrManager`, `WorkLifeBalance`, `JobSatisfaction`, `DistanceFromHome`, `NumCompaniesWorked`, and more.

**Notable Correlations (from EDA Heatmap):**
- `MonthlyIncome` ↔ `JobLevel` — strong positive correlation
- `TotalWorkingYears` ↔ `Age`, `MonthlyIncome` — strong positive correlation
- `YearsAtCompany` ↔ `YearsInCurrentRole`, `YearsWithCurrManager` — strong positive correlation
- `PercentSalaryHike` ↔ `PerformanceRating` — strong positive correlation

---

## 🤖 Model Performance

All models were trained with **SMOTE** applied on the training set to handle class imbalance, then evaluated on a held-out test set. The dashboard displays live comparative metrics during inference.

| Algorithm | F1 Score | ROC-AUC | Deployment Status |
|---|---|---|---|
| **Logistic Regression** ✅ | **0.6374** | **0.7712** | **Primary Engine** |
| XGBoost Classifier | 0.6105 | 0.7588 | Secondary |
| Random Forest | 0.5821 | 0.7430 | Tertiary |

> **✅ Primary Engine: Logistic Regression**
>
> Logistic Regression was selected as the primary deployed model due to its highest F1 Score (**0.6374**) and best ROC-AUC (**0.7712**) among all three candidates. In an HR attrition context, the ROC-AUC score is a critical indicator of a model's ability to discriminate between employees who will stay vs. leave — making Logistic Regression the most reliable end-to-end performer for this use case. Users may also switch to XGBoost or Random Forest via the dashboard's engine selector.

---

## 💻 Local Installation

**1. Clone the repository:**
```bash
git clone https://github.com/Utsav006/employee-attrition-dashboard.git
cd employee-attrition-dashboard
```

**2. (Recommended) Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Run the Flask application:**
```bash
cd Flask_App
python app.py
```

**5. Access the dashboard:**

Open your browser and navigate to `http://127.0.0.1:5000/`

---

## ☁️ Deployment (Render)

This application is live at **[https://employee-attrition-dashboard.onrender.com](https://employee-attrition-dashboard.onrender.com)**.

**Procfile** (include in root):
```
web: gunicorn Flask_App.app:app
```

To redeploy or fork and deploy your own instance:
1. Push your repository to GitHub.
2. Create a new **Web Service** on [Render](https://render.com/) and connect your GitHub repo.
3. Set the **Start Command** to: `gunicorn Flask_App.app:app`
4. Set **Python version** to `3.10` or higher.
5. Deploy — Render will automatically install from `requirements.txt`.

---

## 🖥️ Usage

1. Open the [live dashboard](https://employee-attrition-dashboard.onrender.com) in your browser.
2. Under **Predictive Parameters**, select your preferred **Prediction Engine** (default: Logistic Regression).
3. Fill in the employee's HR metrics in the input form.
4. Submit to receive results in the **Diagnostic Outputs** panel, including:
   - **Attrition Risk Label** — *High Risk* or *Low Risk*
   - **Probability Score** — the model's confidence percentage
5. View the **Comparative Algorithm Performance** table to compare all three models side-by-side.
6. Visit the **About** page for methodology, dataset, and model details.

---

## 🔬 Methodology

```
IBM HR Analytics Dataset (1,470 records)
              │
              ▼
  Exploratory Data Analysis (EDA)
  ├── Correlation Heatmap (25 numerical features)
  └── Attrition Distribution → 84% : 16% imbalance identified
              │
              ▼
      Data Preprocessing
  ├── Label Encoding (categorical → numerical)
  ├── Feature Scaling (StandardScaler)
  └── Feature Selection → model_features.pkl
              │
              ▼
  SMOTE (Synthetic Minority Over-sampling)
  └── Balances minority class (Attrition = 1) on training set
              │
              ▼
        Model Training
  ├── Logistic Regression  → lr_model.pkl   [F1: 0.6374 | AUC: 0.7712] ✅ Primary
  ├── XGBoost Classifier   → xgb_model.pkl  [F1: 0.6105 | AUC: 0.7588]
  └── Random Forest        → rf_model.pkl   [F1: 0.5821 | AUC: 0.7430]
              │
              ▼
  Best Model → attrition_model.pkl (Logistic Regression)
              │
              ▼
  Flask Web App (Dashboard + About page)
  └── Live engine selector — switch models at runtime
              │
              ▼
  Gunicorn → Render → https://employee-attrition-dashboard.onrender.com
```

---

## 📦 Dependencies

```
flask==3.0.0
scikit-learn==1.4.0
xgboost==2.0.0
imbalanced-learn==0.12.0
pandas==2.2.0
numpy==1.26.0
joblib==1.3.2
gunicorn==21.2.0
```

Install all at once:
```bash
pip install -r requirements.txt
```

---

## 🙌 Acknowledgements

- **IBM Watson Analytics** for providing the open-source HR Attrition dataset.
- **IIHMF, MNNIT Allahabad** for hosting the AIML Summer Internship 2026 and providing the academic framework for this capstone.
- The open-source communities behind Scikit-Learn, XGBoost, Imbalanced-Learn, and Flask.

---

## 👨‍💻 Author

**Utsav Singh**

- 2nd-Year Student, B.Tech in Computer Science and Engineering — **United College of Engineering and Research (UCER)**
- B.S. Data Science (pursuing) — **IIT Madras**
- Internship Host: **IIHMF, MNNIT Allahabad**, Prayagraj, Uttar Pradesh, India
- 🐙 [GitHub: Utsav006](https://github.com/Utsav006)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<p align="center">Made with ❤️ as part of AIML Summer Internship 2026</p>