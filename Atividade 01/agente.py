import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from heapq import heappop, heappush

# Criar o grafo representando o Sistema Solar
G = nx.Graph()

# Dados dos astros e suas distâncias médias (em milhões de km)
astros = {
    'Sol': {'distancia': 0},
    'Mercurio': {'distancia': 57.91},
    'Venus': {'distancia': 108.2},
    'Terra': {'distancia': 149.6},
    'Marte': {'distancia': 227.9},
    'Jupiter': {'distancia': 778.6},
    'Saturno': {'distancia': 1433.5},
    'Urano': {'distancia': 2872.5},
    'Netuno': {'distancia': 4495.1},
    'Lua': {'distancia': 0.384},  # Distância da Lua para a Terra
    'Fobos': {'distancia': 0.006},  # Distância de Fobos para Marte
}

# Função para adicionar arestas ao grafo com base nas distâncias
def adicionar_arestas_ao_grafo():
    for astro1 in astros:
        for astro2 in astros:
            if astro1 != astro2:
                distancia = abs(astros[astro1]['distancia'] - astros[astro2]['distancia'])
                G.add_edge(astro1, astro2, weight=distancia)

    # Conectar explicitamente a Lua com a Terra e Fobos com Marte
    G.add_edge('Terra', 'Lua', weight=0.384)  # Distância entre a Terra e a Lua
    G.add_edge('Marte', 'Fobos', weight=0.006)  # Distância entre Marte e Fobos

# Função heurística (distância entre o astro atual e o destino)
def heuristica(astro, destino):
    return astros[astro]['distancia'] - astros[destino]['distancia']

# Algoritmo A* para encontrar o caminho mais curto
def algoritmo_a_star(grafo, origem, destino):
    fila = []
    custo_total = {origem: 0}
    caminho = {origem: None}

    heappush(fila, (0 + heuristica(origem, destino), origem))  # (f(n) = g(n) + h(n))

    while fila:
        _, atual = heappop(fila)

        if atual == destino:
            caminho_final = []
            while atual is not None:
                caminho_final.append(atual)
                atual = caminho[atual]
            return caminho_final[::-1], custo_total[destino]

        for vizinho in grafo[atual]:
            custo_novo = custo_total[atual] + grafo[atual][vizinho]['weight']
            if vizinho not in custo_total or custo_novo < custo_total[vizinho]:
                custo_total[vizinho] = custo_novo
                prioridade = custo_novo + heuristica(vizinho, destino)
                heappush(fila, (prioridade, vizinho))
                caminho[vizinho] = atual

    return None, float('inf')  # Se não encontrar caminho

# Adicionar astros ao grafo e arestas de interconexão (Lua e Fobos)
adicionar_arestas_ao_grafo()

# Função para solicitar ao usuário a origem, paradas e destino
def obter_origem_paradas_destino():
    while True:
        origem = input("Escolha o astro de origem (Sol, Mercurio, Venus, Terra, Marte, Jupiter, Saturno, Urano, Netuno, Lua, Fobos): ").strip()
        paradas = input("Escolha as paradas intermediárias separadas por vírgulas (ou deixe vazio para nenhuma): ").strip()
        destino = input("Escolha o astro de destino (Sol, Mercurio, Venus, Terra, Marte, Jupiter, Saturno, Urano, Netuno, Lua, Fobos): ").strip()

        paradas_lista = [p.strip() for p in paradas.split(',')] if paradas else []

        if origem in astros and destino in astros and all(p in astros for p in paradas_lista):
            return origem, paradas_lista, destino
        else:
            print("Entrada inválida. Por favor, insira astros válidos.")

# Obter origem, paradas e destino do usuário
origem, paradas, destino = obter_origem_paradas_destino()

# Encontrar o caminho mais curto incluindo paradas
caminho_completo = []
custo_total = 0

pontos = [origem] + paradas + [destino]
for i in range(len(pontos) - 1):
    subcaminho, subcusto = algoritmo_a_star(G, pontos[i], pontos[i + 1])
    if subcaminho:
        if caminho_completo:
            subcaminho = subcaminho[1:]  # Evitar duplicar o ponto inicial
        caminho_completo.extend(subcaminho)
        custo_total += subcusto
    else:
        print(f"Não foi possível encontrar um caminho entre {pontos[i]} e {pontos[i + 1]}.")
        break

# Exibir o caminho encontrado
if caminho_completo:
    print(f'Caminho encontrado: {caminho_completo}')
    print(f'Custo total do caminho: {custo_total} milhões de km')

    # Função para gerar coordenadas 2D com base nas órbitas dos planetas (distâncias não precisam ser fidedignas)
    def calcular_posicoes_2d():
        pos = {}
        pos['Sol'] = (0, 0)

        for i, astro in enumerate(astros):
            if astro != 'Sol':
                distancia = astros[astro]['distancia']
                angulo = np.radians(i * 360 / len(astros))
                x = distancia * np.cos(angulo)
                y = distancia * np.sin(angulo)
                pos[astro] = (x, y)

        # Ajustar Lua e Fobos para ficarem próximos aos seus planetas
        pos['Lua'] = (pos['Terra'][0] + 10, pos['Terra'][1])
        pos['Fobos'] = (pos['Marte'][0] + 10, pos['Marte'][1])
        return pos

    pos = calcular_posicoes_2d()

    # Criar uma única figura com dois subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))  # Dois subplots lado a lado

    # Visualização 1: Grafo completo
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, ax=ax1)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{d['weight']:.1f}" for u, v, d in G.edges(data=True)}, font_size=8, ax=ax1)
    ax1.set_title("Grafo completo do Sistema Solar")

    # Visualização 2: Caminho encontrado
    nx.draw_networkx_nodes(G, pos, nodelist=caminho_completo, node_size=700, node_color='lightgreen', ax=ax2)
    nx.draw_networkx_edges(G, pos, edgelist=[(caminho_completo[i], caminho_completo[i + 1]) for i in range(len(caminho_completo) - 1)], edge_color='red', width=2, ax=ax2)
    nx.draw_networkx_labels(G, pos, labels={n: n for n in caminho_completo}, font_size=10, ax=ax2)
    ax2.set_title("Caminho encontrado no Sistema Solar")

    # Exibir a figura
    plt.tight_layout()
    plt.show()
else:
    print("Não foi possível encontrar um caminho.")
