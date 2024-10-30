import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#---------------------------------INFOS BÁSICAS----------------------------------
idade = 0
def infos_basicas():
    clear_screen()
    while True:
        global idade
        time.sleep(0.5)
        clear_screen()
        print('Descrição base\n')
        nome = input('Nome: ')
        raca = input('Raça: ')
        classe = input('Classe: ')
        while True:
            
            try:
                idade = int(input('Idade: '))
                break  # sai do loop se a conversão for bem-sucedida
            except ValueError:
                print("Por favor, insira um número válido.")
        sexo = input('Sexo: ')
        religiao = input('Religião: ')
        #------------------------------------------------------------
        clear_screen()
        print('Legal. Então esse seria seu personagem?\n')
        print(f'''Nome: {nome}   Raça: {raca}    Classe: {classe}\n
Idade: {idade}    Sexo: {sexo}    Religião: {religiao}''')
        confirmacao = input('\nDeseja alterar? s/n').lower()
        if confirmacao == 'n':
            break
            
    return dados_basicos  # Retorna o cabeçalho fora do loop 

#---------------------------------FUNÇÃO DE DISTRIBUIR PONTOS----------------------------------

def distribuição_pontos(dicionario, pontos):
    restante = pontos
    for item in dicionario:
        if restante <= 0:
            print("Distribuição incorreta. Cada item deve ter pelo menos 1 ponto.")
            return False      # Retorna False para indicar que a distribuição está incorreta
        dicionario[item] = int(input(f'{item}: '))
        restante -= dicionario[item]
        if restante < 0:
            print("Distribuição incorreta. Você distribuiu mais pontos do que o disponível.")
            return False      # Retorna False para indicar que a distribuição está incorreta
        print(f'Pontos restantes: {restante}')
    if restante > 0:
        print(f'Ainda há {restante} pontos faltando. Distribua-os novamente.')
        return False      # Retorna False para indicar que a distribuição está incorreta
    elif sum(dicionario.values()) == pontos:
      return True     # Retorna True para indicar que a distribuição está correta

#---------------------------------ATRIBUTOS----------------------------------
inteligencia = 0
def atributos():
    clear_screen()
    while True:
        global inteligencia
        time.sleep(0.5)
        clear_screen()
        pontos_atributos = 101
    
        print('Atributos\n')
        print(f'Distribua {pontos_atributos} pontos nos seguintes atributos:\n')
        
        atributos_dict = {
            'Constituição': 0,
            'Força': 0,
            'Destreza': 0,
            'Inteligência': 0,
            'Agilidade': 0,
            'Percepção': 0,
            'Força de vontade': 0,
            'Carisma': 0
        }
        
        for i in atributos_dict:
          print(f'{i}')
        
        print('\n')
        
        while not distribuição_pontos(atributos_dict, pontos_atributos):
            print("Você precisa distribuir os pontos novamente.\n")
        
        print('\nDistribuição de pontos concluída!\n')
    
        inteligencia = atributos_dict['Inteligência']
        
        #--------------------------------------------
        clear_screen()
        print('\nAtributos\n')
        for i in atributos_dict:
          print(f'{i}: {atributos_dict[i]} - {atributos_dict[i] * 4}')
        confirmacao = input('\nDeseja alterar algo? s/n').lower()
        if confirmacao == 'n':
            return atributos_dict
            break

    atributos_JSON = atributos_dict
    return atributos_JSON
#---------------------------------PERICIAS----------------------------------

