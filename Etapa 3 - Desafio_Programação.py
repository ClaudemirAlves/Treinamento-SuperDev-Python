import sys
        
listas = [[]]
sala_amarela = []
sala_azul = []
salas = [[]]
espaço_cafe_1 = []
espaço_cafe_2 = []
espaços_cafe = [[]]
contador_sala_amarela = []
contador_sala_azul = []
x = 1
contador_sala_azul.append(x)
nome_sala_azul = "Sala Azul"
nome_espaço_cafe_2 = "Espaço 2"

def cadastra_participante(listas, sala_amarela, sala_azul, espaço_cafe_1, espaço_cafe_2, contador_sala_azul, contador_sala_amarela):
    novo = []
    tamanho_azul = len(contador_sala_azul)
    tamanho_amarela = len(contador_sala_amarela)
    print('''
    Para cadastrar um novo participante, por favor, insira o(s) nome(s) e o(s) sobrenome(s) do participante:
    ''')
    nome_pessoa = ("")
    sobrenome_pessoa = ("")
    if nome_pessoa == (""):
        nome_pessoa = input('''    Nome(s) do participante: ''')
        while nome_pessoa == (""):
            print('''
            Este campo não pode ficar sem ser preenchido. Por favor, digite o(s) nome(s) do participante.''')
            nome_pessoa = input('''    Nome(s) do participante: ''')
    if sobrenome_pessoa == (""):
        sobrenome_pessoa = input('''    Sobrenome(s): ''')
        while sobrenome_pessoa == (""):
            print('''
            Este campo não pode ficar sem ser preenchido. Por favor, digite o(s) sobrenome(s) do participante.
            ''')
            sobrenome_pessoa = input('''    Sobrenome(s): ''')
    novo.append(nome_pessoa)
    novo.append(sobrenome_pessoa)
    listas.append(novo)
    if tamanho_azul > tamanho_amarela:
        contador_sala_amarela.append(x)
        contador_sala_amarela.append(x)
        sala_amarela.append(novo)
        espaço_cafe_1.append(novo)
        print(f'''    {nome_pessoa} {sobrenome_pessoa} foi cadastrado(a) com sucesso no Treinamento SuperDevPython!''')
        print('''    Ele(a) estará na %s e no %s na primeira etapa do evento.'''%(sala_amarela[0], espaço_cafe_1[0]))
    else:
        contador_sala_azul.append(x)
        contador_sala_azul.append(x)
        sala_azul.append(novo)
        espaço_cafe_2.append(novo)
        print(f'''    {nome_pessoa} {sobrenome_pessoa} foi cadastrado(a) com sucesso no Treinamento SuperDevPython!''')
        print('''    Ele(a) estará na %s e no %s na primeira etapa do evento.'''%(sala_azul[0], espaço_cafe_2[0]))
    print('''
    Você será redirecionado para a janela inicial do gerenciador.
    ''')
    Retorno = funçoes_adm()

