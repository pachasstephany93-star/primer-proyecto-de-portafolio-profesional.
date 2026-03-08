import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io

# Configuración de la página
st.set_page_config(page_title="Insurance EDA", layout="wide")
st.image("logo1.png", width=1200)



# =====================================
# CLASE (Programación Orientada a Objetos)
# =====================================

class DataAnalyzer:

    def __init__(self, df):
        self.df = df

    def classify_variables(self):
        numeric = self.df.select_dtypes(include=np.number).columns.tolist()
        categorical = self.df.select_dtypes(include="object").columns.tolist()
        return numeric, categorical

    def missing_values(self):
        return self.df.isnull().sum()

    def descriptive_stats(self):
        return self.df.describe()

    def histogram(self, column):
        fig, ax = plt.subplots()
        sns.histplot(self.df[column], kde=True, ax=ax)
        ax.set_title(f"Distribución de {column}")
        return fig

    def bar_chart(self, column):
        fig, ax = plt.subplots()
        self.df[column].value_counts().plot(kind="bar", ax=ax)
        ax.set_title(f"Frecuencia de {column}")
        return fig


# =====================================
# SIDEBAR (MENÚ PRINCIPAL)
# =====================================

st.sidebar.title("Menú Principal")
st.sidebar.image("logo2.png")

menu = st.sidebar.selectbox(
    "Seleccionar sección",
    ["🏠 Home",
     "📋 Carga Dataset",
     "🧮 EDA",
     "📝 Conclusiones"]
)

# =====================================
# HOME
# =====================================

