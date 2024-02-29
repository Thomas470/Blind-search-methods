from queue import Queue

# Define a posição do espaço vazio. Pode ser qualquer valor que não esteja no intervalo [1, 8]
Vazio = None

# Define o estado objetivo
Estado_Objetivo = [1, 2, 3, 4, 5, Vazio, 6, 7, 8]

# Gera os sucessores do estado atual
def gera_sucessores(estado):
    # Cria uma lista vazia para armazenar os sucessores
    sucessores = []
    # Encontra o índice do espaço vazio
    Indice_Vazio = estado.index(Vazio)
    # Move para cima
    if Indice_Vazio > 2:
        # Cria uma cópia do estado atual
        novo_estado = estado[:]
        # Troca o espaço vazio com a peça acima
        novo_estado[Indice_Vazio], novo_estado[Indice_Vazio - 3] = novo_estado[Indice_Vazio - 3], novo_estado[Indice_Vazio]
        # Adiciona o novo estado na lista de sucessores
        sucessores.append(novo_estado)
    # Move para baixo
    if Indice_Vazio < 6:
        # Cria uma cópia do estado atual
        novo_estado = estado[:]
        # Troca o espaço vazio com a peça abaixo
        novo_estado[Indice_Vazio], novo_estado[Indice_Vazio + 3] = novo_estado[Indice_Vazio + 3], novo_estado[Indice_Vazio]
        # Adiciona o novo estado na lista de sucessores
        sucessores.append(novo_estado)
        # Move para esquerda
    # Move para esquerda
    if Indice_Vazio % 3 != 0:
        # Cria uma cópia do estado atual
        novo_estado = estado[:]
        # Troca o espaço vazio com a peça à esquerda
        novo_estado[Indice_Vazio], novo_estado[Indice_Vazio - 1] = novo_estado[Indice_Vazio - 1], novo_estado[Indice_Vazio]
        # Adiciona o novo estado na lista de sucessores
        sucessores.append(novo_estado)
        # Move para direita
    # Move para direita
    if (Indice_Vazio + 1) % 3 != 0:
        # Cria uma cópia do estado atual
        novo_estado = estado[:]
        # Troca o espaço vazio com a peça à direita
        novo_estado[Indice_Vazio], novo_estado[Indice_Vazio + 1] = novo_estado[Indice_Vazio + 1], novo_estado[Indice_Vazio]
        # Adiciona o novo estado na lista de sucessores
        sucessores.append(novo_estado)
    # Retorna a lista de sucessores
    return sucessores
    # Retorna a lista de sucessores


# Algoritmo de busca em largura
def bfs(estado_inicial):
    visitados = set()
    queue = Queue()
    queue.put((estado_inicial, []))
    while not queue.empty():
        # Desenfileira o estado
        estado, caminho = queue.get()
        if estado == Estado_Objetivo:
            # Retorna o caminho até o estado objetivo
            return caminho
        if tuple(estado) not in visitados:
            # Marca o estado como visitado
            visitados.add(tuple(estado))
            for sucessor in gera_sucessores(estado):
                if tuple(sucessor) not in visitados:
                    queue.put((sucessor, caminho + [sucessor]))
    return None


# Algoritmo de busca em profundidade
def dfs(estado_inicial, limite_de_profundidade=50):
    visitados = set()
    pilha = [(estado_inicial, [])]
    while pilha:
        # Desempilha o estado
        estado, caminho = pilha.pop()
        if estado == Estado_Objetivo:
            return caminho
        if tuple(estado) not in visitados and len(caminho) < limite_de_profundidade:
            # Marca o estado como visitado
            visitados.add(tuple(estado))
            for sucessor in gera_sucessores(estado):
                # Adiciona o estado na pilha
                if tuple(sucessor) not in visitados:
                    pilha.append((sucessor, caminho + [sucessor]))
    return None

# Algoritmo de busca iterativa em profundidade
def ids(estado_inicial):
    limite_de_profundidade = 0
    while True:
        # Executa o algoritmo de busca em profundidade
        resultado = dfs(estado_inicial, limite_de_profundidade)
        if resultado is not None:
            return resultado
        limite_de_profundidade += 1

# Solicita o estado inicial do usuário
estado_inicial = []
print("Digite o estado inicial do quebra-cabeça, linha por linha, utilizando o número 1-8 para as peças e o caractere '-' para o espaço vazio.")
# Lê o estado inicial do usuário
for i in range(3):
    linha = input(f"Linha {i + 1}: ").strip().split()
    estado_inicial.extend(linha)

# Converte as strings em inteiros ou None
estado_inicial = [int(x) if x != '-' else None for x in estado_inicial]

# Executa o algoritmo BFS/DFS/IDS
caminho = ids(estado_inicial)
if caminho is None:
    # Não foi encontrada uma solução
    print("Não foi encontrada uma solução.")
else:
    # Imprime o estado inicial e o caminho até o estado objetivo
    print("Estado inicial:")
    for i in range(0, 9, 3):
        print(estado_inicial[i:i+3])
    print("Caminho até o estado objetivo:")
    for estado in caminho:
        # Imprime o estado
        for i in range(0, 9, 3):
            print(estado[i:i+3])
        print()