def cadastrar_sala(sala_amarela, sala_azul, salas):
    nova_amarela = []
    nova_azul = []
    print('''
    Para elevarmos ao máximo a experiência de nossos alunos do treinamento,
    vamos definir nomes e lotações para as salas do evento.
    ''')
    nome_sala_amarela = ("")
    nome_sala_azul = ("")
    lotaçao_max_sala_amarela = 0
    lotaçao_max_sala_azul = 0
    if nome_sala_amarela == (""):
        nome_sala_amarela = input('''    Digite um nome para a sala amarela: ''')
        while nome_sala_amarela == (""):
            print('''
            Este campo não pode ficar sem ser preenchido. Por favor, digite um nome para a sala amarela.
            ''')
            nome_sala_amarela = input('''    Nome da sala amarela: ''')
    if lotaçao_max_sala_amarela == 0:
        lotaçao_max_sala_amarela = int(input('''    Digite a lotação máxima da sala amarela: '''))
        while lotaçao_max_sala_amarela < 1:
            print('''
            A lotação da sala não pode ser 0. Por favor, insira um valor maior.
            ''')
            lotaçao_max_sala_amarela = int(input('''    Lotação máxima da sala amarela: '''))
    if nome_sala_azul == (""):
        nome_sala_azul = input('''    Digite um nome para a sala azul: ''')
        while nome_sala_azul == (""):
            print('''
            Este campo não pode ficar sem ser preenchido. Por favor, digite um nome para a sala azul.
            ''')
            nome_sala_azul = input('''    Nome da sala azul: ''')
    if lotaçao_max_sala_azul == 0:
        lotaçao_max_sala_azul = int(input('''    Digite a lotação máxima da sala azul: '''))
        while lotaçao_max_sala_azul < 1:
            print('''
            A lotação da sala não pode ser 0. Por favor, insira um valor maior.
            ''')
            lotaçao_max_sala_azul = int(input('''    Lotação máxima da sala azul: '''))
    nova_amarela.append(nome_sala_amarela)
    nova_amarela.append(lotaçao_max_sala_amarela)
    nova_azul.append(nome_sala_azul)
    nova_azul.append(lotaçao_max_sala_azul)
    sala_amarela.append(nova_amarela)
    sala_azul.append(nova_azul)
    salas.append(sala_amarela)
    salas.append(sala_azul)
    print('''
    Salas cadastradas com sucesso!
    Você será redirecionado para a janela inicial de administrador do sistema.
    ''')
    Retorno_Adm = funçoes_adm()

def cadastrar_espaço_cafe(espaço_cafe_1, espaço_cafe_2, espaços_cafe):
    print('''
    Para elevarmos ao máximo a experiência de nossos alunos do treinamento, 
    vamos definir nomes e lotações aos espaços de café do evento.
    ''')
    novo_cafe_1 = []
    novo_cafe_2 = []
    nome_espaço_cafe_1 = ("")
    nome_espaço_cafe_2 = ("")
    lotaçao_max_espaço_cafe_1 = 0
    lotaçao_max_espaço_cafe_2 = 0
    if nome_espaço_cafe_1 == (""):
        nome_espaço_cafe_1 = input('''    Digite um nome para o espaço café 1: ''')
        while nome_espaço_cafe_1 == (""):
            print('''
            Este campo não pode ficar sem ser preenchido. Por favor, digite um nome para o espaço café 1.
            ''')
            nome_espaço_cafe_1 = input('''    Nome do espaço café 1: ''')
    if lotaçao_max_espaço_cafe_1 == 0:
        lotaçao_max_espaço_cafe_1 = int(input('''    Digite a lotação máxima do espaço café 1: '''))
        while lotaçao_max_espaço_cafe_1 < 1:
            print('''
            A lotação do espaço café não pode ser 0. Por favor, insira um valor maior.
            ''')
            lotaçao_max_espaço_cafe_1 = int(input('''    Lotação máxima do espaço café 1: '''))
    if nome_espaço_cafe_2 == (""):
        nome_espaço_cafe_2 = input('''    Digite um nome para o espaço café 2: ''')
        while nome_espaço_cafe_2 == (""):
            print('''
            Este campo não pode ficar sem ser preenchido. Por favor, digite um nome para o espaço café 2.
            ''')
            nome_espaço_cafe_2 = input('''    Nome do espaço café 2: ''')
    if lotaçao_max_espaço_cafe_2 == 0:
        lotaçao_max_espaço_cafe_2 = int(input('''    Digite a lotação máxima do espaço café 2: '''))
        while lotaçao_max_espaço_cafe_2 < 1:
            print('''
            A lotação do espaço café não pode ser 0. Por favor, insira um valor maior.
            ''')
            lotaçao_max_espaço_cafe_2 = int(input('''    Lotação máxima do espaço café 2: '''))
    novo_cafe_1.append(nome_espaço_cafe_1)
    novo_cafe_1.append(lotaçao_max_espaço_cafe_1)
    novo_cafe_2.append(nome_espaço_cafe_2)
    novo_cafe_2.append(lotaçao_max_espaço_cafe_2)
    espaço_cafe_1.append(novo_cafe_1)
    espaço_cafe_2.append(novo_cafe_2)
    espaços_cafe.append(espaço_cafe_1)
    espaços_cafe.append(espaço_cafe_2)
    print('''
    Espaços de Café cadastrados com sucesso!
    Você será redirecionado para a janela inicial de administrador do sistema.
    ''')
    Retorno_Adm = funçoes_adm()

