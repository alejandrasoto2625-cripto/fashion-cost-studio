
import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Fashion Cost Studio",
    page_icon="✂️",
    layout="wide"
)

# Diseño visual
st.markdown("""
<style>
.stApp {
    background-color: #F5F2EC;
}
h1, h2, h3, p, label {
    color: #292722;
}
div.stButton > button {
    background-color: #292722;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 10px 22px;
}
</style>
""", unsafe_allow_html=True)

# Título
st.title("FASHION COST STUDIO")
st.caption("GARMENT COSTING & PRODUCTION MANAGEMENT")
st.divider()

st.subheader("Calculadora de costos de prendas")
st.write("Registra los costos de fabricación y calcula el presupuesto de producción.")

# Formulario
with st.form("formulario_costos"):
    col1, col2 = st.columns(2)

    with col1:
        prenda = st.selectbox(
            "Tipo de prenda",
            ["Camiseta", "Pantalón", "Bermuda", "Hoodie", "Otra"]
        )
        cantidad = st.number_input(
            "Cantidad a producir",
            min_value=1,
            value=100,
            step=1
        )
        costo_tela = st.number_input(
            "Costo de tela por unidad ($)",
            min_value=0.0,
            value=15000.0
        )

    with col2:
        costo_confeccion = st.number_input(
            "Costo de confección por unidad ($)",
            min_value=0.0,
            value=12000.0
        )
        costo_insumos = st.number_input(
            "Costo de insumos por unidad ($)",
            min_value=0.0,
            value=3500.0
        )
        margen = st.number_input(
            "Margen de utilidad (%)",
            min_value=0.0,
            value=40.0
        )

    calcular = st.form_submit_button("CALCULAR COSTOS")

# Procesamiento
if calcular:

    # Sumar los costos unitarios
    costo_unitario = costo_tela + costo_confeccion + costo_insumos

    # Calcular costo total de producción
    costo_total = costo_unitario * cantidad

    # Aplicar margen de utilidad
    precio_venta = costo_unitario * (1 + margen / 100)

    # Clasificar el costo con condicionales
    if costo_unitario < 20000:
        categoria = "Costo bajo"
    elif costo_unitario <= 40000:
        categoria = "Costo medio"
    else:
        categoria = "Costo alto"

    # Mostrar resultados
    st.divider()
    st.subheader("RESULTADOS DEL COSTEO")

    a, b, c = st.columns(3)

    a.metric("Costo unitario", f"${costo_unitario:,.0f}")
    b.metric("Costo total", f"${costo_total:,.0f}")
    c.metric("Precio de venta", f"${precio_venta:,.0f}")

    st.info(f"Clasificación de la prenda: {categoria}")

    # Ciclo for para mostrar el detalle
    st.subheader("Detalle de costos")

    conceptos = {
        "Tela": costo_tela,
        "Confección": costo_confeccion,
        "Insumos": costo_insumos
    }

    for concepto, valor in conceptos.items():
        st.write(f"**{concepto}:** ${valor:,.0f}")

    # Ciclo while para validar la cantidad
    contador = 0
    while contador < cantidad:
        contador += 1

    st.success(
        f"Se validaron correctamente {contador} unidades de producción."
    )
