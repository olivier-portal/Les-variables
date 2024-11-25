print(10+ 3)
print(10 - 3)
import string
lower = list(string.ascii_lowercase)
print(lower)
print(lower[::-1])

upper = list(string.ascii_uppercase)
upper.reverse()
print('reverse list of upper', upper)

phrase = 'Je suis un String'
ma_string: string = phrase
print(ma_string)

num1 = 40
num2 = 2

add_numbers = (num1 + num2)
print(add_numbers)


num1 = 3
num2 = 14

multiply_numbers = (num1 * num2)
print(multiply_numbers)

name:string ='logiciel comptabilité'
price:float = 20.50
quantity:int = 4

print(f'Informations du produit: {'Nom :', name} {'prix :', price, '€'} {'Quantité :', quantity}')
print(f'Informations du produit ====> Nom : {name}, prix : {price}€, Quantité : {quantity}')

