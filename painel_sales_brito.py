# Painel @sales_brito - Estilo Militar (Versão Streamlit)
# Adaptado para rodar no Streamlit Cloud

import streamlit as st
from datetime import datetime
import os

# ----------------------------
# Configuração Inicial
# ----------------------------
st.set_page_config(page_title="Painel @sales_brito", layout="wide")
st.markdown("""
    <style>
    .main {
        background-color: #1a1f1c;
        color: #c9c9c9;
        font-family: 'Courier New', monospace;
        background-image: url('https://www.transparenttextures.com/patterns/camo-light.png');
    }
    .stTextInput>div>div>input {
        background-color: #333;
        color: #fff;
    }
    .stButton>button {
        background-color: #28a745;
        color: white;
        font-weight: bold;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# Autenticação Simples
# ----------------------------
def login():
    st.title("🪖 Painel Tático @sales_brito")
    st.subheader("🔒 Acesso Restrito")
    user = st.text_input("Usuário")
    passwd = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if user == "sales_brito" and passwd == "PMGO2025!":
            st.session_state['logado'] = True
            st.success("Acesso liberado, soldado!")
        else:
            st.error("Credenciais incorretas. Missão abortada.")

# ----------------------------
# Painel Principal
# ----------------------------
def dashboard():
    st.sidebar.title("🎖 Missões")
    aba = st.sidebar.radio("Escolha sua operação:", ["📓 Anotações", "📅 Agenda", "📁 Uploads"])
    st.title(f"🎯 Painel do Operacional: @sales_brito")

    if aba == "📓 Anotações":
        st.subheader("📓 Diário de Missões")
        anotacao = st.text_area("Registrar nova missão:")
        if st.button("Salvar Missão"):
            with open("anotacoes_streamlit.txt", "a") as f:
                f.write(f"[{datetime.now().strftime('%d/%m/%Y %H:%M')}] {anotacao}\n")
            st.success("Missão registrada com sucesso!")

        if os.path.exists("anotacoes_streamlit.txt"):
            with open("anotacoes_streamlit.txt", "r") as f:
                conteudo = f.read()
                st.text_area("📖 Histórico de Missões", value=conteudo, height=300)

    elif aba == "📅 Agenda":
        st.subheader("📅 Planejamento do Dia")
        tarefa = st.text_input("Nova tarefa:")
        if st.button("Adicionar Tarefa"):
            with open("agenda_streamlit.txt", "a") as f:
                f.write(f"[ ] {tarefa}\n")
            st.success("Tarefa adicionada!")

        if os.path.exists("agenda_streamlit.txt"):
            with open("agenda_streamlit.txt", "r") as f:
                tarefas = f.readlines()
            st.write("### 📋 Lista de Tarefas")
            for t in tarefas:
                st.markdown(f"- {t.strip()}")

    elif aba == "📁 Uploads":
        st.subheader("📁 Upload de Arquivos")
        uploaded = st.file_uploader("Envie seus arquivos táticos:")
        if uploaded:
            with open(f"uploads/{uploaded.name}", "wb") as f:
                f.write(uploaded.read())
            st.success(f"Arquivo '{uploaded.name}' salvo com sucesso!")

# ----------------------------
# Execução
# ----------------------------
if 'logado' not in st.session_state:
    st.session_state['logado'] = False

if not st.session_state['logado']:
    login()
else:
    dashboard()
