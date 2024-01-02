# cement_Strength

# Cement Strength Prediction
Live Demo
Check out the live demo of the deployed application: https://cement-strength.onrender.com

This project implements a machine learning model to predict the strength of cement based on various input features. The model is trained using the Random Forest algorithm.

## Files

- `Cement_Strength_Prediction.ipynb`: Python script containing the code for training the Random Forest model. The trained model is saved along with the scaler used for data normalization.

- `app.py`: Flask web application that allows users to input cement composition data and get predictions for the cement strength using the pre-trained model.

## Getting Started

### Prerequisites

Make sure you have the following dependencies installed:

- Python (version 3.6 or higher)
- Flask
- scikit-learn

Install the required Python packages using:

```bash
pip install flask scikit-learn
```


#Usage
#Launch the Flask app using the instructions above.

Fill in the input form on the webpage with the required cement composition details:

Cement (component 1)
Blast Furnace Slag (component 2)
Fly Ash (component 3)
Water (component 4)
Superplasticizer (component 5)
Coarse Aggregate (component 6)
Fine Aggregate (component 7)
Age (day)
Click the "Predict" button to get the predicted cement strength.
