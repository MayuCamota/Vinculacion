import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

def load_data():
    file_path = r"C:\Users\mariajose.campos\Documents\CursoRicky\integridad.csv"
    return pd.read_csv(file_path)

def main():
    st.title("Dashboard de Integridad Académica")
    
    df = load_data()
    
    # Verificar que las columnas existen
    required_columns = ["Universidad", "Licenciatura", "Integridad Académica"]
    if not all(col in df.columns for col in required_columns):
        st.error("El archivo CSV no contiene las columnas esperadas. Verifica la estructura del archivo.")
        return
    
    # Filtro por Universidad
    universidades = df["Universidad"].unique()
    universidad_seleccionada = st.selectbox("Selecciona una Universidad", universidades)
    df_filtrado = df[df["Universidad"] == universidad_seleccionada]
    
    # Filtro por Licenciatura (se habilita solo si hay universidad seleccionada)
    licenciaturas = df_filtrado["Licenciatura"].unique()
    licenciatura_seleccionada = st.selectbox("Selecciona una Licenciatura", licenciaturas)
    df_final = df_filtrado[df_filtrado["Licenciatura"] == licenciatura_seleccionada]
    
    # Verificar si hay datos para graficar
    if df_final.empty:
        st.warning("No hay datos disponibles para la selección actual.")
        return
    
    # Gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(df_final["Licenciatura"], df_final["Integridad Académica"], color='skyblue')
    ax.set_xlabel("Licenciatura")
    ax.set_ylabel("Integridad Académica")
    ax.set_title("Integridad Académica por Licenciatura")
    st.pyplot(fig)
    
    # Botón para descargar la gráfica
    buf = BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    st.download_button(label="Descargar gráfica", data=buf, file_name="grafica_integridad.png", mime="image/png")
    
if __name__ == "__main__":
    main()
