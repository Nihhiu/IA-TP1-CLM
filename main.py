from Connect4.simulator import Connect4Simulator 
from Connect4.players.human import Connect4HumanPlayer
from Connect4.players.random import Connect4RandomBot
from Connect4.players.greedy import Connect4GreedyBot
from Connect4.players.minimax import Connect4MinimaxBot

# from LimitPoker.simulator import LimitPokerSimulator
# from LimitPoker.players.human import LimitPokerHumanPlayer
# from LimitPoker.players.random import LimitPokerRandomBot
# from LimitPoker.players.greedy import LimitPokerGreedyBot
# from LimitPoker.players.minimax import LimitPokerMinimaxBot

# from Minesweeper.simulator import MinesweeperSimulator
# from Minesweeper.players.human import MinesweeperHumanPlayer
# from Minesweeper.players.random import MinesweeperRandomBot
# from Minesweeper.players.greedy import MinesweeperGreedyBot
# from Minesweeper.players.minimax import MinesweeperMinimaxBot

from game_simulator import GameSimulator
import player

def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()

def simular_jogo(lista_jogadores, jogo):
    if jogo == '1':
        desc = "Connect 4 - " + lista_jogadores["jogador1"]["nome"] + " vs " + lista_jogadores["jogador2"]["nome"]
        iterations = 1
        
        # Definir o tipo e atribuir função do jogador
        if lista_jogadores["jogador1"]["tipo"] == "1":
            player_1 = Connect4HumanPlayer(lista_jogadores["jogador1"]["nome"])
        elif lista_jogadores["jogador1"]["tipo"] == "2":
            player_1 = Connect4RandomBot(lista_jogadores["jogador1"]["nome"])
        elif lista_jogadores["jogador1"]["tipo"] == "3":
            player_1 = Connect4GreedyBot(lista_jogadores["jogador1"]["nome"])
        elif lista_jogadores["jogador1"]["tipo"] == "4":
            player_1 = Connect4MinimaxBot(lista_jogadores["jogador1"]["nome"])
         
        if lista_jogadores["jogador2"]["tipo"] == "1":
            player_2 = Connect4HumanPlayer(lista_jogadores["jogador2"]["nome"])
        elif lista_jogadores["jogador2"]["tipo"] == "2":
            player_2 = Connect4RandomBot(lista_jogadores["jogador2"]["nome"])
        elif lista_jogadores["jogador2"]["tipo"] == "3":
            player_2 = Connect4GreedyBot(lista_jogadores["jogador2"]["nome"])
        elif lista_jogadores["jogador2"]["tipo"] == "4":
            player_2 = Connect4MinimaxBot(lista_jogadores["jogador2"]["nome"])

        # Rodar a simulação
        run_simulation(desc, Connect4Simulator(player_1,player_2), iterations)
    elif jogo == '2':
        """
        desc = "Limit Texas - " + lista_jogadores["jogador1"]["nome"] + " vs " + lista_jogadores["jogador2"]["nome"]
        iterations = 1
        
        # Definir o tipo e atribuir função do jogador
        if lista_jogadores["jogador1"]["tipo"] == "1":
            player_1 = LimitPokerHumanPlayer(lista_jogadores["jogador1"]["nome"])
        elif lista_jogadores["jogador1"]["tipo"] == "2":
            player_1 = LimitPokerRandomBot(lista_jogadores["jogador1"]["nome"])
        elif lista_jogadores["jogador1"]["tipo"] == "3":
            player_1 = LimitPokerGreedyBot(lista_jogadores["jogador1"]["nome"])
        elif lista_jogadores["jogador1"]["tipo"] == "4":
            player_1 = LimitPokerMinimaxBot(lista_jogadores["jogador1"]["nome"])
         
        if lista_jogadores["jogador2"]["tipo"] == "1":
            player_2 = LimitPokerHumanPlayer(lista_jogadores["jogador2"]["nome"])
        elif lista_jogadores["jogador2"]["tipo"] == "2":
            player_2 = LimitPokerRandomBot(lista_jogadores["jogador2"]["nome"])
        elif lista_jogadores["jogador2"]["tipo"] == "3":
            player_2 = LimitPokerGreedyBot(lista_jogadores["jogador2"]["nome"])
        elif lista_jogadores["jogador2"]["tipo"] == "4":
            player_2 = LimitPokerMinimaxBot(lista_jogadores["jogador2"]["nome"])

        # Rodar a simulação
        run_simulation(desc, LimitPokerSimulator(player_1,player_2), iterations)
        """
        pass
    elif jogo == '3':
        """
        desc = "Minesweeper - " + lista_jogadores["jogador1"]["nome"] + " vs " + lista_jogadores["jogador2"]["nome"]
        iterations = 1
        
        # Definir o tipo e atribuir função do jogador
        if lista_jogadores["jogador1"]["tipo"] == "1":
            player_1 = MinesweeperHumanPlayer(lista_jogadores["jogador1"]["nome"])
        elif lista_jogadores["jogador1"]["tipo"] == "2":
            player_1 = MinesweeperRandomBot(lista_jogadores["jogador1"]["nome"])
        elif lista_jogadores["jogador1"]["tipo"] == "3":
            player_1 = MinesweeperGreedyBot(lista_jogadores["jogador1"]["nome"])
        elif lista_jogadores["jogador1"]["tipo"] == "4":
            player_1 = MinesweeperMinimaxBot(lista_jogadores["jogador1"]["nome"])
         
        if lista_jogadores["jogador2"]["tipo"] == "1":
            player_2 = MinesweeperHumanPlayer(lista_jogadores["jogador2"]["nome"])
        elif lista_jogadores["jogador2"]["tipo"] == "2":
            player_2 = MinesweeperRandomBot(lista_jogadores["jogador2"]["nome"])
        elif lista_jogadores["jogador2"]["tipo"] == "3":
            player_2 = MinesweeperGreedyBot(lista_jogadores["jogador2"]["nome"])
        elif lista_jogadores["jogador2"]["tipo"] == "4":
            player_2 = MinesweeperMinimaxBot(lista_jogadores["jogador2"]["nome"])

        # Rodar a simulação
        run_simulation(desc, MinesweeperSimulator(player_1,player_2), iterations)
        """
        pass
    else:
        print("Ocorreu um erro: Jogo inválido.")

