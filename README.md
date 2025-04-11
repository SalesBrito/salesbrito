import time

def welcome_message():
    mensagem = """
    ===========================================
         BEM-VINDO AO QG DE MARCOS VINICIUS     
    ===========================================
    💻 Especialista em Suporte Técnico e TI
    🔐 Apaixonado por Segurança e Python
    🚀 Transformando desafios em soluções
    ===========================================
        "Disciplina, Foco e Inteligência Digital"
    ===========================================
    """
    for linha in mensagem.split("\n"):
        print(linha)
        time.sleep(0.2)  # Efeito de digitação

welcome_message()
