import random

class Unit:
    HP = 100
    STR = 10
    LUCK = 5
    DEF = 5
    name = ""
    def __init__(self, name):        
        self.name = name
    def status(self):
        print("HP: %d, STR = %d, LUCK = %d, DEF = %d" % (self.HP, self.STR, self.LUCK, self.DEF))
        
class Battle:
    
    def attack(unit1,unit2):
        if random.randrange(0,99) > unit2.LUCK:
            damage = unit1.STR-unit2.DEF
            unit2.HP = unit2.HP - damage
            print("%s(은)는 %s의 공격에 성공하였다! %s는 피가 %d만큼 줄었다!" % (unit1.name, unit2.name, unit2.name, damage))
            if unit2.HP < 0 :
                Battle.endGame(unit1)
        else:
            print("%s (은)는 %s의 공격에 실패하였다!" % (unit1.name,unit2.name))

        if random.randrange(0,99) > unit1.LUCK :
            damage = unit2.STR-unit1.DEF
            unit1.HP = unit1.HP - damage
            print("%s(은)는 %s의 공격에 성공하였다! %s는 피가 %d만큼 줄었다!" % (unit2.name, unit1.name, unit1.name, damage))
            if unit1.HP < 0 :
                Battle.endGame(unit2)

        else:
            print("%s (은)는 %s의 공격에 실패하였다!" % (unit2.name, unit1.name))
            
    def endGame(unit):
        print("%s의 승리!" % unit.name)
        quit()
      
            
unit1 = input("이름을 입력해주세요\n")
unit1 = Unit(unit1)
print(unit1.status())
unit2 = input("이름을 입력해주세요\n")
unit2 = Unit(unit2)
print(unit2.status())
print("싸움을 시작하시겠습니까?\m")
go = input("Y/N")
if go == 'Y':
    while (1):
        Battle.attack(unit1,unit2)
elif go == 'N':
    pass
else :
    print("Y 나 N 을 입력주세요")
