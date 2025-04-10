# Painel @sales_brito - Estilo Militar Moderno (Versão Streamlit)
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
        background-color: #f0f2f6;
        color: #1a1a1a;
        font-family: 'Segoe UI', sans-serif;
    }
    .stTextInput>div>div>input {
        background-color: #ffffff;
        color: #000000;
    }
    .stButton>button {
        background-color: #004d40;
        color: white;
        font-weight: bold;
        border-radius: 8px;
    }
    .stTextArea textarea {
        background-color: #ffffff;
        color: #000000;
        font-family: 'Segoe UI', sans-serif;
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
    aba = st.sidebar.radio("Escolha sua operação:", ["📓 Anotações", "🗕 Agenda", "📁 Uploads", "📚 Estudos (PMGO)", "💰 Investimentos"])
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

    elif aba == "🗕 Agenda":
        st.subheader("🗕 Planejamento do Dia")
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
            os.makedirs("uploads", exist_ok=True)
            with open(f"uploads/{uploaded.name}", "wb") as f:
                f.write(uploaded.read())
            st.success(f"Arquivo '{uploaded.name}' salvo com sucesso!")

    elif aba == "📚 Estudos (PMGO)":
        st.subheader("📚 Missão PMGO: Estudo Diário")
        st.markdown("**Frase Motivacional:** A melhor frase que vocês vão ouvir: 'Você foi aprovado na PMGO!' 🏆")
        st.markdown("**Horário Ideal de Estudo:** Tarde")

        st.markdown("#### 🧽 Cronograma Tático (Automático)")
        if st.button("Carregar Modelo da Semana"):
            with open("cronograma_streamlit.txt", "w") as f:
                f.write("""
Segunda-feira
Manhã: Penal: Crimes contra a Pessoa | CTB: Conceitos
Tarde: Legislação PMGO: Estrutura | Direitos Humanos: Princípios
Noite: Redação: Estrutura | Português: Pontuação

Terça-feira
Manhã: Penal: Patrimônio | CTB: Penalidades
Tarde: Legislação PMGO: Hierarquia | DH: Declaração Universal
Noite: Redação: Tema Livre | Português: Pronomes

Quarta-feira
Manhã: Penal: Crimes em Espécie | CTB: Sinalização
Tarde: Legislação PMGO: Estatuto | DH: Intervenção Policial
Noite: Simulado Geral | Flashcards

Quinta-feira
Manhã: Penal: Parte Geral | CTB: Infrações
Tarde: Legislação PMGO: Conduta | DH: Casos Práticos
Noite: Redação: Argumentação | Português: Concordância

Sexta-feira
Manhã: Penal: Revisão Geral | CTB: Questões
Tarde: Legislação: Revisão | DH: Questões
Noite: Flashcards | Redação: Reescrita

Sábado
Manhã: Questões QConcursos | Mapas Mentais
Tarde: Revisão Geral | Flashcards
Noite: Vídeos Gran Cursos | Avaliação Semanal

Domingo
Livre ou Reposição
Autoavaliação | Planejamento
""")
            st.success("Modelo de cronograma carregado!")

        if os.path.exists("cronograma_streamlit.txt"):
            with open("cronograma_streamlit.txt", "r") as f:
                conteudo = f.read()
                st.text_area("📚 Cronograma da Semana (Editável)", value=conteudo, height=400)

    elif aba == "💰 Investimentos":
        st.subheader("💰 Controle de Investimentos")
        st.markdown("**Meta:** Comprar uma moto 🏍️")
        st.markdown("**Corretora:** Rico")
        st.markdown("**Plataforma:** App ou PC")

        st.markdown("#### 📊 Planilha de Controle:")
        link_planilha = "https://docs.google.com/spreadsheets/d/1Zx-8DruS4RigITNLxiKwddiVD8Ne38YVKjXgXoqWP0Q"
        st.markdown(f"📌 [Abrir planilha de investimentos]({link_planilha})")

# ----------------------------
# Execução
# ----------------------------
if 'logado' not in st.session_state:
    st.session_state['logado'] = False

if not st.session_state['logado']:
    login()
else:
    dashboard()
