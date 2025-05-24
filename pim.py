from colorama import init, Fore, Style
from datetime import datetime, timedelta
from faker import Faker
import json
import time


fake = Faker('pt_BR')  # Inicializa o Faker com o locale pt_BR


def gerar_dados_falsos(num_usuarios):
    usuarios = []
    for _ in range(num_usuarios):
        nome = fake.name()
        senha = fake.password(length=10, special_chars=False,
                              digits=True, upper_case=True, lower_case=True)
        nota = fake.random_int(min=7, max=10)
        idade = fake.random_int(min=12, max=20)

        # Gera data de entrada nos últimos 1 mês
        data_entrada = fake.date_between(start_date='-30d', end_date='today')

        # Calcula o tempo logado em dias
        tempo_logado = (datetime.today().date() -
                        data_entrada).days  # Tempo logado em dias

        usuarios.append({
            "nome": nome,
            "senha": senha,
            "nota": nota,
            "idade": idade,
            # Formata a data como string
            "data_entrada": data_entrada.strftime('%Y-%m-%d'),
            "tempo_logado": tempo_logado  # Tempo logado em dias
        })
    return usuarios


# Chamada da função
usuarios_falsos = gerar_dados_falsos(20)  # Gera 20 usuários falsos
with open("usuarios.json", "w", encoding="utf-8") as f:
    json.dump(usuarios_falsos, f, ensure_ascii=False, indent=4)

pessoa = {"nome": "Seu Nome", "idade": 30}  # Substitua pelos valores desejados

# Serializando: Python Para JSON
json_string = json.dumps(pessoa)

init()

usuarios = []
usuario_logado = None  # Inicializa a variável do usuário logado

try:
    with open("usuarios.json", "r", encoding="utf-8") as f:
        usuarios = json.load(f)
except FileNotFoundError:
    usuarios = []


# PARTE DO LOGIN E CADASTRO

def login():
    global usuario_logado
    print("-" * 30)
    nome_de_usuario = input(
        Fore.MAGENTA + "Insira seu nome de aluno: " + Style.RESET_ALL)
    senha = input(
        Fore.MAGENTA + f"Insira sua senha {nome_de_usuario}: " + Style.RESET_ALL)

    for user in usuarios:
        if user["nome"] == nome_de_usuario and user["senha"] == senha:
            usuario_logado = user
            print(Fore.YELLOW + "CARREGANDO..." + Style.RESET_ALL)
            time.sleep(2)
            print(
                Fore.GREEN + f"Login feito com sucesso {nome_de_usuario}!" + Style.RESET_ALL)
            print(f"Sua nota atual é: {user['nota']}")
            mini_cursos()
            return

    print(Fore.RED + "❌ Erro, tente novamente" + Style.RESET_ALL)


# Tentativa de carregar os dados dos usuários e notas salvos
try:
    with open("usuarios_notas.json", "r", encoding="utf-8") as f:
        usuarios = json.load(f)
except FileNotFoundError:
    usuarios = []


def cadastro():
    print("-" * 30)
    nome_de_usuario = input("Crie seu nome de usuário: ")

    for user in usuarios:
        if user["nome"] == nome_de_usuario:
            print(
                Fore.RED + "❌ Esse nome de usuário já existe. Escolha outro!" + Style.RESET_ALL)
            return

    senha = input("Crie sua senha: ")

    # Solicita a idade e garante que seja um número inteiro
    while True:
        idade_input = input("Digite sua idade: ")
        if idade_input.isdigit():
            idade = int(idade_input)
            break
        else:
            print(Fore.RED + "❌ Idade inválida. Digite apenas números." + Style.RESET_ALL)

    # Adiciona o novo usuário com idade e nota
    usuarios.append({
        "nome": nome_de_usuario,
        "senha": senha,
        "idade": idade,
        "nota": 0
    })

    # Salva os dados no arquivo JSON
    with open("usuarios.json", "w", encoding="utf-8") as f:
        json.dump(usuarios, f, ensure_ascii=False, indent=4)

    print("✅ Cadastro realizado com sucesso!")
