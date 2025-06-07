
import streamlit as st

st.set_page_config(page_title="Laura - Demo", page_icon="🤖")

st.title("Asistente Virtual Laura")
st.subheader("Demo inicial")
st.write("Hola, soy Laura. Estoy diseñada para ayudarte con tus pedidos de productos cárnicos.")

catalogo = {
    "Pechuga de pollo": "15.000 COP/kg",
    "Carne de res": "22.000 COP/kg",
    "Costilla de cerdo": "18.000 COP/kg",
    "Pollo entero": "13.500 COP/kg"
}

st.write("### Catálogo disponible:")
for producto, precio in catalogo.items():
    st.write(f"- {producto}: {precio}")

nombre = st.text_input("¿Cuál es tu nombre?")
producto = st.selectbox("¿Qué producto deseas?", list(catalogo.keys()))
cantidad = st.number_input("¿Cuántos kilos necesitas?", min_value=1, max_value=100, step=1)

if st.button("Hacer pedido"):
    if nombre and producto and cantidad:
        st.success(f"Gracias {nombre}, tu pedido de {cantidad} kg de {producto} ha sido registrado.")
    else:
        st.error("Por favor completa todos los campos.")

st.caption("Demo desarrollada para Carnicos15")
