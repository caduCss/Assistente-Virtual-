import ollama
import json
import os

arquivo_memoria = "memoria.json"


def carregar_memoria():
    if os.path.exists(arquivo_memoria):
        try:
            with open(arquivo_memoria, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)

        except json.JSONDecodeError:
            print("Aviso: arquivo de memória vazio ou inválido.")
            return []

    return []


def salvar_memoria(historico):
    with open(arquivo_memoria, "w", encoding="utf-8") as arquivo:
        json.dump(historico, arquivo, ensure_ascii=False, indent=2)
        

print("================================")
print("         SEXTA FEIRA")
print("================================")
print("Para encerrar digite 'sair'")

historico = carregar_memoria()


while True:

    mensagem = input("você: ")

    if mensagem.lower() == "sair":
        salvar_memoria(historico)
        print("Sexta feira: Até mais!")
        break

    historico.append({
        "role": "user",
        "content": mensagem
    })

    resposta = ollama.chat(
        model="qwen3.5:9b",
        messages=historico
    )

    texto_resposta = resposta["message"]["content"]

    historico.append({
        "role": "assistant",
        "content": texto_resposta
    })

    salvar_memoria(historico)

    print("Sexta feira:", texto_resposta)
    print()
    