# -----------------------------------------------------------MENU DOS CURSOS AQUIII


def mini_cursos():
    print(Fore.LIGHTCYAN_EX + "-" * 30)
    print(Fore.LIGHTMAGENTA_EX + "---- Bem vindo ao Pega o Bit 🔥 ----")
    print(Fore.LIGHTCYAN_EX + "-" * 30)
    print(Fore.LIGHTYELLOW_EX + "🧠 [1] " + Fore.LIGHTWHITE_EX +
          "Curso de pensamento lógico computacional 🧠")
    print(Fore.LIGHTBLUE_EX + "🤖 [2] " + Fore.LIGHTWHITE_EX +
          "Curso de infraestrutura computacional 🤖")
    print(Fore.LIGHTGREEN_EX + "👾 [3] " +
          Fore.LIGHTWHITE_EX + "Curso de cibersegurança 👾")
    print(Fore.LIGHTRED_EX + "📈 [4] " + Fore.LIGHTWHITE_EX + "Suas notas 📈")
    print(Fore.LIGHTBLACK_EX + "❌ [5] " + Fore.LIGHTWHITE_EX + "SAIR... ❌")
    print("-" * 30)
    opcao_de_cursos = input("Selecione as opções acima: ")
    if opcao_de_cursos == "1":
        print("voce selecionou o curso de pensamento lógico computacional 🤖")
        pensamento_logico_computacional()

    elif opcao_de_cursos == "2":
        print("voce selecionou o curso de infraestrutura computacional")
        infraestrutura_computacional()
    elif opcao_de_cursos == "3":
        print("voce selecionou o curso de cibersegurança")
        cibersegurança()
    elif opcao_de_cursos == '4':
        notas()
    elif opcao_de_cursos == "5":
        print("Saindo da plataforma...")
    else:
        print("Tente novamente")
# ---------------------------------------------------------DEF DOS CURSOS AQUI!!!!!!!!!!!!!!!


nota = 0  # Inicializando a pontuação


def notas():
    global usuario_logado

    # Verificando se há um usuário logado
    if usuario_logado is None:
        print("Nenhum usuário logado. Realize o login primeiro.")
        login()  # Pode chamar a função de login novamente se o usuário não estiver logado
        return

    print(f"Sua nota atual é: {usuario_logado['nota']} pontos")
    input("Digite [Enter] para voltar ao menu...")
    mini_cursos()
    return
    print("Usuário não encontrado!")


