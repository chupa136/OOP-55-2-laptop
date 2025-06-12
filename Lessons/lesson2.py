class skill:
    def __init__(self, skill_1,skill_2):
        self.skill_1 = skill_1
        self.skill_2 = skill_2

class hero:
    def __init__(self, name, lvl,hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        print(f"{self.name} action!!")

class WarriorHero(hero, skill):
    def __init__(self, name, lvl,hp, st):
        super().__init__(name,lvl,hp)
        self.st = st

    def action(self):
        print(f"WarriorHero method")

hero_1 = WarriorHero("Warrior",1,100)
hero_1.action()

#CamelCase  | Верблюжья натация
#snake_case | Змеинная натация