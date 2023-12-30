from flask import Flask, request, render_template
import numpy as np
import joblib

# Flask app
app = Flask(__name__)

# Load the pre-trained model and the fitted scaler
loaded_model = joblib.load('cement_strength_rf.joblib')
scaler = joblib.load('scaler.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get input values from the form
        Cement_component = float(request.form['Cement (component 1)(kg in a m^3 mixture)'])
        Blast_Furnace_Slag = float(request.form['Blast Furnace Slag (component 2)(kg in a m^3 mixture)'])
        Fly_Ash = float(request.form['Fly Ash (component 3)(kg in a m^3 mixture)'])
        Water = float(request.form['Water (component 4)(kg in a m^3 mixture)'])
        Superplasticizer = float(request.form['Superplasticizer (component 5)(kg in a m^3 mixture)'])
        Coarse_Aggregate = float(request.form['Coarse Aggregate (component 6)(kg in a m^3 mixture)'])
        Fine_Aggregate = float(request.form['Fine Aggregate (component 7)(kg in a m^3 mixture)'])
        Age_day = float(request.form['Age (day)'])

        # Organize the input features as a numpy array
        features = np.array([[Cement_component, Blast_Furnace_Slag, Fly_Ash, Water, Superplasticizer, Coarse_Aggregate,
                              Fine_Aggregate, Age_day]])

        # Scale the input data using the fitted scaler
        scaled_test_data = scaler.transform(features)

        # Make prediction using the pre-trained model
        prediction = loaded_model.predict(scaled_test_data)

        return render_template('index.html', prediction=prediction[0])

if __name__ == "__main__":
    app.run(debug=True)