def pensamento_logico_computacional():
    while True:
        print("-" * 30)
        print("----🤖 Bem-vindo ao curso de pensamento lógico computacional 🤖-----")
        print("-" * 30)
        print("[1] ▪️ O que é pensamento lógico computacional?")
        print("[2] ▪️ Pilares do pensamento lógico")
        print("[3] ▪️ Competencias e habilidades")
        print("[4] ▪️ Questionário")
        print("[5] ▪️ Voltar à tela de cursos")
        opcao = input(Fore.LIGHTGREEN_EX +
                      "Escolha uma opção: " + Style.RESET_ALL)
        print("-" * 30)

        if opcao == "1":
            print(
                "O pensamento computacional pode ser definido como uma habilidade\n"
                "para resolver problemas e desafios de forma eficiente, assim como\n"
                "um computador faria.\n\n"
                "Essa resolução pode ou não envolver equipamentos tecnológicos, mas\n"
                "a sua base é a exploração de forma criativa, crítica e estratégica\n"
                "dos domínios computacionais.\n\n"
                "Usar o pensamento computacional é ver um desafio ou problema,\n"
                "refletir sobre ele, separá-lo em partes, resolver cada uma dessas\n"
                "partes da maneira mais lógica e assertiva para depois chegar a um\n"
                "resultado final.\n"
            )
            input("Digite [Enter] para voltar ao menu...")

        elif opcao == "2":
            print(
                "Decomposição:\n"
                "👉 Dividir o desafio em problemas menores para facilitar a compreensão.\n"
                "----------------------------------------------------------------------\n"
                "Abstração:\n"
                "👉 Focar no essencial e deixar o que não importa de lado.\n"
                "----------------------------------------------------------------------\n"
                "Reconhecimento de padrão:\n"
                "👉 Identificar repetições e similaridades pra ajudar na resolução.\n"
                "----------------------------------------------------------------------\n"
                "Algoritmo:\n"
                "👉 Criar uma sequência lógica de passos para resolver o problema.\n"
            )
            input("Digite [Enter] para voltar ao menu...")

        elif opcao == "3":
            print(
                "Competencias e habilidades trabalhadas no pensamento lógico computacional\n"
                " ▪️ raciocínio lógico;\n"
                " ▪️ trabalho em grupo;\n"
                " ▪️ criatividade;\n"
                " ▪️ análise de dados;\n"
                " ▪️ gestão de projetos;\n"
                " ▪️ programação;\n"
                " ▪️ codificação.\n"
            )
            input("Digite [Enter] para voltar ao menu...")

        elif opcao == "4":
            questionario_pensamento_computacional()

        elif opcao == "5":
            print("Voltando ao menu de cursos...")
            mini_cursos()
            break

        else:
            print("⚠️ Opção inválida")

# ---------------------------------------------
# FUNÇÃO DO QUESTIONÁRIO


def questionario_pensamento_computacional():
    print("[1] Começar")
    print("[2] Voltar")
    comecar_questionario = input("Insira a opção acima: ")

    if comecar_questionario == "1":
        print("-" * 30)
        print("Qual das opções representa os pilares do pensamento lógico computacional?")
        print("-" * 30)
        print("(A)  - Decomposição e Nuvem")
        print("(B)  - Algoritmo e Reconhecimento facial")
        print("(C) - Abstração e Mouse")
        print("(D)- Reconhecimento de padrão e Abstração")
        # pra aceitar d ou D gustavo do futuro
        resposta = input("Resposta: ").strip().upper()

        if resposta == 'D':
            print(Fore.GREEN + "😎✔️ Acertou" + Style.RESET_ALL)
            usuario_logado["nota"] += 1  # Atualiza a nota no usuário logado
            # Atualiza também a lista geral
            for u in usuarios:
                if u["nome"] == usuario_logado["nome"]:
                    u["nota"] = usuario_logado["nota"]
                    break
        else:
            print(Fore.RED + "❌ Errou" + Style.RESET_ALL)

        print("-" * 30)
        print("Qual das opções corresponde as competências e habilidades desenvolvidas no pensamento lógico computacional.")
        print("-" * 30)
        print("(A)  - Análise de dados e teclados.")
        print("(B)  - Gestão de projetos e software")
        print("(C)  - Programação e codificação.")
        print("(D)  - Criatividade e LGPD.")
        resposta_1 = input("Resposta: ").strip().upper()

        if resposta_1 == "C":
            print(Fore.GREEN + "😎✔️ Acertou" + Style.RESET_ALL)
            usuario_logado["nota"] += 1
            for u in usuarios:
                if u["nome"] == usuario_logado["nome"]:
                    u["nota"] = usuario_logado["nota"]
                    break
        else:
            print(Fore.RED + "❌ Errou" + Style.RESET_ALL)

        print("-" * 30)
        print("Como pode ser definido o pensamento computacional?")
        print("-" * 30)
        print("(A) - Habilidade para resolver problemas e desafios de forma eficiente")
        print('(B) - Pensamento baseado em computadores e hardware')
        print('(C) - Resolução de problemas relacionados a software')
        print('(D) - Pensamento formatado em Nuvem')
        resposta_3 = input("Resposta: ").strip().upper()

        if resposta_3 == "A":
            print(Fore.GREEN + "😎✔️ Acertou" + Style.RESET_ALL)
            usuario_logado["nota"] += 1
            for u in usuarios:
                if u["nome"] == usuario_logado["nome"]:
                    u["nota"] = usuario_logado["nota"]
                    break
        else:
            print(Fore.RED + "❌ Errou" + Style.RESET_ALL)

        print("-" * 30)
        print("O que significa reconhecimento de padrão?")
        print("(A) - Divisão do desafio em problemas menores para facilitar a compreensão")
        print("(B) - Criar uma sequência lógica de passos para resolver o problema")
        print("(C) - Identificar repetições e similaridades pra ajudar na resolução")
        print("(D) - Identificar o padrão dos softwares utilizados")
        resposta_4 = input("Resposta: ").strip().upper()

        if resposta_4 == "C":
            print(Fore.GREEN + "😎✔️ Acertou" + Style.RESET_ALL)
            usuario_logado["nota"] += 1
            for u in usuarios:
                if u["nome"] == usuario_logado["nome"]:
                    u["nota"] = usuario_logado["nota"]
                    break
        else:
            print(Fore.RED + "❌ Errou" + Style.RESET_ALL)

        # Salva as notas no arquivo JSON
        with open("usuarios_notas.json", "w", encoding="utf-8") as f:
            json.dump(usuarios, f, ensure_ascii=False, indent=4)

        print("-" * 30)
        input("Digite [Enter] para voltar ao menu...")

    elif comecar_questionario == "2":
        print("Voltando ao curso...")

    else:
        print("Tenta de novo 😅")


