#no EMACS
# C-c C-c -> roda o programa
# C-c C-p -> inicia o interpretador python
# C-c C-r -> roda o que esta selecionado

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def latir(self):
        print('auau')


cachorro = Dog('jorjao',10)

print(cachorro.age)
cachorro.latir()

print(f"teste é esse : {type(cachorro.name)}")


