import time
import os

def welcome_message():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o terminal (Windows ou Linux)
    
    mensagem = [
        "===========================================",
        "     BEM-VINDO AO QG DE MARCOS VINICIUS    ",
        "===========================================",
        "💻 Especialista em Suporte Técnico e TI",
        "🔐 Apaixonado por Segurança e Python",
        "🚀 Transformando desafios em soluções",
        "===========================================",
        "\"Disciplina, Foco e Inteligência Digital\"",
        "==========================================="
    ]

    for linha in mensagem:
        print(linha)
        time.sleep(0.3)  # Efeito de digitação lenta

welcome_message()