def infraestrutura_computacional():
    while True:
        print("-" * 30)
        print("Bem vindo ao curso de infraestrutura computacional")
        print("-" * 30)
        print("[1] - o que é infraestrutura computacional? ")
        print("[2] - Componentes da infraestrutura computacional")
        print("[3] - questionário")
        print("[4] - voltar a tela de cursos")
        opcao_do_curso_2 = input("Selecione alguma das opções acima: ")
        print("-" * 30)

        if opcao_do_curso_2 == '1':
            print("Infraestrutura de tecnologia da informação (TI) refere-se aos\n"
                  "componentes necessários para operar e gerenciar ambientes corporativos de TI.\n"
                  "A infraestrutura de TI pode ser implantada em um sistema de cloud computing ou nas próprias instalações da organização.\n"
                  "Esses componentes incluem hardware, software, rede, sistema operacional e armazenamento de dados.\n"
                  "Todos eles são usados para fornecer serviços e soluções de TI. As soluções de infraestrutura de TI estão disponíveis\n"
                  "como aplicações de software para download. Elas são executadas nos recursos de TI existentes,\n"
                  "como armazenamento definido por software, ou como soluções online oferecidas por provedores de serviços,\n"
                  "na forma de infraestrutura como serviço (IaaS).\n"
                  )
            input("Digite [Enter] para voltar ao menu...")
        elif opcao_do_curso_2 == "2":
            print("Hardware\n"
                  "Hardware inclui servidores, datacenters, computadores pessoais, roteadores, switches e outros dispositivos.\n "
                  "As instalações que abrigam, resfriam e fornecem energia aos datacenters também fazem parte da infraestrutura.\n"
                  "--------------------------------------------------------------------------------------------------------------\n"
                  'Software\n'
                  'Software refere-se às aplicações usadas pela empresa, como servidores web, sistemas de gerenciamento de conteúdo e o sistema operacional, como o Linux®. \n'
                  'O sistema operacional é responsável por gerenciar o hardware e os recursos do sistema.\n '
                  'Ele também conecta todos os recursos físicos e de software que executam tarefas.\n'
                  '---------------------------------------------------------------------------------------------------------------\n'
                  'Rede\n'
                  'Os componentes interconectados da rede possibilitam a comunicação, o gerenciamento e as operações de\n'
                  'rede entre os sistemas internos e externos. A rede é formada pela conexão à internet, ativação da rede,\n'
                  'firewalls e segurança, além de hardwares como roteadores, switches e cabos.\n'

                  )
            input("Digite [Enter] para voltar ao menu...")

        elif opcao_do_curso_2 == '3':
            questionario_infraestrutura_computacional()

        elif opcao_do_curso_2 == "4":
            print("Voltando ao menu de cursos...")
            mini_cursos()
            break

        else:
            print(" Opção inválida, tenta de novo meu consagrado!")


