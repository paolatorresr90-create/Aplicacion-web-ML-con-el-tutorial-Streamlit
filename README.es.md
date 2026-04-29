# 🍷 Wine Quality Predictor (Streamlit App)

¡Bienvenida/o! Este proyecto es una evolución de mi predictor de calidad de vino, ahora integrado en una interfaz interactiva y profesional utilizando **Streamlit**. La aplicación permite a los usuarios ajustar parámetros químicos en tiempo real para obtener predicciones basadas en un modelo de Machine Learning de alto rendimiento.

🚀 **Prueba la aplicación en vivo aquí:** (https://pawi-web-ml-con-el-tutorial-streamlit.onrender.com/)

---

## 🌟 Mejoras en esta versión
A diferencia de la versión anterior en Flask, esta aplicación incluye:
- **Validación de Datos:** Controles numéricos que fuerzan el formato correcto (ej. `0.5` en lugar de `.5`) para evitar errores de procesamiento.
- **Interfaz Reactiva:** Los resultados se muestran de forma inmediata y elegante.
- **Manejo de Errores:** Bloques `try/except` para asegurar que la aplicación sea robusta frente a fallos inesperados.

---

## 🧐 ¿Cómo funciona?
El modelo utiliza el algoritmo **XGBoost** para clasificar vinos en dos categorías:
1. **Alta Calidad ✨**
2. **Calidad Promedio 🍷**

### Parámetros de entrada:
- **Alcohol:** Porcentaje de volumen.
- **Acidez Volátil:** Cantidad de ácido acético.
- **Sulfatos:** Aditivos antimicrobianos.
- **Ácido Cítrico:** Factor de frescura.
- **Dióxido de Azufre Total:** Concentración de SO2.

---

## 🛠️ Tecnologías
- **Streamlit:** Para la creación de la interfaz web.
- **XGBoost:** Algoritmo de Gradient Boosting para la predicción.
- **Python 3.11:** Lenguaje base.
- **Render:** Hosting y despliegue continuo.

---

## 📂 Estructura del Proyecto
```text
.
├── app.py              # Lógica de Streamlit y carga del modelo
├── wine_model_xgb.pkl  # Modelo entrenado (binario)
├── requirements.txt    # Librerías necesarias
├── Procfile            # Configuración para el despliegue en Render
└── README.md           # Documentación del proyecto
