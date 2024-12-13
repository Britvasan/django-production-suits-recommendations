import mysql.connector
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'brit',
    'database': 'project'
}

def fetch_data_from_db():
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT orders, order_type, customization, recommended_product FROM recommendation_data")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return pd.DataFrame(data)

def train_recommendation_model():
    # Fetch data from the database
    data = fetch_data_from_db()

    # Initialize LabelEncoders
    encoders = {
        'orders': LabelEncoder(),
        'order_type': LabelEncoder(),
        'customization': LabelEncoder(),
        'recommended_product': LabelEncoder()
    }

    if data.empty:
        raise ValueError("No data available for training the model.")

    # Encode data
    X = pd.DataFrame({
        'orders': encoders['orders'].fit_transform(data['orders']),
        'order_type': encoders['order_type'].fit_transform(data['order_type']),
        'customization': encoders['customization'].fit_transform(data['customization'])
    })
    y = encoders['recommended_product'].fit_transform(data['recommended_product'])

    # Train model
    model = PassiveAggressiveClassifier()
    model.fit(X, y)
    accuracy = accuracy_score(y, model.predict(X))

    return model, encoders, accuracy

def predict_recommended_product(model, encoders, orders, order_type, customization):

    # if orders is None or order_type is None or customization is None:
    # return "Missing required input data."

    try:
        # Encode inputs
        orders_encoded = encoders['orders'].transform([orders])[0]
        order_type_encoded = encoders['order_type'].transform([order_type])[0]
        customization_encoded = encoders['customization'].transform([customization])[0]
        X_test = [[orders_encoded, order_type_encoded, customization_encoded]]

        # Predict and decode
        recommended_encoded = model.predict(X_test)[0]
        recommended_product = encoders['recommended_product'].inverse_transform([recommended_encoded])[0]
        return recommended_product
    except ValueError as e:
        return "No suitable recommendation found for the provided input."
















