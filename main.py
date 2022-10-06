#no EMACS
# C-c C-c -> roda o programa
# C-c C-p -> inicia o interpretador python
# C-c C-r -> roda o que esta selecionado

#OOP - TESTE DE TIPAGEM -------------------------------------------

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def latir(self):
        print('auau')


#cachorro = Dog('jorjao',10)
#print(cachorro.age)
#cachorro.latir(sdsd)
#print(f"teste é esse : {type(cachorro.name)}")



#FUNÇÕES - DECLARAÇÕES --------------------------------------------

#def teste(a,b,v=3,z=4):
#    print(f'Valor atribuido : {a+b+v+z}')

#teste(1,2)


#tem como definir uma variavel global :
#   global d = 10    --exemplo




def g(x, *args):
    print(f'x={x}')

    for i in args:
        print(f'i={i}')


g(1,2,3,4,5,5,5,5,5,'abc')       #atribuindo parametros de tamanho variavel

def concatenate(**kwargs):
    result = '' 

    for arg in kwargs.values():
        result += arg
    
    return result

print(concatenate('teste','oi','jjsjss'))

