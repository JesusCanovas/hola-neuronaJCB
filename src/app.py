import streamlit as st
import numpy as np

#st.set_page_config(layout="wide")
st.image('images/neurona1.png')
st.title('¡Hola neurona!')

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])
with tab1:
    st.header("Neurona con una entrada y un peso")
    
    st.subheader("Valor del peso", divider='rainbow')
    w0 = st.slider('Peso', 0.00 , 5.00, 0.1)
    
    st.subheader('Valor de la entrada', divider='rainbow')
    x0 = st.number_input("Valor de la entrada", key=1, step=1)
    
    st.subheader('Valor de salida', divider='rainbow')
    if st.button('Calcular la salida', key=2):
        st.divider()
        st.write(f"La salida de la neurona es:  {w0*x0}")

with tab2:
    st.header("Neurona con dos entradas y dos pesos")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Peso 1", divider='rainbow')
        w0 = st.slider("Peso $w_1$", 0.00 , 5.00, 0.1, key=3)
        st.subheader('Entrada 1', divider='rainbow')
        x0 = st.number_input("Entrada $x_2$", key=4, step=1)
    with col2:
        st.subheader("Peso 2", divider='rainbow')
        w1 = st.slider("Peso $w_2$", 0.00 , 5.00, 0.1, key=5)
        st.subheader('Entrada 2', divider='rainbow')
        x1 = st.number_input("Entrada $x_2$", key=6, step=1)
    st.subheader('Valor de salida', divider='rainbow')
    if st.button('Calcular la salida', key=7):
        st.divider()
        st.write(f"La salida de la neurona es:  { x0 * w0 + x1 * w1}")

with tab3:
    st.header("Neurona con tres entradas y sesgo")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Peso 1", divider='rainbow')
        w0 = st.slider("Peso $w_1$", 0.00 , 5.00, 0.1, key=8)
        st.subheader('Entrada 1', divider='rainbow')
        x0 = st.number_input("Entrada x1", key=9, step=1)
    with col2:
        st.subheader("Peso 2", divider='rainbow')
        w1 = st.slider("Peso $w_2$", 0.00 , 5.00, 0.1, key=10)
        st.subheader('Entrada 2', divider='rainbow')
        x1 = st.number_input("Entrada x2", key=11, step=1)
    with col3:
        st.subheader("Peso 3", divider='rainbow')
        w2 = st.slider("Peso $w_3$", 0.00 , 5.00, 0.1, key=12)
        st.subheader('Entrada 3', divider='rainbow')
        x2 = st.number_input("Entrada $x_3$", key=13, step=1)
    st.subheader('Valor del Sesgo', divider='rainbow')
    b = st.number_input("Introduzca el valor del sesgo", key=14, step=1)
    st.subheader('Valor de salida', divider='rainbow')
    if st.button('Calcular la salida', key=15):
        st.divider()
        st.write(f"La salida de la neurona es:  { x0 * w0 + x1 * w1 + x2 * w2 + b}")

st.divider()

st.markdown("© Jesús Cánovas Barqueros - CPIFP Alan Turing")