def consulta_lista(listas, sala_amarela, sala_azul):
    nome_participante = input('''    Digite o(s) nome(s) ou o(s) sobrenome(s) do participante para consultar: ''')
    for mostrar in listas:
        if nome_participante in mostrar:
            try:
                nome_participante = mostrar
                if nome_participante in sala_amarela:
                    print(f'''
                    Participante encontrado na %s e no %s!!! Seu(s) nome(s) é(são): %s, e sobrenome(s): %s
                    '''%(sala_amarela[0], espaço_cafe_1[0], mostrar[0], mostrar[1]))
                    print('''
                    Digite 1 para fazer outra consulta ou 2 para voltar à janela incial de administrador do sistema.
                    ''')
                    opçao_consulta_A = int(input('''    1 ou 2?: '''))
                    if opçao_consulta_A == 1:
                        nova_consulta = consulta_lista(listas, sala_amarela, sala_azul)
                    elif opçao_consulta_A == 2:
                        Retorno = funçoes_adm()
                    else:
                        print('''
                        Opçao inválida. Você será redirecionado para a janela incial de administrador do sistema.
                        ''')
                        Reinicio_Sistema = funçoes_adm() 
                elif nome_participante in sala_azul:
                    print(f'''
                    Participante encontrado na %s e no %s!!! Seu(s) nome(s) é(são): %s, e sobrenome(s): %s
                    '''%(sala_azul[0], espaço_cafe_2[0], mostrar[0], mostrar[1]))
                    print('''
                    Digite 1 para fazer outra consulta ou 2 para voltar à janela incial de administrador do sistema.
                    ''')
                    opçao_consulta_A = int(input('''    1 ou 2?: '''))
                    if opçao_consulta_A == 1:
                        nova_consulta = consulta_lista(listas, sala_amarela, sala_azul)
                    elif opçao_consulta_A == 2:
                        Retorno = funçoes_adm()
                    else:
                        print('''
                        Opçao inválida. Você será redirecionado para a janela incial de administrador do sistema.
                        ''')
                        Reinicio_Sistema = funçoes_adm()  
            except nome_participante not in mostrar:
               print()
            else:
                print('''
                Participante não encontrado.
                ''')
                print('''
                Digite 1 para refazer a consulta ou 2 para voltar a janela inicial de administrador do sistema.
                ''')
                opçao_consulta = int(input('''    1 ou 2?: '''))
                if opçao_consulta == 1:
                    consulta_Lista = consulta_lista(listas, sala_amarela, sala_azul)
                elif opçao_consulta == 2:
                    Retorno_Consulta = funçoes_adm()
                else:
                    print('''
                    Opçao inválida. Você será redirecionado para a janela incial de administrador do sistema.
                ''')
                    Reinicio_Sistema = funçoes_adm()
            finally:
                print() 

def consulta_salas(salas, contador_sala_azul, nome_sala_azul, sala_azul):
    nome_sala = input('''    Digite o nome da sala para consultar: ''')
    for apresentar in salas:
        for apresentar2 in apresentar:
            if nome_sala in apresentar2:
                try:
                    print('''
                    Sala encontrada!!! Nome, lotação e participantes, respectivamente: %s
                    '''%(apresentar))
                    print('''
                    Você será redirecionado para a janela incial de administrador do sistema.
                    ''')
                    Reinicio_Sistema = funçoes_adm()  
                except contador_sala_azul not in apresentar2:
                    print()
                else:
                    print()
                finally:
                    print()
            elif nome_sala == nome_sala_azul:
                print('''
                Sala encontrada!!! Nome, lotação e participantes, respectivamente: %s
                '''%(sala_azul))
                print('''
                Você será redirecionado para a janela incial de administrador do sistema.
                ''')
                Reinicio_Sistema = funçoes_adm()  
            else:
                print('''
                Sala não encontrada.
                ''')
                print('''
                Você será redirecionado para a janela incial de administrador do sistema.
                ''')
                Reinicio_Sistema = funçoes_adm()

