📊 Insurance Company – Exploratory Data Analysis App
📌 Descripción del proyecto

Este proyecto consiste en el desarrollo de una aplicación interactiva de análisis exploratorio de datos (EDA) utilizando Python y Streamlit.

La aplicación permite analizar información de clientes de una compañía de seguros, con el objetivo de identificar patrones relacionados con la renovación de pólizas.

A través de diferentes visualizaciones y análisis estadísticos, se exploran variables demográficas, financieras y de comportamiento de pago que pueden influir en la decisión de un cliente de renovar o no su seguro.

Este proyecto fue desarrollado como parte del curso Python for Analytics.

🎯 Objetivos del proyecto

Aplicar técnicas de Análisis Exploratorio de Datos (EDA).

Desarrollar una aplicación interactiva con Streamlit.

Implementar Programación Orientada a Objetos (POO) en Python.

Analizar factores que influyen en la renovación de pólizas de seguros.

Presentar visualizaciones que faciliten la interpretación de los datos.

🗂 Dataset

El dataset utilizado contiene información de clientes de una compañía de seguros.

Algunas de las variables más relevantes incluyen:

Variable	Descripción
id	Identificador único del cliente
perc_premium_paid_by_cash_credit	Porcentaje de la prima pagada en efectivo o crédito
age_in_days	Edad del cliente en días
Income	Ingreso mensual del cliente
Count_3-6_months_late	Pagos atrasados entre 3 y 6 meses
Count_6-12_months_late	Pagos atrasados entre 6 y 12 meses
Count_more_than_12_months_late	Pagos atrasados mayores a 12 meses
application_underwriting_score	Puntaje de evaluación del cliente
no_of_premiums_paid	Número total de primas pagadas
sourcing_channel	Canal de captación del cliente
residence_area_type	Tipo de residencia (urbana o rural)
premium	Valor de la prima
renewal	Indica si el cliente renovó la póliza
⚙️ Tecnologías utilizadas

El proyecto fue desarrollado utilizando las siguientes herramientas:

Python

Pandas

NumPy

Matplotlib

Seaborn

Streamlit

Estas librerías permiten realizar análisis de datos, generar visualizaciones y crear aplicaciones web interactivas.

🧠 Estructura del análisis

La aplicación está dividida en diferentes secciones para facilitar la exploración del dataset:

🏠 Home

Presenta información general del proyecto, autor y tecnologías utilizadas.

📋 Carga del Dataset

Permite cargar el archivo CSV y visualizar:

Vista previa del dataset

Número de filas y columnas

🧮 Exploratory Data Analysis (EDA)

Incluye diferentes tipos de análisis:

Información general del dataset

Clasificación de variables numéricas y categóricas

Estadísticas descriptivas

Análisis de valores faltantes

Distribución de variables numéricas

Distribución de variables categóricas

Relación entre variables numéricas y categóricas

Relación entre variables categóricas

Análisis dinámico del dataset

Visualización de la renovación de pólizas

📝 Conclusiones

Se presentan los principales hallazgos obtenidos durante el análisis.

📊 Principales hallazgos

A partir del análisis exploratorio se identificaron algunos patrones importantes:

El nivel de ingreso del cliente influye en la capacidad de pago de primas.

Los clientes con más retrasos en pagos tienden a renovar menos sus pólizas.

El underwriting score está relacionado con el riesgo del cliente.

Algunos canales de captación generan clientes más propensos a renovar.

Existen diferencias en el comportamiento de renovación entre zonas urbanas y rurales.

🚀 Cómo ejecutar la aplicación

Clonar el repositorio:

git clone https://github.com/TU-USUARIO/insurance-renewal-analysis.git

Entrar a la carpeta del proyecto:

cd insurance-renewal-analysis

Instalar las dependencias:

pip install -r requirements.txt

Ejecutar la aplicación:

streamlit run app.py
🌐 Aplicación desplegada

La aplicación puede ejecutarse en línea a través de Streamlit Cloud.

🔗 Link de la aplicación:
(Agregar aquí el enlace cuando la app esté desplegada)

📁 Estructura del proyecto
insurance-renewal-analysis
│
├── app.py
├── InsuranceCompany.csv
├── requirements.txt
├── logo1.png
├── logo2.png
├── .gitignore
└── README.md
👩‍💻 Autor

Stephany Xiomara Pachas Sánchez
Curso: Python for Analytics
Año: 2026