def pericias(atributos_dict):
    clear_screen()
    global idade, inteligencia
    while True:
        print('Perícias\n')
        pontos_pericias = idade * 10 + (inteligencia * 5)
    
        pericias = {}
        print('Escolha suas pericias!\n')
    
        lista_pericias = [
        "Acrobacia(AGI)", "Adestramento(INT)", "Agricultura", "Alquimia", "Armas Brancas(DEX)",
        "Armas Brancas de Longo Alcance(DEX)", "Armeiro", "Armadilhas(INT)", "Arquitetura", 
        "Arqueologia", "Arremesso(DEX)", "Artes Marciais", "Artesanato", "Artíficie", 
        "Artilharia(INT)", "Astrologia", "Astronomia", "Atuação(CAR)", "Avaliação de Objetos(PER)", 
        "Barganha(CAR)", "Biologia", "Briga(DEX)", "Burocracia(INT)", "Caça(PER)", 
        "Camuflagem(PER)", "Canto(CAR)", "Concentração(WILL)", "Condução(AGI)", 
        "Contabilidade(INT)", "Conhecimentos(INT)", "Culinária(PER)", "Dança(AGI)", 
        "Desarmar", "Desenho e Pintura(DEX)", "Direito e Jurisprudência", "Disfarce(INT)", 
        "Doma", "Ecologia", "Escalada(FOR)", "Escapismo(AGI)", "Escultura(DEX)", 
        "Escudo(DEX)", "Empatia(CAR)", "Etiqueta(CAR)", "Esquiva(AGI)", "Explosivos", "Falsificação(INT)", 
        "Filosofia", "Física", "Furtar(DEX)", "Furtividade(AGI)", "Geografia", 
        "Heráldica", "Herbalismo", "História", "Idiomas", "Impressão(CAR)", 
        "Instrumentos Musicais(DEX)", "Interrogatório(INT)", "Investigação(PER)", 
        "Intimidação(WILL)", "Joalheria(DEX)", "Jogos", "Lábia(CAR)", "Liderança(CAR)", 
        "Literatura", "Manha(CAR)", "Manuseio de fechaduras(DEX)", "Meteorologia", 
        "Mineração", "Montaria(AGI)", "Navegação(INT)", "Natação(AGI)", "Ocultismo", 
        "Prestidigitação(DEX)", "Primeiros Socorros(INT)", "Primeiros Socorros Animais(INT)", 
        "Procura(PER)", "Rastreio(PER)", "Rituais", "Salto(AGI)", "Sedução(CAR)", 
        "Sobrevivência(PER)", "Subterfúgio(PER)", "Tarot", "Teologia", "Teoria da Magia", 
        "Tortura(INT)", "Venefício(INT)", "Veterinária", "Zoologia"]
    
        for i in lista_pericias:
            print(f'{i}')
        
        while True:
            escolha = input('\nPericia: ')
            print('(deixe vazio pra finalizar)')
            if escolha == '':
                break
            elif escolha in lista_pericias:
                pericias[escolha] = 0
            else:
                print('Pericia não listada. Escolha outra')
            
        clear_screen()
    
        print('São essas as perícias que escolheu.\n')
    
        for i in pericias:
            print(f'{i}')
    
        confirmacao = input('\nDeseja altera-las? s/n').lower()
        if confirmacao == 'n':
            break
            
    clear_screen()
    while True:
        print('Perícias\n')
        
        print(f'Distribua {pontos_pericias} pontos nas pericias que escolheu:\n' )
        
        for i in pericias:
          print(f'{i}')
        print('')
        
        while not distribuição_pontos(pericias, pontos_pericias):
            print("Você precisa distribuir os pontos novamente.\n")
        
        
        # Mapeamento das abreviações para os nomes dos atributos
        atributo_map = {
            'CON': 'Constituição',
            'FOR': 'Força',
            'DEX': 'Destreza',
            'INT': 'Inteligência',
            'AGI': 'Agilidade',
            'PER': 'Percepção',
            'WILL': 'Força de vontade',
            'CAR': 'Carisma'
        }
        
        # Adicionar os valores dos atributos às perícias
        for chave, valor in pericias.items():
            for abreviacao, nome_completo in atributo_map.items():
                if abreviacao in chave:
                    pericias[chave] += atributos_dict[nome_completo]
        
        print('\nDistribuição de pontos concluída!\n')
        
        #-----------------------------
        clear_screen()
        print('\nPericias\n')
        for i in pericias:
          print(f'{i}: {pericias[i]}')
    
        confirmacao = input('\nDeseja redistribuir os pontos? s/n').lower()
        if confirmacao == 'n':
            break

    pericias_JSON = pericias
    return pericias_JSON