def consulta_espaço_cafe(espaços_cafe, contador_sala_azul, nome_espaço_cafe_2, espaço_cafe_2):
    nome_espaço_cafe = input('''    Digite o nome do espaço café para consultar: ''')
    for aparecer in espaços_cafe:
        for aparecer2 in aparecer:
            if nome_espaço_cafe in aparecer2:
                try:
                    print('''
                    Espaço Café encontrado!!! Nome, lotação e participantes, respectivamente: %s
                    '''%(aparecer))
                    print('''
                    Você será redirecionado para a janela incial de administrador do sistema.
                    ''')
                    Reinicio_Sistema = funçoes_adm()  
                except contador_sala_azul not in aparecer2:
                    print()
                else:
                    print()
                finally:
                    print()
            elif nome_espaço_cafe == nome_espaço_cafe_2:
                print('''
                Espaço Café encontrado!!! Nome, lotação e participantes, respectivamente: %s
                '''%(espaço_cafe_2))
                print('''
                Você será redirecionado para a janela incial de administrador do sistema.
                ''')
                Reinicio_Sistema = funçoes_adm() 
            else:
                print('''
                Espaço Café não encontrado.
                ''')
                print('''
                Você será redirecionado para a janela incial de administrador do sistema.
                ''')
                Reinicio_Sistema = funçoes_adm() 

def funçoes_adm():
    opçao_adm = 0
    print('''
    O que você deseja fazer? Digite:

    1 para cadastrar um novo participante. IMPORTANTE: você precisa cadastrar as salas e espaços cafés primeiro;
    2 para cadastrar uma sala para o treinamento;
    3 para cadastrar um espaço café para o evento;
    4 para consultar um participante;
    5 para consultar as salas e suas lotações;
    6 para consultar os espaços cafés e suas lotações;
    ou 7 para sair do gerenciador.
    ''')
    opçao_adm = int(input('''    1, 2, 3, 4, 5, 6 ou 7?: '''))
    if opçao_adm == 1:
        cadastro_participante = cadastra_participante(listas, sala_amarela, sala_azul, espaço_cafe_1, espaço_cafe_2, contador_sala_azul, contador_sala_amarela)
    if opçao_adm == 2:
        cadastro_salas = cadastrar_sala(sala_amarela, sala_azul, salas)
    if opçao_adm == 3:
        cadastro_espaços_cafes = cadastrar_espaço_cafe(espaço_cafe_1, espaço_cafe_2, espaços_cafe)
    if opçao_adm == 4:
        consulta_Lista = consulta_lista(listas, sala_amarela, sala_azul)
    if opçao_adm == 5:
        consulta_Sala = consulta_salas(salas, contador_sala_azul, nome_sala_azul, sala_azul)
    if opçao_adm == 6:
        consulta_Cafe = consulta_espaço_cafe(espaços_cafe, contador_sala_azul, nome_espaço_cafe_2, espaço_cafe_2)
    if opçao_adm == 7:
        print('''
        O gerenciador será encerrado.
        ''')
        sys.exit()
    else:
        print('''
        Opção inválida!
        ''')
        retornando = funçoes_adm()

def programa():
    print('''
    Bem vindo ao sistema de gerenciamento do Treinamento SuperDevPython!
    Escolha uma das seguintes opções:
    ''')
    Funçoes_Adm = funçoes_adm()

inicializador = programa()