def main():
    print("""
          ########################
          Trabalho realizado por:
          Sérgio Gabriel - 28251
          Diogo Oliveira - 29950
          ########################
          Orientadores:
          Doutor Jorge Ribeiro
          Doutor Luís Teófilo
          ######################## 


          Qual jogo pretende jogar
          1 ------ Connect 4
          2 ------ Limit Texas
          3 ------ Minesweeper

          ________________________
          """)
    escolha = input("Opção: ")

    if escolha not in ['1', '2', '3']:
        print("Opção inválida. Escolha novamente.")
        return main()

    # Obter os jogadores
    lista_jogadores = jogadores()

    simular_jogo(lista_jogadores, escolha)

# texto para escolher o tipo de jogador (Humano, Random, Greedy, Minimax)
def modo_jogo_escolha (num: int):
    print("""
          #########################
          Jogador {}:
          #########################

          1 ------ Humano
          2 ------ Computador:Random
          3 ------ Computador:Greedy
          4 ------ Computador:Minimax
    """.format(num))

    escolha = input("Tipo de Jogador: ")

    if escolha not in ['1', '2', '3', '4']:
        print("Opção inválida. Escolha novamente.")
        return modo_jogo_text(num)

# escolher o nome do jogador
def nome_jogador_escolha (tipo: str, num: int):
    if tipo == '1':
        return input("O nome do jogador: ")
    elif tipo == '2':
        return 'Random_Bot{}'.format(num)
    elif tipo == '3':
        return 'Greedy_Bot{}'.format(num)
    elif tipo == '4':
        return 'Minimax_Bot{}'.format(num)

# definir o tipo e nome do jogador
def jogadores():
    # Jogador 1
    tipo_1 = modo_jogo_escolha(1)
    nome_1 = nome_jogador_escolha(tipo_1, 1)
    
    # Jogador 2
    tipo_2 = modo_jogo_escolha(2)
    nome_2 = nome_jogador_escolha(tipo_2, 2)
    

    lista_jogadores = {
        "jogador1": {
            "nome": nome_1,
            "tipo": tipo_1
        },
        "jogador2": {
            "nome": nome_2,
            "tipo": tipo_2
        }
    }

    return lista_jogadores