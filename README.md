# 📊 Insurance Company – Exploratory Data Analysis App
![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)

![License](https://img.shields.io/badge/License-MIT-green)

![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)

![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen)

![PRs](https://img.shields.io/badge/PRs-Welcome-orange)


# 📌 Descripción del proyecto

Este proyecto consiste en el desarrollo de una aplicación interactiva de análisis exploratorio de datos (EDA) utilizando Python y Streamlit.

La aplicación permite analizar información de clientes de una compañía de seguros, con el objetivo de identificar patrones relacionados con la renovación de pólizas.

A través de diferentes visualizaciones y análisis estadísticos, se exploran variables demográficas, financieras y de comportamiento de pago que pueden influir en la decisión de un cliente de renovar o no su seguro.

Este proyecto fue desarrollado como parte del curso Python for Analytics.

# 🎯 Objetivos del proyecto

. Aplicar técnicas de Análisis Exploratorio de Datos (EDA) de forma estructurada.

. Desarrollar una aplicación web interactiva y profesional con Streamlit.

. Implementar Programación Orientada a Objetos (POO) en Python para mantener un código limpio y escalable.

.  Analizar qué factores (ingresos, canales de venta, retrasos) influyen en la renovación de pólizas de seguros.

. Presentar visualizaciones claras que faciliten la toma de decisiones basada en datos.

# 🧠 Estructura de la Aplicación

La aplicación está dividida en un menú lateral intuitivo con 4 secciones principales:

🏠 Home: Presentación general del proyecto, descripción del caso de estudio y tecnologías aplicadas.

📋 Carga Dataset: Módulo dinámico para subir el archivo .csv, visualizar dimensiones y explorar las primeras filas del dataframe.

🧮 Exploratory Data Analysis (EDA): El corazón de la aplicación, dividido en 7 pestañas:

# Información general y tipos de datos.

- Estadísticas descriptivas.

- Distribución univariada de numéricas (Histogramas interactivos).

- Detección de Outliers (Boxplots).

- Análisis de variables categóricas (Gráficos de barras).

- Análisis Bivariado (Scatter plots dinámicos y agrupación por categorías).

- Matriz de Correlación térmica.

# 📝 Conclusiones: Resumen de los hallazgos de negocio más importantes.

  📊 Principales Hallazgos de Negocio

A partir del análisis exploratorio profundo, se lograron identificar los siguientes patrones clave:

- Influencia del Ingreso: El nivel de ingresos mensuales (Income) del cliente tiene una influencia directa en su capacidad de pagar primas más altas.

- Impacto de la Morosidad: Los clientes con historial de retrasos (especialmente en los rangos de 3-6 y 6-12 meses) tienen una probabilidad drásticamente menor de renovar sus pólizas.

- Underwriting Score: Esta puntuación refleja con precisión el perfil de riesgo; a mayor score, suele haber mayor estabilidad en los pagos y renovaciones.

- Canales de Captación (sourcing_channel): El análisis bivariado sugiere que ciertos canales de reclutamiento generan clientes con mayor retención a largo plazo en la compañía.

- Geografía: El análisis por área de residencia (Urbana vs Rural) demuestra diferencias sutiles pero importantes en los volúmenes de primas recaudadas.

🚀 Cómo ejecutar la aplicación localmente

Si deseas correr este proyecto en tu propia computadora, sigue estos pasos:

# 1. Clonar el repositorio:

git clone [https://github.com/TU-USUARIO/insurance-renewal-analysis.git](https://github.com/TU-USUARIO/insurance-renewal-analysis.git)


# 2. Entrar a la carpeta del proyecto:

cd insurance-renewal-analysis


# 3. Instalar las dependencias:

pip install -r requirements.txt


# 4. Ejecutar la aplicación en Streamlit:

streamlit run app.py


# 🌐 Aplicación Desplegada

La aplicación ha sido desplegada exitosamente en la nube utilizando Streamlit Community Cloud.

🔗 Link de la aplicación: (Reemplaza este texto con tu link real cuando despliegues la app)

# 📁 Estructura del repositorio

insurance-renewal-analysis/
│
├── app.py                   # Script principal de la aplicación Streamlit
├── InsuranceCompany.csv     # Dataset utilizado para el análisis
├── requirements.txt         # Dependencias del proyecto
├── logo1.png                # Logo principal de la app
├── logo2.png                # Logo del menú lateral
├── .gitignore               # Archivos a ignorar por git
└── README.md                # Documentación del proyecto (Este archivo)


# 👩‍💻 Autor

# Stephany Xiomara Pachas Sánchez 📚 Curso: Python for Analytics

# 📅 Año: 2026
