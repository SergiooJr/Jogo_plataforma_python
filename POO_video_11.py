# a classe é como se fosse um molde
class Cachorros: # Uma boa prática é começar classes com letra maiúscula
    # smp que criamo uma classe devemos criar um método construtor (é ele que permite criarmos customizações
    # diferentes de objetos)
    def __init__(self, nome, cor_de_pelo, idade, tamanho): # método construtor (recebe atributos)
    # o SELF é como um indicador de que estamos usando funções dentro de uma classe, ele sempre será o 1° parâmetro/
    # atributo de um método dentro de uma classe
        self.nome = nome
        self.cor_de_pelo = cor_de_pelo
        self.idade = idade
        self.tamanho = tamanho
    def latir(self): # método latir
        print(f'{self.nome} está latindo!')
    def correr(self): # método correr
        print(f'{self.nome} está correndo!')
# DIFERENÇA ENTRE atributos (são as caracteristicas dos individuos que pertencem a uma determinada classe
# (são variáveis)) E métodos (são as ações que esses individuos executam dentro de tal classe (são funções))

cachorro_1 = Cachorros('Thor', 'Bege', 7, 'Pequeno') # instanciando um objeto
print(cachorro_1.nome)
print(cachorro_1.idade)

# alterando um atributo fora da classe
cachorro_1.idade = 3
print(f' A nova idade do {cachorro_1.nome} é {cachorro_1.idade} meses.')

cachorro_1.latir()
cachorro_1.correr()
