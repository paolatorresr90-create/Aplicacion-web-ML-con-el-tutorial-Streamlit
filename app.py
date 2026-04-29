import streamlit as st
import pickle
import numpy as np

# Configuración de la página
st.set_page_config(page_title="Predictor de Vino Tinto", page_icon="🍷")

# Cargar el modelo
try:
    model = pickle.load(open('wine_model_xgb.pkl', 'rb'))
except FileNotFoundError:
    st.error("No se encontró el archivo del modelo. Asegúrate de que 'wine_model_xgb.pkl' esté en la misma carpeta.")

st.title("🍷 Predicción de Calidad de Vino Tinto")
st.write("Ingresa las propiedades del vino para evaluar su calidad.")

# Usamos columnas para que se vea más organizado
col1, col2 = st.columns(2)

with col1:
    # Validación: step=0.1 fuerza el formato decimal y ayuda a evitar errores de parseo
    alcohol = st.number_input("Alcohol", min_value=0.0, max_value=20.0, value=10.5, step=0.1)
    volatile_acidity = st.number_input("Acidez Volátil", min_value=0.0, max_value=2.0, value=0.5, step=0.01)
    sulphates = st.number_input("Sulfatos", min_value=0.0, max_value=2.0, value=0.6, step=0.01)

with col2:
    citric_acid = st.number_input("Ácido Cítrico", min_value=0.0, max_value=1.0, value=0.3, step=0.01)
    total_sulfur_dioxide = st.number_input("Dióxido de Azufre Total", min_value=0.0, max_value=300.0, value=40.0, step=1.0)

# Botón de predicción
if st.button("Predecir Calidad"):
    try:
        # Los datos deben estar en el mismo orden que el entrenamiento
        features = np.array([[alcohol, volatile_acidity, sulphates, citric_acid, total_sulfur_dioxide]])
        prediction = model.predict(features)
        
        if prediction[0] == 1:
            st.success("✨ ¡Excelente elección! Es un vino de alta calidad.")
        else:
            st.warning("🍷 Es un vino de calidad promedio.")
            
    except Exception as e:
        st.error(f"Hubo un error al procesar la predicción: {e}")