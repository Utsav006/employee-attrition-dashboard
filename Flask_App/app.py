from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load all three trained models into a dictionary for fast routing
deployed_models = {
    'lr': joblib.load('../Model/lr_model.pkl'),
    'rf': joblib.load('../Model/rf_model.pkl'),
    'xgb': joblib.load('../Model/xgb_model.pkl')
}

# Engine names for frontend display mapping
engine_names = {
    'lr': 'Logistic Regression',
    'rf': 'Random Forest Classifier',
    'xgb': 'XGBoost Classifier'
}

model_features = joblib.load('../Model/model_features.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        input_data = pd.DataFrame(columns=model_features)
        input_data.loc[0] = 0  
        
        for key in request.form:
            if key in input_data.columns and key != 'engine':
                input_data.at[0, key] = float(request.form[key])
        
        # Identify which engine the user selected
        selected_engine_key = request.form.get('engine', 'lr')
        active_model = deployed_models[selected_engine_key]
        active_engine_name = engine_names[selected_engine_key]
        
        prediction = active_model.predict(input_data)[0]
        probability = active_model.predict_proba(input_data)[0][1]
        
        result = "Likely to Leave" if prediction == 1 else "Likely to Stay"
        output_text = f'Prediction: Employee is {result} (Risk Probability: {probability:.2%})'
        
        return render_template('index.html', prediction_text=output_text, active_engine=active_engine_name)

if __name__ == "__main__":
    app.run(debug=True)