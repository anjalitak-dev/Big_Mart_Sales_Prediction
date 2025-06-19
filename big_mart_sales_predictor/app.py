from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the saved model
model = joblib.load('bigdatamodel.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/predict', methods=['POST'])
def predict():

    if request.method == 'POST':
        try:
            # Get form data (example)
            item_identifier = int(request.form['item_identifier'])
            item_weight = float(request.form['item_weight'])
            item_fat_content = int(request.form['item_fat_content'])
            item_visibility = float(request.form['item_visibility'])
            item_type = int(request.form['item_type'])
            item_mrp = float(request.form['item_mrp'])
            outlet_identifier = int(request.form['outlet_identifier'])
            outlet_establishment_year = int(request.form['outlet_establishment_year'])
            outlet_size = int(request.form['outlet_size'])
            outlet_location_type = int(request.form['outlet_location_type'])
            outlet_type = int(request.form['outlet_type'])

            # Prepare the feature array
            features = np.array([[item_identifier, item_weight, item_fat_content, item_visibility,
                                  item_type, item_mrp, outlet_identifier, outlet_establishment_year,
                                  outlet_size, outlet_location_type, outlet_type]])

            # Make prediction
            prediction = model.predict(features)
            return render_template('prediction.html', prediction=prediction[0])

        except Exception as e:
            return str(e)

if __name__ == '__main__':
    app.run(debug=True)
