#Pedro Henrique Rodrigues Marques dos Santos
#11611ECP017

n = None                            # número de estados n
simbolos_t = None                   # conjunto de símbolos terminais (Σ)
cj_s_pilha = None                   # conjunto de símbolos de pilha (Γ)
cj_F = None                         # conjunto de estados de aceitação (F)
n_transicoes = None                 # número t de transições (δ) do autômato
transicoes=[]                       # lista com as transicoes possiveis do automato
n_cadeias = None                    # número c de cadeias de entrada que serão avaliadas.
cadeias = []                        # lista que conterá as cadeias que serão avaliadas
aceitacao = None                    # usada para avaliação da aceitacao das cadeias
nSimbolosTerminais = None           # quantidade de simbolos terminais
SimbolosTerminais = None            # lista de transições
nS_pilha = None                     # numero de simbolos na pilha
lista_pilha = None                  # lista de simbolos da pilha
estado_inicial = 0                  # estado incial no q0



def init():                                     # função primaria para captura 
    global n, simbolos_t, cj_F, n_transicoes, cj_s_pilha    # dos parâmetros iniciais do automato
    n = int(input())
    simbolos_t = input().split(' ')
    cj_s_pilha = input().split(' ')
    cj_F = input().split(' ')
    n_transicoes = int(input())


def get_transicoes():                           # capturar todas as transições de acordo com o numero de transicoes informadas.
    global transicoes
    while len(transicoes) < n_transicoes:
        aux = input()
        aux = aux.split(' ')
        transicoes.append(aux)

def get_cadeias():                             # capturar as cadeias que serão avaliadas
    global cadeias, n_cadeias
    while len(cadeias) < n_cadeias:
        aux = list(input())
        cadeias.append(aux)

def tratar_pilha (cadeia, estado, pilha, newPilha):
    if(newPilha == ['-']):
        aux = pilha.pop()
        if(avaliar_cadeia(cadeia,estado,pilha)):
            return True
        else:
            pilha.append(aux)

    elif(newPilha != ['-']):
        empilha = newPilha[::-1]
        aux = pilha.pop()
        NovaPilha = pilha + empilha
        if(avaliar_cadeia(cadeia,estado,NovaPilha)):
            return True
        else:
            pilha.append(aux)

def avaliar_cadeia (w_atual, estadoAtual, pilha):
    global transicoes, aceitacao
           
    for i in range(len(transicoes)):
        t_atual = transicoes[i] #pega cada trnasição
        top_pilha = pilha[-1] #pega o topo da pilha 'Z'
        estado_inicial = int(t_atual[0]) #pega o estado inicial daquela transição
        simbolo = t_atual[1] # pega o simbolo que será consumido naquela transição
        topo_pilha = t_atual[2] # pega o que deve estar no topo da pilha para aceitar a transição

        if(w_atual == [] or w_atual ==['-']):
            if(w_atual in aceitacao): 
                return True
            elif ( (estado_inicial == estadoAtual) and (list(simbolo)==['-']) and topo_pilha == topo_pilha):
              newState = int(t_atual[3])
              newPilha = list(t_atual[4])

              if(tratar_pilha(w_atual, newState, pilha,newPilha)): return True
              if(newState in aceitacao): return True          

        elif(w_atual !=[]):
            if(estado_inicial == estadoAtual and topo_pilha == top_pilha):
                if(simbolo == w_atual[0]):
                    if(tratar_pilha(w_atual[1:],int(t_atual[3], pilha, list(t_atual[4])))):
                        return True
    return False



if __name__ == "__main__":
    init()
    get_transicoes()
    n_cadeias = int(input())                    # obter o numero c de cadeias
    get_cadeias()
    aceitacao = list(map(int, cj_F[1:]))
    nSimbolosTerminais = simbolos_t[0] 
    SimbolosTerminais = simbolos_t[1:]

    for i in range(n_cadeias):                         # será avaliado as n cadeias inseridas
        if(avaliar_cadeia(cadeias[i],estado_inicial,['Z'])): # dado o valor de retorno, imprime se a cadeia é ou não aceita.
            print("aceita")
        else:
            print("rejeita")

    
