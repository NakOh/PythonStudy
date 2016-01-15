class Simple:

    def setName(self, name):
        self.name = name


    def sum(self, a, b):
        print(self.name)
        return a+b

    def sub(self,a1,b1):
        return a1-b1

class Cal(Simple):
    def __init__(self, name):
        self.name = name
        print(self.name)

a = Cal("Hello")
a.sum(1,2)