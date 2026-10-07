import ollama

print("================================")
print("         SEXTA FEIRA")
print("================================")
print("para encerrar digite 'sair'")

historico= []

while True:

    # Recebe a mensagem do usuário
    mensagem = input("bem vindo! sou a Sexta Feira, Como posso ajudar?: ")

    # Verifica se o usuário quer encerrar
    if mensagem.lower() == "sair":
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

    texto_resposta= resposta["message"]["content"]
    
    historico.append({
            "role": "assistant", "content": texto_resposta
    })


    # Mostra a resposta da IA
    print(texto_resposta)
    print()




    
    