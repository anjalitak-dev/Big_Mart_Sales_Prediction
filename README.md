# 🛒 BigMart Sales Predictor – Flask Web App

This project is a web-based sales prediction application built using **Flask** and a **machine learning model** trained to estimate the sales of items in a retail store based on various item and outlet attributes.

It allows users to input product and outlet details via a user-friendly interface and get a sales prediction as output. The model is served using Flask and uses a `joblib`-saved `.pkl` file for inference.

---

## 🚀 Features

- 🏪 **Retail Sales Prediction**  
  Predicts item sales using features such as item weight, fat content, visibility, MRP, outlet type, and more.

- 🌐 **Web Interface**  
  Clean and intuitive frontend powered by HTML templates rendered via Flask.

- ⚙️ **Pre-trained Model Integration**  
  Uses a `bigdatamodel.pkl` file trained on historical data (e.g., from BigMart dataset).

- 📄 **Multiple Pages**  
  Includes Home (`/`), About (`/about`), Login (`/login`), and Prediction (`/predict`) routes.

---

## 🛠 Technologies Used

| Component         | Technology          |
|------------------|---------------------|
| Backend Framework| Flask               |
| ML Model         | Scikit-learn (saved with Joblib) |
| Frontend         | HTML, CSS (via templates) |
| Language         | Python              |
| Deployment Ready | Yes (Local or cloud platforms) |



