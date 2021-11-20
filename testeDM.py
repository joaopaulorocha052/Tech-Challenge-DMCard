#Le a quantidade de expressoes que o usuario desesja consultar
numExpression = input("Digite a quantidade de expressoes: ")
#verifica se o numero esta correto
while numExpression == "" or numExpression.isdigit() == False:
  numExpression = input("Digite a quantidade correta de expressoes: ")
#transforma numExpression em inteiro
numExpression = int(numExpression)
i=0
#enquanto i for menor que numExpression
while i < numExpression:
    #inicia a lista e outras variaveis
    list = []
    expressionCount = 0
    aux = 0
    close = None
    #pede a expressao que o usuario deseja verificar
    expression = input("Digite a expressao desejada: ")
    #roda toda e string da expressao e verifica os parenteses.
    #Se k for um '(', ele sera adicionado a lista.
    #Se K for um ')', o ultimo parenteses da lista sera retirado, de forma a manter a
    #quantidade de abre e fecha parenteses igual.
    #caso a lista ja esteja vazia, imprime 'incorrect'
    for k in expression:
        if k == "(":
            list.append(k)
        elif k == ")":
            if len(list) != 0:
                close = list.pop()  
            else:
                print("incorrect")
                aux = 1
                break
    #Verifica se a expressao esta correta ou nao.
    #Se estiver correta, imprime 'correct'.
    #Se estiver errada, imprime 'incorrect'.
    if aux == 0:
        if len(list) == 0:
            expressionCount = 1
        if expressionCount != 0:
            print("correct")
        else: 
            print("incorrect")
    i += 1
    