#---------------------------APRIMORAMENTOS------------------------------

def aprimoramentos():
    clear_screen()
    aprimoramentos_negativos = {"Alergia": 1, "Alcoólatra": 1, "Arma ou Amuleto Maldito": 2, "Cleptomaníaco": 2, "Código de Honra": 1, "Compulsão": 1, "Complexo de Inferioridade": 1,
    "Coração Mole": 1, "Covarde": 1, "Curioso": 1, "Deficiente Físico": (1, 3), "Dificuldade de Fala": 1, "Distração": 1, "Família ou Mentor Desonrado": 1, "Fanático": 2, "Fanfarronice": 1,
    "Fobia": (1, 2), "Fúria": 2, "Galante": 1, "Ganância": 1, "Gula": 1, "Hábitos Detestáveis": 1, "Inimigo": 1, "Intolerância": 1, "Má Fama": (1, 3), "Mania": 1, "Mau Humor": 1, "Megalomaníaco": 1,
    "Ódio": 1, "Orgulhoso": 1, "Pacifista": (1, 3), "Perda Terrível": 1, "Restrição à Magia": (1, 3), "Sanguinário": 1, "Sono Pesado": 1, "Traumatizado": 2, "Timidez": 1, "Teimosia": 1, "Vontade Fraca": 1}
    
    aprimoramentos_pos = {}
    aprimoramentos_neg = {}
    aprimoramentos_pts = 3
    
    print(f'''Aprimoramentos\n
Você tem 3 pontos para gastar em aprimoramentos. 
Porém, se escolher aprimoramentos negativos, isso somará pontos.\n
Aprimoramentos Positivos gastam 1 ponto
Aprimoramentos Negativos restituem 1 ponto\n

Vamos começar pelos negativos\n''')
    
    for chave, valor in aprimoramentos_negativos.items():
        if isinstance(valor, tuple):
            niveis_aprim = " - ".join(map(str, range(valor[0], valor[1] + 1)))
        else:
            niveis_aprim = valor
        print(f'{chave}   -   Custo (Nível): {niveis_aprim}')
        
    while True:
        while True:
            escolha = input('Escolha seu aprimoramento negativo: (deixe vazio pra sair) ')
            if escolha == '':
                break
            
            # Verifica se o aprimoramento existe no dicionário
            if escolha in aprimoramentos_negativos:
                valor = aprimoramentos_negativos[escolha]
                
                if isinstance(valor, tuple):
                    # Mostra os níveis disponíveis
                    niveis_disponiveis = " - ".join(map(str, range(valor[0], valor[1] + 1)))
                    print(f"Qual nível deseja?")
                    print(f'({niveis_disponiveis})')
                    # Recebe a quantidade de pontos escolhida e verifica se está dentro do intervalo
                    qntd_pontos = int(input())
                    
                    if valor[0] <= qntd_pontos <= valor[1]:
                        aprimoramentos_pts += qntd_pontos
                        aprimoramentos_neg[escolha] = qntd_pontos
                        #aprimoramentos_neg.append(f"{escolha} (nível {qntd_pontos})")
                        print(f'{escolha} nível {qntd_pontos} adicionado.')
                    else:
                        print("Nível inválido. Escolha dentro do intervalo.")
                else:
                    aprimoramentos_pts += valor
                    aprimoramentos_neg[escolha] = valor
                    print(f'{escolha} adicionado.')
            else:
                print("Escolha um aprimoramento válido.")
                
        clear_screen()
        print(f"\nAprimoramentos escolhidos:")
        if not aprimoramentos_neg:
            print ('Nenhum')
        else:
            for chave, valor in aprimoramentos_neg.items():
                print(f'{chave}: +{valor} pts')
                
        confirmacao = input('\nDeseja alterar seu aprimoramentos? (s/n)')
        if confirmacao == 'n':
                break

    pericias_JSON = pericias
    return pericias_JSON

