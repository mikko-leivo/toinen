class Person():
    def __init__(self, name ="SirMcEatsAlot", age = 100):
        self.name = name
        self.age = age
    def flexaa(self):
        x = 1+1
        print(f'{self.name} miettii hetken ja sanoo 1+1 on {x}')

mikko = Person("Mikko")
mervi =Person("Mervi")

mervi.flexaa()