class Hero:
    a = 10
    hp = 100
    mp = 50
    def attack(self,m):
        m.hp = m.hp - self.a
        print("영웅이 공격했습니다 현재 몬스터 피 %d" % m.hp)

class Monster:
    attack = 10
    hp = 100
    mp = 50

hero = Hero()
monster = Monster()

inputs = input()

if inputs == 'a':
    hero.attack(monster)