#-------------

    aprimoramentos_positivos = {"Acerto Crítico Aprimorado": (1, 3), "Acuidade com Arma": 1, "Ambidestria": 2, "Ambiente Favorável": (1, 4), "Aparência Inofensiva": 1,
        "Arma ou Amuleto Mágico": (1, 2), "Arma Preferencial": 1, "Armadura de Heróis": (1, 3), "Ataque Desarmado": (1, 4), "Ataque Furtivo": (1, 3), "Ataque Poderoso": 1,
        "Atravessar": (1, 2), "Aumentar Magia": 1, "Biblioteca": (1, 4), "Bom Senso": 1, "Caminho da Floresta": 1, "Canalizador": (2, 4), "Classe Social": (1, 3),
        "Companheiro Animal": 1, "Contatos e Aliados": (1, 4), "Coração de Guerreiro": 2, "Coragem": 2, "Corpo Fechado": 2, "Corpo Maleável": 1, "Dívida de Gratidão": (1, 3),
        "Eloquente": 1, "Empatia com Animais": 1, "Especialização em Arma": (1, 2), "Esquiva Sobrenatural": 1, "Estender Magia": 1, "Evasão": 1, "Fama": (1, 4),
        "Família ou Mentor Honrado": 1, "Familiares": 2, "Imunidade a Venenos": (2, 3), "Inimigo Favorito": 1, "Magia sem Gestos": 1, "Magia Silenciosa": 1,
        "Maximizar Magia": 2, "Memória Eidética": 1, "Montaria Especial": 2, "Movimento Rápido": 1, "Olhar da Verdade": 2, "Patrono": 2, "Poderes Mágicos": (1, 5),
        "Pontos de Fé": (1, 5), "Pontos Heróicos": (1, 4), "Potencializar Magia": 1, "Rastro Invisível": 1, "Reputação": (2, 4), "Recursos e Dinheiro": (1, 5),
        "Redução de Dano": (1, 3), "Resistência à Dor": 3, "Resistência à Magia": (1, 5), "Sábio": 1, "Saúde de Ferro": 1, "Sedutor": 1, "Senso de Direção": 1,
        "Sentidos Aguçados": 1, "Sono Leve": (1, 2), "Sortudo": (2, 3), "Talento": 1, "Temperamento Calmo": 2, "Tiro Letal": 1, "Tiro Longo": 1, "Vontade de Ferro": 2, "Voz de Comando": 4}

    clear_screen()
    print(f"Agora vamos escolher os Positivos!\n")
    
    for chave, valor in aprimoramentos_positivos.items():
        if isinstance(valor, tuple):
            niveis_aprim = " - ".join(map(str, range(valor[0], valor[1] + 1)))
        else:
            niveis_aprim = valor
        print(f'{chave}   -   Custo: {niveis_aprim}')

    while True:
        aprimoramentos_pts_inicial = aprimoramentos_pts
        aprimoramentos_pos = {}
        while True:
            print(f'Você possui {aprimoramentos_pts_inicial} pontos.')
            if aprimoramentos_pts_inicial == 0:
                break
            escolha = input('Escolha seu aprimoramento positivo: (deixe vazio pra sair) ')
            if escolha == '':
                break
            
            # Verifica se o aprimoramento existe no dicionário
            if escolha in aprimoramentos_positivos:
                valor = aprimoramentos_positivos[escolha]
                
                if isinstance(valor, tuple) and escolha != 'Canalizador':
                    # Mostra os níveis disponíveis
                    niveis_disponiveis = " - ".join(map(str, range(valor[0], valor[1] + 1)))
                    print(f"Qual nível deseja?")
                    print(f'({niveis_disponiveis})')
                    # Recebe a quantidade de pontos escolhida e verifica se está dentro do intervalo
                    qntd_pontos = int(input())
                    if aprimoramentos_pts_inicial - qntd_pontos < 0:
                        print('Você não tem pontos suficientes para esse aprimoramento!')
                        print(f'Você possui {aprimoramentos_pts_inicial} pontos somente.\n')
                        continue
                    elif valor[0] <= qntd_pontos <= valor[1]:
                        aprimoramentos_pts_inicial -= qntd_pontos
                        aprimoramentos_pos[escolha] = qntd_pontos
                        print(f'{escolha} nível {qntd_pontos} adicionado.')
                    else:
                        print("Nível inválido. Escolha dentro do intervalo.")
                        
                elif escolha == 'Canalizador':
                    print('Qual nível deseja?\n2 ou 4')
                    qntd_pontos = int(input())
                    if aprimoramentos_pts_inicial - qntd_pontos < 0:
                        print('Você não tem pontos suficientes para esse aprimoramento!')
                        print(f'Você possui {aprimoramentos_pts_inicial} pontos somente.\n')
                        continue
                    else:
                        aprimoramentos_pts_inicial -= qntd_pontos
                        aprimoramentos_pos[escolha] = qntd_pontos
                        print(f'{escolha} nível {qntd_pontos} adicionado.')
                    
                else:
                    if aprimoramentos_pts_inicial - valor < 0:
                        print('Você não tem pontos suficientes para esse aprimoramento!')
                        print(f'Você possui {aprimoramentos_pts_inicial} pontos somente.\n')
                        continue
                    else:
                        aprimoramentos_pts_inicial -= valor
                        aprimoramentos_pos[escolha] = valor
                        print(f'{escolha} adicionado.')
            else:
                print("Escolha um aprimoramento válido.")

        clear_screen()
        print(f"\nAprimoramentos escolhidos:")
        if not aprimoramentos_pos:
            print ('Nenhum')
        else:
            for chave, valor in aprimoramentos_pos.items():
                print(f'{chave}: +{valor} pts')

        confirmacao = input('\nDeseja alterar seu aprimoramentos? (s/n)').lower()
        if confirmacao == 'n':
            break

    return {
        'positivos': aprimoramentos_pos,
        'negativos': aprimoramentos_neg
    }

