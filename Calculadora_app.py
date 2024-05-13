import time
import streamlit as st

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y

def potenciacao(x, y):
    return x ** y

def radiciacao(x, y):
    return x ** (1/y)

st.title(":violet[Calculadora]")
st.write(":grey[Feito por Anna Beatriz C. Silva]")

st.write(" ")
x = st.number_input(":violet[Escolha o primeiro número]")
y = st.number_input(":violet[Escolha o segundo número]")

opcao = st.radio(":violet[Escolha uma operação]", ["Adição", "Subtração", "Multiplicação", "Divisão", "Potenciação", "Radiciação"])

st.write(" ")

if st.button("Calcular"):
    with st.spinner(text="Calculando..."):
        time.sleep(3)
    if opcao == "Adição":
        resultado = soma(x, y)
    elif opcao == "Subtração":
        resultado = subtracao(x, y)
    elif opcao == "Multiplicação":
        resultado = multiplicacao(x, y)
    elif opcao == "Divisão":
        resultado = divisao(x, y)
    elif opcao == "Potenciação":
        resultado = potenciacao(x, y)
    elif opcao == "Radiciação":
        resultado = radiciacao(x, y)
    st.balloons()
    st.success("Feito!")
    st.write("Resultado: ", resultado)