def questionario_infraestrutura_computacional():
    print("-" * 30)
    print("[1] Começar")
    print("[2] Voltar")
    print("-" * 30)
    começar_questionario_1 = input("Insira a opção acima: ")

    if começar_questionario_1 == '1':
        print("-" * 30)
        print('Qual das opções abaixo representam os componentes da infraestrutura de TI?')
        print("-" * 30)
        print('(A) - Hardware e Nuvem')
        print('(B) - Software e Rede')
        print('(C) - Rede e internet')
        print("(D) - Software e Hardware")
        resposta_questionario_infra_1 = input("Resposta: ").strip().upper()
        if resposta_questionario_infra_1 == 'D':
            print(Fore.GREEN + "😎✔️ Acertou" + Style.RESET_ALL)
            usuario_logado["nota"] += 1  # Atualiza a nota no usuário logado
            # Atualiza também a lista geral
            for u in usuarios:
                if u["nome"] == usuario_logado["nome"]:
                    u["nota"] = usuario_logado["nota"]
                    break
        else:
            print(Fore.RED + "❌ Errou" + Style.RESET_ALL)
        print("-" * 30)
        print('Qual das opções abaixo é a rede essencial para a comunicação dos sistemas?')
        print("-" * 30)
        print('A - Internet')
        print('B - Nuvem')
        print('C - Hardware')
        print('D - Software')
        resposta_questionario_infra_2 = input("Resposta: ").strip().upper()

        if resposta_questionario_infra_2 == 'A':
            print(Fore.GREEN + "😎✔️ Acertou" + Style.RESET_ALL)
            usuario_logado["nota"] += 1  # Atualiza a nota no usuário logado
            # Atualiza também a lista geral
            for u in usuarios:
                if u["nome"] == usuario_logado["nome"]:
                    u["nota"] = usuario_logado["nota"]
                    break
        else:
            print(Fore.RED + "❌ Errou" + Style.RESET_ALL)
        print("-" * 30)
        print("Ao que se refere a Infraestrutura da tecnologia da informação?")
        print("-" * 30)
        print("(A) - Aos componentes necessários para operar e gerenciar ambientes corporativos de TI")
        print("(B) - Aos softwares necessários para desenvolvimento dentro dos ambientes corporativos de TI")
        print("(C) - A infraestrutura da construção do ambiente de trabalho dos profissionais de TI")
        print("(D) - A instalações que abrigam, resfriam e fornecem energia aos datacenters dos ambientes de TI")

        resposta_questionario_infra_3 = input("Resposta: ").strip().upper()

        if resposta_questionario_infra_3 == 'A':
            print(Fore.GREEN + "😎✔️ Acertou" + Style.RESET_ALL)
            usuario_logado["nota"] += 1
            for u in usuarios:
                if u['nome'] == usuario_logado['nome']:
                    u["nota"] = usuario_logado['nota']
                    break
        else:
            print(Fore.RED + "❌ Errou" + Style.RESET_ALL)

        print("O que define o termo Software?")
        print("(A) - Aplicações utilizadas para gerenciar os hardwares e os recursos do sistema")
        print("(B) - Componentes interconectados de rede")
        print("(C) - Aos componentes necessários para utilização dos computadores, como teclado e mouse")
        print("(D) - A sistemas pertencentes única e exclusivamente a servidores em Nuvem")
        resposta_questionario_infra_4 = input("Resposta: ").strip().upper()

        if resposta_questionario_infra_4 == 'A':
            print(Fore.GREEN + "😎✔️ Acertou" + Style.RESET_ALL)
            usuario_logado["nota"] += 1

            for u in usuarios:
                if u['nome'] == usuario_logado['nome']:
                    u["nome"] = usuario_logado['nota']
                    break
        else:
            print(Fore.RED + "❌ Errou" + Style.RESET_ALL)

        # Salva as notas no arquivo JSON
        with open("usuarios_notas.json", "w", encoding="utf-8") as f:
            json.dump(usuarios, f, ensure_ascii=False, indent=4)

        print("-" * 30)

        input("Digite [Enter] para voltar ao menu...")

    elif começar_questionario_1 == "2":
        print("Voltando ao curso...")

    else:
        print("Tenta de novo 😅")