#------------------------FUNÇÃO DE LISTAGEM------------------------

def listagem():
    lista = []
    item = input('Digite aqui os itens: \n(deixe em branco pra não adicionar mais)\n')
    
    while item != '':
      lista.append(item)
      item = input()

    return lista

#------------------------ARMAS------------------------

def armas():
    while True:
        print('Armas e equipamentos de combate\n')
        lista_armas = listagem()
        #------------------------------
        clear_screen()
        print('Armas e equipamentos de combate\n')
        for i in lista_armas:
             print(f'{i}')
        confirmacao = input('\nDeseja alterar? s/n').lower()
        if confirmacao == 'n':
            break

    return lista_armas

#------------------------INVENTÁRIO------------------------

def inventario():
    while True:
        print('Inventario')
        inventario_usuario = listagem()
        #-------------------------
        clear_screen()
        print('Inventário\n')
        for i in inventario_usuario:
            print(f'{i}')
        confirmacao = input('\nDeseja alterar? s/n').lower()
        if confirmacao == 'n':
            break

    return inventario_usuario

#--------------------------MAGIAS--------------------------


def escolhendo_magias():
    print('Magias')
    print('\nNessa parte você vai descrever as magias que você conversou com o mestre.\nSe seu personagem não possui magia, deixe vazio')
    
    class Magia:
        def __init__(self, nome, pontos_magia, pontos_focus, caminho, descricao):
            self.nome = nome
            self.pontos_magia = pontos_magia
            self.pontos_focus = pontos_focus
            self.caminho = caminho
            self.descricao = descricao
    
        def __str__(self):
            return (f"Magia: {self.nome}\n"
                    f"Pontos de Magia: {self.pontos_magia}\n"
                    f"Pontos de FOCUS: {self.pontos_focus}\n"
                    f"Caminho: {self.caminho}\n"
                    f"Descrição: {self.descricao}\n")

        def to_dict(self):
            return {
                'nome': self.nome,
                'pontos_magia': self.pontos_magia,
                'pontos_focus': self.pontos_focus,
                'caminho': self.caminho,
                'descricao': self.descricao
            }
        
    # Lista para armazenar as magias
    lista_magias = []
    
    # Função para adicionar magias
    def adicionar_magia():
        while True:
            nome = input("Nome da magia: ")
            while True:
                try:
                    pontos_magia = int(input('Pontos de magia: '))
                    break  # sai do loop se a conversão for bem-sucedida
                except ValueError:
                    print("Por favor, insira um número válido.")
            while True:
                try:
                    pontos_focus = int(input('Pontos de FOCUS:'))
                    break  # sai do loop se a conversão for bem-sucedida
                except ValueError:
                    print("Por favor, insira um número válido.")
            caminho = input("Caminho: ")
            descricao = input("Descrição da magia: ")
            
            # Criando uma nova instância de Magia
            magia = Magia(nome, pontos_magia, pontos_focus, caminho, descricao)
            clear_screen()
            print(magia)
            
            confirmacao = input('\nDeseja alterar sua magia? s/n').lower()
            if confirmacao == 'n':
                break
            else:
                continue
        # Adicionando à lista
        lista_magias.append(magia)
    
    # Loop principal para adicionar várias magias
    tem_magia = input('\nSe seu personagem possui magia, digite "s" ').lower()
    if tem_magia == 's':
        while True:
            adicionar_magia()
            continuar = input("Deseja adicionar outra magia? (s/n): ").lower()
            if continuar.lower() != 's':
                break

    # Função para exibir todas as magias com formatação específica
    def mostrar_magias():
        if lista_magias:
            print("\nLista de magias:\n")
            for magia in lista_magias:
                print(magia.__str__())
        else:
            print("\nNenhuma magia cadastrada.")
            time.sleep(2)
    
    # Exibindo as magias cadastradas
    clear_screen()
    mostrar_magias()
    input('')
    
    return [magia.to_dict() for magia in lista_magias]
