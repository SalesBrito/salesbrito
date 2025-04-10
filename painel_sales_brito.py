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
    .stTextArea textarea {
        background-color: #222;
        color: #0f0;
        font-family: 'Courier New', monospace;
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
    aba = st.sidebar.radio("Escolha sua operação:", ["📓 Anotações", "📅 Agenda", "📁 Uploads", "📚 Estudos (PMGO)", "💰 Investimentos"])
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
            os.makedirs("uploads", exist_ok=True)
            with open(f"uploads/{uploaded.name}", "wb") as f:
                f.write(uploaded.read())
            st.success(f"Arquivo '{uploaded.name}' salvo com sucesso!")

    elif aba == "📚 Estudos (PMGO)":
        st.subheader("📚 Missão PMGO: Estudo Diário")
        st.markdown("**Frase Motivacional:** A melhor frase que vocês vão ouvir: 'Você foi aprovado na PMGO!' 🏆")
        st.markdown("**Horário Ideal de Estudo:** Tarde")

        st.markdown("#### 🧭 Cronograma Semanal por Matéria e Turno")
        dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        turnos = ["Manhã", "Tarde", "Noite"]
        materias = ["Direito Penal", "CTB", "Legislação PMGO", "Direitos Humanos", "Português", "Redação"]
        cronograma = {}

        for dia in dias_semana:
            with st.expander(f"📅 {dia}"):
                cronograma[dia] = {}
                for turno in turnos:
                    cronograma[dia][turno] = {}
                    st.markdown(f"**{turno}:**")
                    for materia in materias:
                        assunto = st.text_input(f"{materia}", key=f"{dia}_{turno}_{materia}")
                        cronograma[dia][turno][materia] = assunto

        st.markdown("#### 📆 Resumo do Cronograma da Semana")
        for dia in dias_semana:
            st.markdown(f"**{dia}**:")
            for turno in turnos:
                materias_assuntos = [f"{materia}: {cronograma[dia][turno][materia]}" for materia in materias if cronograma[dia][turno][materia]]
                if materias_assuntos:
                    st.markdown(f"- {turno}: " + ", ".join(materias_assuntos))

        st.markdown("#### 📌 Metas da Semana")
        metas = [
            "Finalizar aula de Legislação",
            "Revisar Penal com flashcards",
            "Fazer 30 questões de CTB",
            "Simulado Completo",
            "Resumo de Direitos Humanos"
        ]
        for meta in metas:
            st.checkbox(meta)

        st.markdown("#### 🧠 Técnicas de Estudo")
        st.markdown("- Pomodoro (25/5)\n- Mapas Mentais\n- Flashcards (Anki)\n- Revisão Espaçada\n- Questões diárias (QConcursos / Gran)")

        st.markdown("#### 🔁 Revisão Programada")
        st.markdown("- Dia 1 após o estudo\n- Dia 7\n- Dia 30")

        st.markdown("#### 🔗 Plataformas Utilizadas")
        st.markdown("- [Gran Cursos](https://www.grancursosonline.com.br)\n- [QConcursos](https://www.qconcursos.com)\n- [AnkiWeb](https://apps.ankiweb.net/)\n- [Google Drive](https://drive.google.com/drive/folders/1Zx-8DruS4RigITNLxiKwddiVD8Ne38YVKjXgXoqWP0Q)")

        st.markdown("#### 📂 Materiais e Revisões")
        link_drive = "https://drive.google.com/drive/folders/1Zx-8DruS4RigITNLxiKwddiVD8Ne38YVKjXgXoqWP0Q"
        st.markdown(f"📎 [Acessar pasta de materiais no Google Drive]({link_drive})")

        st.markdown("#### 🧾 Simulados e Revisões Prontas")
        st.markdown("- 📄 [Simulado PMGO - PDF](#)\n- 📄 [Resumo CTB - PDF](#)\n- 📄 [Flashcards Direitos Humanos - PDF](#)")

    elif aba == "💰 Investimentos":
        st.subheader("💰 Controle de Investimentos")
        st.markdown("**Meta:** Comprar uma moto 🏍️")
        st.markdown("**Corretora:** Rico")
        st.markdown("**Plataforma:** App ou PC")

        st.markdown("#### 📊 Planilha de Controle:")
        link_planilha = "https://docs.google.com/spreadsheets/d/1Zx-8DruS4RigITNLxiKwddiVD8Ne38YVKjXgXoqWP0Q"
        st.markdown(f"📎 [Abrir planilha de investimentos]({link_planilha})")

# ----------------------------
# Execução
# ----------------------------
if 'logado' not in st.session_state:
    st.session_state['logado'] = False

if not st.session_state['logado']:
    login()
else:
    dashboard()
