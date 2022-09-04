#modelo1
class MyClass:#classe
  x = 5#set um valor a uma variável
  a = 4

p1 = MyClass()#atribui todas as variáveis (métodos se tiver) da myclass ao código
print(p1.x)#puxa a variável "p1" que especificadamente puxa a "x"
print(p1.a)

#modelo2
def met():#método
    y = 5#set um valor de variável
    b = 4
    return y,b #retorna ambas as variáveis contidas no código

fun=met()
print(fun) #print(met()) da na mesma

#é notável a diferença das duas.
#enquanto o modelo 1 você consegue fazer uma divisão das variáveis que almeja controlar, 
#na 2 não é possível, pois retorna todas de uma vez

