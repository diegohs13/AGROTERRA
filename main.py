def chat_gpt(mensagem):
    import openai

    # Cole sua API abaixo.
    # Para obter sua API siga as instruções do README
    openai.api_key = "Cole sua API key aqui"

    messages = []
    modelo = "gpt-3.5-turbo"

    message = mensagem

    while message:
        messages.append({"role": "user", "content": message})

        response = openai.ChatCompletion.create(
            model=modelo,
            messages=messages)
        resposta = response["choices"][0]["message"]["content"]

        messages.append({"role": "assistant", "content": resposta})

        return resposta


def timer(tempo):
    import time
    import sys

    if tempo > 9:
        print(f'Em {tempo} segundos o programa será fechado!')
        print('-' * 100)
        print((' ' * 30) + 'Obrigado por usar a AgroTerra! <3')
        print('-' * 100)
        for i in range(0, tempo):
            sys.stdout.write("\r{}".format(i + 1))
            sys.stdout.flush()
            time.sleep(1)

    else:
        print(f'Em {tempo} segundos voltaremos para o menu incial...')
        for i in range(0, tempo):
            sys.stdout.write("\r{}".format(i + 1))
            sys.stdout.flush()
            time.sleep(1)
        print('')


def login():
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

    print('-' * 100)
    print('Olá, bem vindo á AgroTerra!')
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
    print('-' * 100)
    print((' ' * 30) + 'MENU INICIAL')
    print('-' * 100)
    print('[0] Sair\n'
          '[1] Cadastrar plantações\n'
          '[2] Listar plantações\n'
          '[3] Análise de safras\n'
          '[4] Identificação de pragas')
    print('-' * 100)

    while True:
        escolha_usuario = input('Por favor escolha a opção desejada: ')
        print('-' * 100)

        if escolha_usuario.isnumeric():
            if 5 > int(escolha_usuario) >= 0:
                return escolha_usuario

            else:
                print('Escolha somente as opções listadas')
                print('-' * 100)

        else:
            print('Por favor utilize números na escolha')
            print('-' * 100)


def cadastrar_plantacoes(identificacao):
    def itens_plantacao(item):
        if item == 'alimento':
            while True:
                alimento = input('Digite o alimento da plantação: ')
                if alimento.isnumeric():
                    print('Não utilize numeros na hora de cadastrar o alimento!')
                else:
                    return alimento

        elif item == 'hectares':
            while True:
                hectares = input('Digite o tamanho do terreno em hectares: ')
                if hectares.isnumeric():
                    return hectares
                else:
                    print('Por favor utilize números na hora de cadastrar os hectares: ')

        elif item == 'solo':
            while True:
                solo = input('Digite o tipo de solo: ')
                if solo.isnumeric():
                    print('Não utilize numeros na hora de cadastrar o solo!')
                else:
                    return solo

    plantacoes = {
        'alimento': itens_plantacao('alimento'),
        'hectares': itens_plantacao('hectares'),
        'solo': itens_plantacao('solo')

    }

    plantacoes_usuario[identificacao] = plantacoes
    print('-' * 100)
    print((' ' * 30) + 'Plantação cadastrada com sucesso')
    print('-' * 100)
    timer(5)


def listar_plantacoes():
    while True:
        if len(plantacoes_usuario) > 0:
            print('-' * 100)
            print(f'Olá, você tem {len(plantacoes_usuario)} plantações cadastradas!')
            print('-' * 100)
            print(plantacoes_usuario)
            print('-' * 100)
            return True

        else:
            print('-' * 100)
            print('Você ainda não possui nenhuma plantação cadastrada\nPor favor cadastre')
            print('-' * 100)
            return False


def escolha_plantacao():
    while True:
        if not listar_plantacoes():
            return False

        else:
            escolha = input('Digite o número de identificação da plantação que deseja escolher: ')

            if escolha.isnumeric():
                if int(escolha) > len(plantacoes_usuario):
                    print('Número de identicação não encontrado!')
                else:
                    print(f'A plantação escolhida foi:\n'
                          f'{plantacoes_usuario[escolha]}')
                    return escolha
            else:
                print('Utilize números na hora da escolha!')