if menu == "🏠 Home":

    st.title(" 🧮 Insurance Company -  Exploratory Data Analysis ")

    st.write("""
    Aplicación desarrollada en Streamlit para realizar análisis exploratorio
    del dataset InsuranceCompany.
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Autor")
        st.write("**Nombre:** Stephany Xiomara Pachas Sánchez")
        st.write("**Curso:** Python for Analytics")
        st.write("**Año:** 2026")
        
    with col2:
        st.subheader("Tecnologías utilizadas")

        st.write("""
        - Python
        - Pandas
        - NumPy
        - Matplotlib
        - Seaborn
        - Streamlit
        """) 
    st.divider()   
    
    st.subheader("Descripción del Dataset")

    st.write("""
    El dataset InsuranceCompany contiene información de clientes de una
    compañía de seguros, incluyendo datos demográficos, historial de pagos
    de primas y comportamiento de renovación de pólizas.

    El objetivo del análisis exploratorio es identificar patrones que
    permitan entender qué factores influyen en la renovación de seguros.
    """)
    
    

    

# =====================================
# CARGA DEL DATASET
# =====================================

elif menu == "📋 Carga Dataset":

    file = st.file_uploader("Cargar archivo CSV", type=["csv"])

    if file is not None:

        df = pd.read_csv(file)

        st.success("Archivo cargado correctamente")

        st.subheader("Vista previa del dataset")
        st.dataframe(df.head())

        st.subheader("Dimensiones del dataset")
        st.write("Filas:", df.shape[0])
        st.write("Columnas:", df.shape[1])

        st.session_state["df"] = df

    else:

        st.warning("Debe cargar el dataset para continuar")

# =====================================
# EDA
# =====================================

elif menu == "🧮 EDA":

    if "df" not in st.session_state:

        st.warning("Primero debes cargar el dataset")

    else:

        df = st.session_state["df"]

        analyzer = DataAnalyzer(df)

        tabs = st.tabs([
            "Info Dataset",
            "Clasificación Variables",
            "Estadísticas",
            "Valores Faltantes",
            "Distribución Numérica",
            "Variables Categóricas",
            "Numérico vs Categórico",
            "Categórico vs Categórico",
            "Análisis Dinámico",
            "Hallazgos"
        ])

        # TAB 1
        with tabs[0]:

            st.subheader("Información del Dataset")
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("Tipos de datos")
                st.write(df.dtypes)
                
            with col2:
                st.write("### Dimensiones del dataset")
                st.write("Filas:", df.shape[0])
                st.write("Columnas:", df.shape[1])        
            
            st.divider()
            st.write("### Información detallada")
            
            buffer = io.StringIO()
            df.info(buf=buffer)
            st.text(buffer.getvalue())
        # TAB 2
        with tabs[1]:
            
            st.subheader("Clasificación de Variables")
            
            num, cat = analyzer.classify_variables()
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("Variables Numéricas")
                st.write(num)
            with col2:
                st.write("Variables Categóricas")
                st.write(cat)

        # TAB 3
        with tabs[2]:
            
            st.subheader("Estadísticas Descriptivas")
            st.dataframe(analyzer.descriptive_stats())
            st.divider()
            st.subheader("Moda de las variables")
            st.dataframe(df.mode().iloc[0].to_frame("Moda"))
            
        # TAB 4
        with tabs[3]:
            st.subheader("Valores Faltantes")
            missing = analyzer.missing_values()
            st.dataframe(missing)
            fig, ax = plt.subplots()
            missing.plot(kind="bar", ax=ax)
            ax.set_title("Valores faltantes por variable")
            st.pyplot(fig)
            
        # TAB 5
        with tabs[4]:
            st.subheader("Distribución de Variables Numéricas")
            num, cat = analyzer.classify_variables()

            column = st.selectbox("Selecciona variable numérica", num)

            fig = analyzer.histogram(column)

            st.pyplot(fig)

        # TAB 6
        with tabs[5]:
            st.subheader("Distribución de Variables Categóricas")
            num, cat = analyzer.classify_variables()

            column = st.selectbox("Selecciona variable categórica", cat)

            fig = analyzer.bar_chart(column)

            st.pyplot(fig)

        # TAB 7
        with tabs[6]:
           
           
            st.subheader("Relación Numérico vs Categórico")
            num, cat = analyzer.classify_variables()

            n = st.selectbox("Variable numérica", num)
            c = st.selectbox("Variable categórica", cat)
           
            fig, ax = plt.subplots()
            sns.boxplot(x=df[c], y=df[n], ax=ax)
            ax.set_title(f"{n} según {c}")
            
            st.pyplot(fig)

           
        
        with tabs[7]:

            st.subheader(" Relación Categórico vs Categórico")

            col1 = st.selectbox("Variable 1", cat)
            col2 = st.selectbox("Variable 2", cat)

            tabla = pd.crosstab(df[col1], df[col2])

            st.dataframe(tabla)

            fig, ax = plt.subplots()
            sns.heatmap(tabla, annot=True, cmap="Blues")
            ax.set_title("Mapa de calor")
            st.pyplot(fig)
            
        with tabs[8]:

            st.subheader("Análisis Dinámico")

            columnas = st.multiselect("Selecciona columnas", df.columns)
            mostrar = st.checkbox("Mostrar datos")         
            filas = st.slider("Número de filas", 5, 50, 10)
            
            if mostrar and columnas:
                st.dataframe(df[columnas].head(filas))   
                 
        with tabs[9]:

            st.subheader("Hallazgos principales")

            fig, ax = plt.subplots()

            sns.countplot(x="renewal", data=df, ax=ax)
            
            ax.set_title("Renovación de pólizas")
            
            st.pyplot(fig)
            
            st.write("""
            Insight:
            Se observa la proporción de clientes que renuevan la póliza
            frente a los que no lo hacen.
            """)
# =====================================
# CONCLUSIONES
# =====================================  

elif menu == "📝 Conclusiones":

    st.title("Conclusiones")

    st.write("""
    1. El ingreso del cliente influye en el pago de primas.
    2. Los clientes con más retrasos presentan menor renovación.
    3. El underwriting score está relacionado con el riesgo del cliente.
    4. Algunos canales de captación generan clientes más fieles.
    5. Existen diferencias entre zonas urbanas y rurales.
    """)