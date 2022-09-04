lista=[]

print('estamos fazendo uma lista, se sua lista tiver completa, apenas digite acabar')

print('o que deseja colocar na lista? ')
while(2>1):
    item=input()
    if (item=='acabar'):
        break #break finaliza o código totalmente
        #continue finaliza o código apenas dentro da estrutura
    else:
        lista.append(item)
        print(lista)
        print(len(lista))#len identifica quantidade
#lista.remove(item) remover

    