def analise_safras():
    escolha_analise = escolha_plantacao()

    if not escolha_analise:
        print('Não é possivel fazer analise sem ter uma plantação cadastrada')
    else:
        alimento_analise = plantacoes_usuario[escolha_analise]['alimento']
        hectares_analise = plantacoes_usuario[escolha_analise]['hectares']
        solo_analise = plantacoes_usuario[escolha_analise]['solo']

        print('-' * 100)
        print((' ' * 30) + 'TIPOS DE ANÁLISE')
        print('-' * 100)
        print('[1] Sobre quais cuidados ter com a safra\n'
              '[2] Sobre como cultivar\n'
              '[3] Melhor época para plantio e colhimento\n'
              '[4] Outras')
        print('-' * 100)

        while True:
            tipo_analise = input('Qual tipo de análise deseja fazer? ')
            if tipo_analise.isnumeric():
                if tipo_analise == '1':
                    msg_analise = f'Possuo uma plantação de {alimento_analise},' \
                                  f' com um terreno {solo_analise} de {hectares_analise} hectares,' \
                                  f' quais os cuidados que devo ter com ela?'

                    print('-' * 100)
                    print('Aguarde alguns segundos...')
                    print('-' * 100)
                    print(chat_gpt(msg_analise))
                    print('-' * 100)
                    timer(5)
                    break
                elif tipo_analise == '2':
                    msg_analise = f'Possuo uma plantação de {alimento_analise},' \
                                  f' com um terreno {solo_analise} de {hectares_analise} hectares,' \
                                  f' como cultivar melhor e mantê-lo?'
                    print('-' * 100)
                    print('Aguarde alguns segundos...')
                    print('-' * 100)
                    print(chat_gpt(msg_analise))
                    print('-' * 100)
                    timer(5)
                    break
                elif tipo_analise == '3':
                    msg_analise = f'Possuo uma plantação de {alimento_analise},' \
                                  f' com um terreno {solo_analise} de {hectares_analise} hectares,' \
                                  f' qual a melhor epoca para colher e plantar?'
                    print('-' * 100)
                    print('Aguarde alguns segundos...')
                    print('-' * 100)
                    print(chat_gpt(msg_analise))
                    print('-' * 100)
                    timer(5)
                    break
                elif tipo_analise == '4':
                    msg_analise = input(f'Lembrando de especificar que seu plantio é de {alimento_analise} e '
                                        f'seu terreno é {solo_analise} de {hectares_analise} hectares, '
                                        f'explique sua dúvida: ')
                    print('-' * 100)
                    print('Aguarde alguns segundos...')
                    print('-' * 100)
                    print(chat_gpt(msg_analise))
                    print('-' * 100)
                    timer(5)
                    break

                else:
                    print('Escolha somente as opções listadas')
                    print('-' * 100)

            else:
                print('Por favor utilize números na escolha')
                print('-' * 100)


def identificao_pragas():
    escolha_pragas = escolha_plantacao()

    if not escolha_pragas:
        print('Não é possivel fazer a identificação de pragas sem ter uma plantação cadastrada')
    else:
        alimento_pragas = plantacoes_usuario[escolha_pragas]['alimento']
        hectares_pragas = plantacoes_usuario[escolha_pragas]['hectares']
        solo_pragas = plantacoes_usuario[escolha_pragas]['solo']

        msg_pragas = f'Possuo uma plantação de {alimento_pragas},' \
                     f' com um terreno {solo_pragas} de {hectares_pragas} hectares, ' \
                     f'quais são as possiveis pragas e como lidar com elas?'

        print('-' * 100)
        print('Aguarde alguns segundos...')
        print('-' * 100)
        print(chat_gpt(msg_pragas))
        print('-' * 100)
        timer(5)


plantacoes_usuario = {}


if login():
    while True:
        menu = menu_inicial()

        if menu == '0':
            print('-' * 100)
            print('Voce escolheu sair')
            print('-' * 100)
            timer(10)
            break

        elif menu == '1':
            id_plantacoes = (len(plantacoes_usuario) + 1)
            print(f'Sua plantação terá o seguinte número de identificação: [{id_plantacoes}]')
            cadastrar_plantacoes(str(id_plantacoes))

        elif menu == '2':
            listar_plantacoes()

        elif menu == '3':
            analise_safras()

        elif menu == '4':
            identificao_pragas()
else:
    print('-' * 100)
    print('Voce escolheu sair')
    print('-' * 100)
    timer(10)
