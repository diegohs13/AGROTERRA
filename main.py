import openai


def chat_gpt():
    openai.api_key = "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"

    messages = []
    modelo = "gpt-3.5-turbo"
    # messages.append({"role": "system", "content": system_msg})

    message = input("O que gostaria de perguntar? ")

    while input != "sair":
        messages.append({"role": "user", "content": message})

        response = openai.ChatCompletion.create(
            model=modelo,
            messages=messages)
        resposta = response["choices"][0]["message"]["content"]

        messages.append({"role": "assistant", "content": resposta})

        return resposta


print('-' * 100)
print('Olá, bem vindo á IA da fome KKKKKKKKKKKK')
print('-' * 100)

escolha = input('Deseja usar o chat gpt? [1] sim [2] não: ')

if escolha == '1':
    print(chat_gpt())
