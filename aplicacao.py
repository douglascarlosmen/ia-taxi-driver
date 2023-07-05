import gymnasium as gym
import numpy as np
import pickle

ambiente = gym.make("Taxi-v3", render_mode="human")
tabela_q = pickle.load(open("treinamento_taxi.sav", "rb"))

episodios = 5

for _ in range(episodios):
    estado = ambiente.reset()[0]
    penalidades, recompensa = 0, 0
    finalizado = False

    while not finalizado:
        acao = np.argmax(tabela_q[estado])
        estado, recompensa, finalizado, info, l = ambiente.step(acao)
