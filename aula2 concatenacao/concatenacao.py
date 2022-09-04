a='pizza'
b=20

print('Gostaria de {0}, mas {1} reais é caro para uma {0}!'.format(a,b))
#format importa as variáveis para o print utilizar como um vetor
#a={0} b={1}
#não é possível concatenar string com int por meio de +

price = 49
txt = "o preço é {} reais"
print()
print(txt.format(price))
#"o preço é {} reais".format(price)

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."#:.2f= x.00
print()
print(myorder.format(quantity, itemno, price))
#não necessáriamente os {} precisam de número, elas podem ser organizada apenas por ordem no format
#
print()
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))