def cibersegurança():
    while True:
        print("-" * 30)
        print("----Bem vindo ao curso de cibersegurança----")
        print("-" * 30)
        print("[1] ▪️ O que é cibersegurança?")
        print("[2] ▪️ Tipos de cibersegurança")
        print("[3] ▪️ Ameaças comuns a cibersegurança")
        print("[4] ▪️ questionario")
        print("[5] ▪️ Voltar ao menu de cursos")
        opcao_do_curso_3 = input("Escolha uma opção: ")

        if opcao_do_curso_3 == "1":
            print("A cibersegurança refere-se a quaisquer tecnologias, práticas e políticas que atuem na prevenção de ataques cibernéticos ou na mitigação\n"
                  "do seu impacto. A cibersegurança tem como objetivo proteger sistemas de computador, aplicações\n"
                  "dispositivos, dados, ativos financeiros e pessoas contra ransomwares e outros malwares, golpes de phishing\n"
                  "roubo de dados e outras ameaças cibernéticas.\n"
                  )
            input("Digite [Enter] para voltar ao menu...")
        elif opcao_do_curso_3 == "2":
            print("Tipos de cibersegurança:\n"
                  " ▪️ Segurança de IA\n"
                  ' ▪️ Segurança da infraestrutura crítica\n'
                  ' ▪️ Segurança de rede\n'
                  ' ▪️ Segurança de endpoints\n'
                  ' ▪️ Segurança de aplicativos\n'
                  ' ▪️ Segurança na nuvem\n'
                  ' ▪️ Segurança da informação\n'
                  ' ▪️ Segurança móvel\n'
                  )
            input("Digite [Enter] para voltar ao menu...")
        elif opcao_do_curso_3 == "3":
            print('Ameaças comuns à cibersegurança:\n'

                  ' ▪️ Malware\n'
                  ' ▪️ Ransomware\n'
                  ' ▪️ Phishing\n'
                  ' ▪️ Roubo e abuso de credenciais\n'
                  ' ▪️ Ameaças internas\n'
                  ' ▪️ Ataques de IA\n'
                  ' ▪️ Cryptojacking\n'
                  ' ▪️ Distributed denial-of-service (DDoS)\n'
                  )
            input("Digite [Enter] para voltar ao menu...")
        elif opcao_do_curso_3 == "4":
            questionario_cibersegurança()

        elif opcao_do_curso_3 == "5":
            print("Voltando ao menu de cursos...")
            mini_cursos()
            break

        else:
            print(Fore.RED + "⚠️ Opção inválida" + Style.RESET_ALL)


