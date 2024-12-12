from typing import Iterable, Set, Tuple
import heapq

class Nodo:
    
    def __init__(self, estado: str, pai: 'Nodo', acao: str, custo: int):
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo

    def __eq__(self, other):
        return isinstance(other, Nodo) and self.estado == other.estado

    def __hash__(self):
        return hash(self.estado)

    def __lt__(self, other):
        # Comparar com base no custo para usar em heapq
        return self.custo < other.custo
def sucessor(estado: str) -> Set[Tuple[str, str]]:
    
    movimentos = {
        "direita": 1, "esquerda": -1, "acima": -3, "abaixo": 3
    }
    restricoes = {
        "direita": [2, 5, 8], "esquerda": [0, 3, 6],
        "acima": [0, 1, 2], "abaixo": [6, 7, 8]
    }
    posicao_vazia = estado.find("_")
    sucessores = set()

    for acao, deslocamento in movimentos.items():
        if posicao_vazia not in restricoes[acao]:
            nova_posicao = posicao_vazia + deslocamento
            novo_estado = list(estado)
            novo_estado[posicao_vazia], novo_estado[nova_posicao] = novo_estado[nova_posicao], novo_estado[posicao_vazia]
            sucessores.add((acao, "".join(novo_estado)))

    return sucessores

def expande(nodo: Nodo) -> Set[Nodo]:
    
    proximas_acoes = sucessor(nodo.estado)
    proximos_nodos = set()

    for acao, proximo_estado in proximas_acoes:
        proximo_nodo = Nodo(custo=nodo.custo + 1, acao=acao, estado=proximo_estado, pai=nodo)
        proximos_nodos.add(proximo_nodo)

    return proximos_nodos

def astar_hamming(estado: str) -> list[str]:
    objetivo = "12345678_"
    visitados = set()
    fronteira = [(0, Nodo(estado, None, None, 0))]

    while fronteira:
        _, nodo = heapq.heappop(fronteira)

        if nodo.estado == objetivo:
            caminho = []
            while nodo.pai:
                caminho.append(nodo.acao)
                nodo = nodo.pai
            return caminho[::-1]

        if nodo.estado not in visitados:
            visitados.add(nodo.estado)
            for filho in expande(nodo):
                h = sum(1 for i, c in enumerate(filho.estado) if c != "_" and c != objetivo[i])
                f = filho.custo + h
                heapq.heappush(fronteira, (f, filho))

    return None

def astar_manhattan(estado: str) -> list[str]:
    objetivo = "12345678_"
    posicoes_objetivo = {v: i for i, v in enumerate(objetivo)}
    visitados = set()
    fronteira = [(0, Nodo(estado, None, None, 0))]

    while fronteira:
        _, nodo = heapq.heappop(fronteira)

        if nodo.estado == objetivo:
            caminho = []
            while nodo.pai:
                caminho.append(nodo.acao)
                nodo = nodo.pai
            return caminho[::-1]

        if nodo.estado not in visitados:
            visitados.add(nodo.estado)
            for filho in expande(nodo):
                h = sum(
                    abs(i // 3 - posicoes_objetivo[c] // 3) + abs(i % 3 - posicoes_objetivo[c] % 3)
                    for i, c in enumerate(filho.estado) if c != "_"
                )
                f = filho.custo + h
                heapq.heappush(fronteira, (f, filho))

    return None

# Extras opcionais
def bfs(estado: str) -> list[str]:
    
    fronteira = [Nodo(estado, None, None, 0)]
    visitados = set()

    while fronteira:
        nodo = fronteira.pop(0)

        if nodo.estado == "12345678_":
            caminho = []
            while nodo.pai:
                caminho.append(nodo.acao)
                nodo = nodo.pai
            return caminho[::-1]

        if nodo.estado not in visitados:
            visitados.add(nodo.estado)
            fronteira.extend(expande(nodo))

    return None

def dfs(estado: str) -> list[str]:
    
    fronteira = [Nodo(estado, None, None, 0)]
    visitados = set()

    while fronteira:
        nodo = fronteira.pop()

        if nodo.estado == "12345678_":
            caminho = []
            while nodo.pai:
                caminho.append(nodo.acao)
                nodo = nodo.pai
            return caminho[::-1]

        if nodo.estado not in visitados:
            visitados.add(nodo.estado)
            fronteira.extend(expande(nodo))

    return None

def astar_new_heuristic(estado: str) -> list[str]:
    
    objetivo = "12345678_"
    visitados = set()
    fronteira = [(0, Nodo(estado, None, None, 0))]

    while fronteira:
        _, nodo = heapq.heappop(fronteira)

        if nodo.estado == objetivo:
            caminho = []
            while nodo.pai:
                caminho.append(nodo.acao)
                nodo = nodo.pai
            return caminho[::-1]

        if nodo.estado not in visitados:
            visitados.add(nodo.estado)
            for filho in expande(nodo):
                h = max(abs(i // 3 - objetivo.index(c) // 3) + abs(i % 3 - objetivo.index(c) % 3) for i, c in enumerate(filho.estado) if c != "_")
                f = filho.custo + h
                heapq.heappush(fronteira, (f, filho))

    return None