#---------------------------------MENUS----------------------------------
clear_screen()
print(f'''Bem vindo ao FICHANATOR 2000!
    
Aqui, voce vai poder fazer sua ficha de RPG Daemon
e edita-la antes de finalizar!\n''')

time.sleep(5)

def mostrar_menu():
    print('MENU\n')
    print('1 - Criar personagem')
    print('2 - Sair')


def criar_personagem():
    time.sleep(0.5)
    clear_screen()
    print('Vamos começar?\nPrimeiro a descrição básica dele.')
    input('')
    time.sleep(0.5)
    infos_basicas()#------------------
    clear_screen()
    print('Agora vamos distribuir os Atributos!')
    input('')
    time.sleep(0.5)
    atributos_dict = atributos()  # Captura o dicionário de atributos
    clear_screen()
    print('Bacana. Agora, com a Idade e Inteligência definidos, vamos distribuir as Perícias!')
    input('')
    time.sleep(0.5)
    pericias(atributos_dict)#------------------
    clear_screen()
    print('Agora vamos lapidar um pouco a história do seu personagem com Aprimoramentos!')
    input('')
    time.sleep(0.5)
    aprimoramentos()#------------------
    clear_screen()
    print('Agora vamos escolher suas armas')
    input('')
    time.sleep(0.5)
    armas()
    clear_screen()
    print('Agora seu inventário!')
    input('')
    time.sleep(0.5)
    inventario()#------------------
    clear_screen()
    print('Só falta ver as magias, se você tiver!')
    input('')
    time.sleep(0.5)
    clear_screen()
    escolhendo_magias()#------------------
    clear_screen()
    print('Pronto! Agora é só o dev colocar a função de gerar a ficha')
    input('')

def main():
    #itens = alimentos
    while True:
        time.sleep(0.5)
        clear_screen()  # Limpa o output anterior antes de mostrar o menu
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            criar_personagem()
        elif escolha == '2':
            break
        else:
            time.sleep(0.5)
            clear_screen()  # Limpa o output anterior antes de mostrar o menu
            print('Selecione uma opção válida')
            time.sleep(2)

if __name__ == "__main__":
    main()