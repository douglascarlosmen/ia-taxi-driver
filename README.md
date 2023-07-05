# IA Taxi Driver 🚖🤖

Inteligência Artificial desenvolvida em Python, com o objetivo de aprender a sequência correta de movimentos que um carro (taxi) deve fazer, a fim de buscar o "passageiro" em um ponto A e deixá-lo em um ponto B.

O cenário é reiniciado sempre que a IA atingir o objetivo, fazendo com que a localização dos pontos A e B sejam diferentes a cada episódio.

## Versão do Python 🐍
- [3.11](https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe)

## Módulos utilizados ❗
- [gymnasium](https://gymnasium.farama.org/)
- [numpy](https://numpy.org/)
- [pickle](https://docs.python.org/3/library/pickle.html)
- [random](https://docs.python.org/3/library/random.html)

## Como usar 💻

Após ter instalado os módulos necessários você poderá executar o arquivo `treinamento.py` para que o script de treinamento da IA seja executado.

`py treinamento.py`

Por padrão, a execução do treinamento não mostrará nada visual além da mensagem `"Treinamento concluído"` ao final da execução, porém você pode alterar o valor do argumento `"render_mode"` presente na linha `7` para `humans`.

Dessa forma será aberta uma janela onde você poderá acompanhar o treinamento de forma visual.

![Feedback visual do treinamento](https://gymnasium.farama.org/_images/taxi.gif)

Ainda no arquivo `treinamento.py`, você encontrará a variável `n_loops` que está com o valor de `100000` por padrão.

Este número representa a quantidade de episódios que serão executados no treinamento da IA.

No final da execução do treinamento você terá um novo arquivo no diretório do projeto, chamado `treinamento_taxi.sav`.

Este arquivo contém todas as regras de movimentações corretas que a IA aprendeu durante o treinamento.

Agora você pode executar o arquivo `aplicacao.py` e ter um feedback visual da IA atingindo o objetivo sem errar.

Por padrão, o ciclo irá se repetir por `5` vezes, mas você pode aumentar esse número alterando o valor da variável `episodios` encontrada na linha `8`

## Grupo de Estudos 📚

Está estudando Machine Learning e Inteligência Artificial?

Vamos estudar juntos!

Entre em contato comigo pelo e-mail contatodouglasmen@gmail.com

Este e-mail também é o meu PIX, caso você queira deixar uma contribuiçãozinha 🙂