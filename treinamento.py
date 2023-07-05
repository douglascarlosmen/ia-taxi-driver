import gymnasium as gym
import random
import numpy as np
import pickle

# Ambiente de aprendizagem
ambiente = gym.make("Taxi-v3", render_mode="ansi")

# Tabela de possíveis movimentos zerada
tabela_q = np.zeros([ambiente.observation_space.n, ambiente.action_space.n])

# Movimentos possíveis:
# 0 = sul
# 1 = norte
# 2 = leste
# 3 = oeste
# 4 = pegar o passageiro
# 5 = entregar o passageiro

# Taxa de aprendizagem
alpha = 0.1

# Fator de desconto
gamma = 0.6

# Porcentagem da chance de exploração
epsilon = 0.1

# Quantidade de vezes que o processo será executado
n_loops = 100000

for i in range(n_loops):
    # Estado inicial do agente no loop
    estado = ambiente.reset()[0]

    recompensa = 0
    finalizado = False

    while not finalizado:
        # Exploração
        if random.uniform(0, 1) < epsilon:
            # Ação randômica
            acao = ambiente.action_space.sample()

        #  Exploitation
        else:
            # Ação mais indicada
            acao = np.argmax(tabela_q[estado])

        # Realiza a ação
        proximo_estado, recompensa, finalizado, info, _ = ambiente.step(acao)

        # Armazenando valor atual para aplicar no cálculo
        q_antigo = tabela_q[estado, acao]

        # Encontrando o próximo valor máximo baseado no próximo estado
        proximo_maximo = np.max(tabela_q[proximo_estado])

        # Aplicando Formula do QLearning
        q_novo = (1 - alpha) * q_antigo + alpha * (recompensa + gamma * proximo_maximo)
        
        # Substituindo o valor na tabela q pelo novo valor encontrado
        tabela_q[estado, acao] = q_novo

        # Mudando o estado do agente
        estado = proximo_estado

# Salvar as instruções obtidas do treinamento em um arquivo .sav
pickle.dump(tabela_q, open("treinamento_taxi.sav", "wb"))

print("Treinamento concluído")
