# Comments

'''
Multi-line
'''

#Basic print
import math


print('Hello world')
print(1+3)

#Variables
vardas = 'Pijus'
amzius = 20

#Method1
print('Mano vardas' + vardas)
print('Man yra ' + str(amzius))

#Method2
print(f'Mano vardas {vardas}. Man yra {amzius}')
print(f'Man yra {amzius}') 

#Method3
print('Mano vardas', vardas)
print(f'Man yra', amzius) 

# str() | int - str
#int() | str - int

# ~Conversion
print(int(amzius) + 2)

#String multiplication
print('-'*20)

#No new line
print('Hello world. ', end='')
print('It prints on same line')

#def echo(word):
 #   print('1' + word)

#Mixing '' ""
#print(f'Mano vardas yra {vardas} ir as noriu pasakyti {echo("")}')

print('2 + 2 = ', 2 + 2)
print('2 - 2 = ', 2 - 2)
print('2 * 2 = ', 2 * 2)
print('2 / 2 = ', 2 / 2)
print('3 ^ 2 = ', math.pow(3, 2))
print('5 % 3 = ', 5 % 3)

#Functions

# TODO: remove this on final push
print('-'*20)

def hello_word():
    print('Hello world from func')
hello_word()

# Simple function with args
def hello(name):
    print(f'Hello, {name}')
hello('Pijus')

def sum(a, b):
    print(f'{a} + {b} = {a + b}')
sum(2, 3)

# TODO: remove this on final push
print('-'*20)

a = input('Pasirinkite pirma skaiciu: ')
b = input('Pasirinkite antra skaiciu: ')

def parse(input_string):
    return int(input_string)

sum(parse(a), parse(b))

#Changes changes.....