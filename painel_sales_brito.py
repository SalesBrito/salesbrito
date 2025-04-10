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
        background-color: #f4f6f9;
        color: #1a1a1a;
        font-family: 'Segoe UI', sans-serif;
    }
    .stTextInput>div>div>input {
        background-color: #ffffff;
        color: #000000;
    }
    .stButton>button {
        background-color: #2e7d32;
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
    st.title("🪖 Painel Militar @sales_brito")
    st.subheader("🔒 Acesso Restrito")
    st.markdown(
        "> A melhor frase que vocês vão ouvir: 'Você foi aprovado na PMGO!'"
    )
    user = st.text_input("Usuário")
    passwd = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if user == "sales_brito" and passwd == "PMGO2025!":
            st.session_state['logado'] = True
            st.success("Acesso liberado, soldado!")
        else:
            st.error("Credenciais incorretas. Tente novamente.")

# ----------------------------
# Painel Principal
# ----------------------------
def dashboard():
    st.sidebar.title("📋 Menu Principal")
    aba = st.sidebar.radio("Escolha uma seção:", ["📓 Anotações", "🗕 Agenda", "📁 Uploads", "📚 Estudos (PMGO)", "💰 Investimentos"])
    st.title(f"📌 Painel de Comando: @sales_brito")

    if aba == "📓 Anotações":
        st.subheader("📓 Diário de Estudos")
        anotacao = st.text_area("Digite sua anotação:")
        if st.button("Salvar Anotação"):
            with open("anotacoes_streamlit.txt", "a") as f:
                f.write(f"[{datetime.now().strftime('%d/%m/%Y %H:%M')}] {anotacao}\n")
            st.success("Anotação salva!")

        if os.path.exists("anotacoes_streamlit.txt"):
            with open("anotacoes_streamlit.txt", "r") as f:
                conteudo = f.read()
                st.text_area("📖 Histórico", value=conteudo, height=300)

    elif aba == "🗕 Agenda":
        st.subheader("📆 Planejamento Diário")
        tarefa = st.text_input("Adicionar tarefa:")
        if st.button("Adicionar"):
            with open("agenda_streamlit.txt", "a") as f:
                f.write(f"[ ] {tarefa}\n")
            st.success("Tarefa adicionada!")

        if os.path.exists("agenda_streamlit.txt"):
            with open("agenda_streamlit.txt", "r") as f:
                tarefas = f.readlines()
            st.write("### ✅ Tarefas do Dia")
            for t in tarefas:
                st.markdown(f"- {t.strip()}")

    elif aba == "📁 Uploads":
        st.subheader("📁 Enviar Arquivos")
        uploaded = st.file_uploader("Envie seus arquivos:")
        if uploaded:
            os.makedirs("uploads", exist_ok=True)
            with open(f"uploads/{uploaded.name}", "wb") as f:
                f.write(uploaded.read())
            st.success(f"Arquivo '{uploaded.name}' salvo com sucesso!")

    elif aba == "📚 Estudos (PMGO)":
        st.subheader("📚 Planejamento PMGO")
        st.markdown("**Horário Ideal de Estudo:** Tarde")

        st.markdown("#### 📅 Cronograma da Semana")
        if st.button("Carregar Modelo Semanal"):
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
            st.success("Cronograma semanal carregado!")

        if os.path.exists("cronograma_streamlit.txt"):
            with open("cronograma_streamlit.txt", "r") as f:
                conteudo = f.read()
                st.text_area("🗂️ Cronograma Editável", value=conteudo, height=400)

    elif aba == "💰 Investimentos":
        st.subheader("💰 Controle de Investimentos")
        st.markdown("**Meta:** Comprar uma moto 🏍️")
        st.markdown("**Corretora:** Rico")
        st.markdown("**Plataforma:** App ou PC")

        st.markdown("#### 📊 Acesso à Planilha:")
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
