import time


def chat_gpt():
    import openai

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


def validador_cpf(cpf):
    corpo_cpf = cpf[:9]
    digito_cpf = cpf[-2:]

    calculo_1 = 0
    calculo_2 = 0

    multiplicacao = [10, 9, 8, 7, 6, 5, 4, 3, 2]

    for i, j in zip(multiplicacao, corpo_cpf):
        calculo_1 += i * int(j)

    resto_1 = calculo_1 % 11

    digito_1 = 0 if resto_1 < 2 else 11 - resto_1

    corpo_cpf += str(digito_1)

    for i, j in zip(multiplicacao, corpo_cpf[1:]):
        calculo_2 += i * int(j)

    resto_2 = calculo_2 % 11

    digito_2 = 0 if resto_2 < 2 else 11 - resto_2

    return digito_cpf == f'{digito_1}{digito_2}'


def login():
    print('-' * 100)
    print('Olá, bem vindo á IA da fome KKKKKKKKKKKK')
    print('-' * 100)

    while True:
        cpf_entrada = input('Por favor digite seu CPF para fazer login ou insira "X" para sair:')
        cpf_sem_barra = cpf_entrada.replace('-', '')
        cpf_formatado = cpf_sem_barra.replace('.', '')

        if cpf_formatado.isnumeric():
            if len(cpf_formatado) == 11:
                if cpf_formatado in blocklist:
                    print('O CPF não pode conter todos números iguais!\n')
                else:
                    if not validador_cpf(cpf_formatado):
                        print('Seu CPF está invalido\n')
                    else:
                        print('-' * 100)
                        print('Login efetuado com sucesso!')
                        print('-' * 100)
                        return True
            else:
                print('O CPF deve conter 11 dígitos!\n')

        elif cpf_formatado.lower() == 'x':
            break
        else:
            print('Digite seu CPF corretamente ou apenas "x" para sair!\n')


def menu_inicial():
    print('MENU INICIAL\n'
          '[0] Sair\n'
          '[1] Cadastrar plantações\n'
          '[2] Listar plantações\n'
          '[3] Análise de safras\n'
          '[4] Identificação de pragas\n')

    while True:
        escolha_usuario = input('Por favor escolha uma das opções acima: ')

        if escolha_usuario.isnumeric():
            if 5 > int(escolha_usuario) >= 0:
                return escolha_usuario

            else:
                print('-' * 100)
                print('Escolha somente as opções listadas')
                print('-' * 100)

        else:
            print('-' * 100)
            print('Por favor utilize números na escolha')
            print('-' * 100)


def cadastrar_plantacoes(identificacao):
    plantacoes = {
        'plantio': input('Dígite o plantio desejado: '),
        'hectares': input('Digite o tamanho da sua plantação em hectares: ')
    }

    plantacoes_usuario[identificacao] = plantacoes

    print('Plantação cadastrada com sucesso')


def listar_plantacoes():
    quantidade_plantacoes = len(plantacoes_usuario)

    if quantidade_plantacoes > 0:
        print(f'Olá, você tem {quantidade_plantacoes} plantações cadastradas!\n')
        print(plantacoes_usuario)

    else:
        print('Você ainda não possui nenhuma plantação cadastrada')


def analise_safras():
    print('Análise de safras')


def identificao_pragas():
    print('Identificação de pragas')


blocklist = [
    '00000000000',
    '11111111111',
    '22222222222',
    '33333333333',
    '44444444444',
    '55555555555',
    '66666666666',
    '77777777777',
    '88888888888',
    '99999999999'
]

plantacoes_usuario = {}

if login():
    while True:
        menu = menu_inicial()

        if menu == '0':
            print('Voce escolheu sair')
            print('Em 10 segundos o programa será fechado')
            time.sleep(10)
            break

        elif menu == '1':
            id_plantacoes = (len(plantacoes_usuario) + 1)
            print(f'Sua plantação terá o seguinte número de identificação: [{id_plantacoes}]')
            cadastrar_plantacoes(id_plantacoes)

        elif menu == '2':
            listar_plantacoes()
else:
    print('Voce escolheu sair')
    print('Em 10 segundos o programa será fechado')
    time.sleep(10)
