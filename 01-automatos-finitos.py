#Pedro Henrique Rodrigues Marques dos Santos
#11611ECP017

n = None                            # número de estados n
simbolos_t = None                   # conjunto de símbolos terminais (Σ)
cj_F = None                         # conjunto de estados de aceitação (F)
n_transicoes = None                 # número t de transições (δ) do autômato
transicoes=[]                       # lista com as transicoes possiveis do automato
n_cadeias = None                    # número c de cadeias de entrada que serão avaliadas.
cadeias = []                        # lista que conterá as cadeias que serão avaliadas
aceitacao = None                    # usada para avaliação da aceitacao das cadeias
estado_inicial = 0

def init():                                     # função primaria para captura 
    global n, simbolos_t, cj_F, n_transicoes, qtd_simbolsF    # dos parâmetros iniciais do automato
    n = int(input())
    simbolos_t = input().split(' ')
    cj_F = input().split(' ')
    n_transicoes = int(input())

    
def get_transicoes():                           # capturar todas as transições de acordo com o numero de transicoes informadas.
    global transicoes
    while len(transicoes) < n_transicoes:
        aux = input()
        aux = aux.split()
        transicoes.append(aux)

def get_cadeias():                             # capturar as cadeias que serão avaliadas
    global cadeias, n_cadeias
    while len(cadeias) < n_cadeias:
        aux = list(input())
        cadeias.append(aux)

def avaliar_cadeia(w_atual, estadoAtual):      # avalia as cadeias atuais e por recursividade simbolo a simbolo com as transições dos estados
    global aceitacao                           # caso possua o simbolo atual na transição, muda-se o estado, porém continua avaliando as outras transições e estados aceitos
    if(w_atual == ['-']):                      # até chegar a um unico caminho de aceitação.
        if(estadoAtual in aceitacao):
            return True
        return False

    if(w_atual == []):
        if(estadoAtual in aceitacao):
            return True
        return False
    
    for i in range(len(transicoes)):           # irá comparar os simbolos a palavra w com todos os simbolos das transições
        tAtual = transicoes[i]
        estadoInicialT = int(tAtual[0])
        if((estadoInicialT == estadoAtual) and (tAtual[1] == w_atual[0])):   
            if(avaliar_cadeia(w_atual[1:],(int(tAtual[2])))): # chama a função novamente para avaliar os proximos simbolos e também passa o próximo estado
                return True
    return False


if __name__ == "__main__":
    init()
    get_transicoes()
    n_cadeias = int(input())                    # obter o numero c de cadeias
    get_cadeias()
    aceitacao = list(map(int, cj_F[1:]))
    
    for i in range(n_cadeias):                         # será avaliado as n cadeias inseridas
        if(avaliar_cadeia(cadeias[i],estado_inicial)): # dado o valor de retorno, imprime se a cadeia é ou não aceita.
            print("aceita")
        else:
            print("rejeita")
    
        