def questionario_cibersegurança():
    print("[1] Começar")
    print("[2] Voltar")
    começar_questionario_2 = input("Insira a opção acima:")

    if começar_questionario_2 == '1':
        print("-" * 30)
        print("1 - Quais os tipos de cibersegurança\n"

              "(A) - Segurança de IA e segurança de internet\n"
              "(B) - Segurança de rede e hardware\n"
              "(C) - Segurança móvel e segurança de aplicativos.\n"
              "(D) - Segurança na nuvem e segurança da ti.\n"
              )
        resposta_ciber_1 = input("Insira a sua resposta: ").strip().upper()
        if resposta_ciber_1 == "C":
            print(Fore.GREEN + "😎✔️ Acertou" + Style.RESET_ALL)
            usuario_logado["nota"] += 1  # Atualiza a nota no usuário logado
            # Atualiza também a lista geral
            for u in usuarios:
                if u["nome"] == usuario_logado["nome"]:
                    u["nota"] = usuario_logado["nota"]
                    break
        else:
            print(Fore.RED + "❌ Errou" + Style.RESET_ALL)

        print("O que é cibersegurança?")
        print("(A) - Conjunto de jogos online que simulam invasões de computadores")
        print("(B) - Método de acelerar a conexão de internet usando antivírus")
        print("(C) - Tecnologias, práticas e políticas de prevenção a ataques cibernético")
        print("(D) - Programa de edição de vídeos com proteção contra vírus")
        resposta_ciber_2 = input("Insira sua resposta: ").strip().upper()

        if resposta_ciber_2 == "C":
            print(Fore.GREEN + "😎✔️ Acertou" + Style.RESET_ALL)
            usuario_logado["nota"] += 1  # Atualiza a nota no usuário logado

            for u in usuarios:
                if u["nome"] == usuario_logado["nome"]:
                    u["nota"] = usuario_logado["nota"]
                    break
        else:
            print(Fore.RED + "❌ Errou" + Style.RESET_ALL)

        # Salva as notas no arquivo JSON
        with open("usuarios_notas.json", "w", encoding="utf-8") as f:
            json.dump(usuarios, f, ensure_ascii=False, indent=4)

        print("-" * 30)
        input("Digite [Enter] para voltar ao menu...")

    elif começar_questionario_2 == "2":
        print("Voltando ao curso...")

    else:
        print("Tenta de novo 😅")

# ----------------------------------------------------------LOGIN E CADASTRO AQUI


def login_ou_cadastro():
    print("\n" + "-" * 30)
    print("[1] ▪️ Login")
    print("[2] ▪️ Cadastro")
    print("[3] ❌ Voltar")
    print("-" * 30)
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        login()
    elif escolha == "2":
        cadastro()
    elif escolha == "3":
        return
    else:
        print("Erro, tente novamente")


def sobre():
    while True:
        print("" + "-" * 30)
        print("Nossa plataforma ajuda na inclusão digital, com foco estudantil!")
        print("Ela foi criada por alunos da UNIP. Ela inclui 3 cursos de tecnologia")
        print(
            "O máximo de nota que o aluno pode tirar, será 10 pontos no final (BOA SORTE 😁)")
        print("[1] Voltar")
        voltar = input("⬅️  Digite o número [1] para voltar: ")
        print("-" * 30)
        if voltar == "1":
            return
        else:
            print("tente novamente")
# ----------------------------------------------------MENU INICIAL AQUI


def menu():
    while True:
        print(Fore.LIGHTCYAN_EX + "-" * 30)
        print(Fore.LIGHTMAGENTA_EX + "---- Bem vindo ao MENU do Pega o Bit 🔥 ----")
        print(Fore.LIGHTCYAN_EX + "-" * 30)
        print(Fore.LIGHTMAGENTA_EX + "[1] " +
              Fore.LIGHTWHITE_EX + "🔒 Login / Cadastro")
        print(Fore.LIGHTMAGENTA_EX +
              "[2] " + Fore.LIGHTWHITE_EX + "📜 Sobre a nossa plataforma")
        print("[3] " + Fore.LIGHTWHITE_EX + "❌ Sair")
        print("-" * 30)
        opcao = input("Digite o número que deseja acessar: ")

        if opcao == "1":
            login_ou_cadastro()
        elif opcao == "2":
            sobre()
        elif opcao == "3":
            print("\nsaindo da plataforma...")
            break
        else:
            print("-------> opção invalida, tente novamente")


menu()
