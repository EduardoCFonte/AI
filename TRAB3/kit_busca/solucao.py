from typing import Iterable, Set, Tuple


class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, pai:'Nodo', acao:str, custo:int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        
        self.custo = custo
        self.acao = acao
        self.estado = estado
        self.pai = pai

        def __eq__(self,no):
            return isinstance(no,Nodo) and self.estado == no.estado
            
        def __hash__(self):
            return hash(self.estado)
        
def sucessor(estado:str)->Set[Tuple[str,str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    
    set_acao_estado = set() 
    
    # dicionario de ações e valores possiveis
    acoes = {
        "direita" : 1,
        "esquerda" : -1,
        "acima" : -3,
        "abaixo" : 3
    }
    
    # dicionario com as restrições de cada ação para uma determinada posicao vazia
    restricao_movimentos = {
        "direita": [2,5,8],
        "esquerda": [0,3,6],
        "acima": [0,1,2],
        "abaixo": [6,7,8],
    }
    
    
    # encontra posicao vazia
    posicao_atual = estado.find("_")
    
    for acao, valor in acoes.items():
        if posicao_atual not in restricao_movimentos[acao]:
            proxima_posicao = posicao_atual + valor

            acao_possivel = list(estado)
            
            # troca o conteudo da posicão atual do "_" coom a posição que será atingida após o calculo da proxima posicao
            acao_possivel[posicao_atual],acao_possivel[proxima_posicao] = acao_possivel[proxima_posicao], acao_possivel[posicao_atual]
            
            tupla_acao = (acao, "".join(acao_possivel))
            
            set_acao_estado.add(tupla_acao)

    return set_acao_estado


def expande(nodo:Nodo)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    
    proximas_acoes = sucessor(nodo.estado)
    proximos_nodos = set()
    
    for acao,proximo_estado in proximas_acoes:
        proximo_nodo = Nodo(custo=nodo.custo + 1, acao = acao,estado = proximo_estado, pai = nodo)
        proximos_nodos.add(proximo_nodo)
        
    return proximos_nodos

def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def bfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def dfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def astar_new_heuristic(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

