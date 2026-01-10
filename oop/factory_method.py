from abc import ABC, abstractmethod


# Product
class Skill(ABC):
    def __init__(self, skill_title: str, mana_cost: int):
        self.skill_title = skill_title
        self.mana_cost = mana_cost

    def __str__(self) -> str:
        super().__str__()
        return self.description()

    @abstractmethod
    def cast(self, attacker, target):
        pass

    def description(self):
        return f'Skill: {self.skill_title}. Mana cost: {self.mana_cost}'

# Concrete products
class PowerStrike(Skill):
    def __init__(self):
        super().__init__(skill_title='Power Strike', mana_cost=5)

    def cast(self, attacker, target):
        damage = attacker.attack * 2
        target.hp -= damage
        print(f"{attacker.name} strikes {target.name} for {damage} dmg!")

class Fireball(Skill):
    def __init__(self):
        super().__init__(skill_title='Fireball', mana_cost=15)

    def cast(self, attacker, target):
        damage = attacker.intelligence * 3
        target.hp -= damage
        print(f"{attacker.name} casts {target.name} for {damage} dmg!")

class MultiStrike(Skill):
    def __init__(self):
        super().__init__(skill_title='Multi Strike', mana_cost=10)

    def cast(self, attacker, target):
        damage = attacker.attack * 1
        target.hp -= damage
        print(f"{attacker.name} strikes {target.name} for {damage} dmg!")

# Creator
class SkillFactory(ABC):
    @abstractmethod
    def create_skill(self) -> Skill:
        pass

    def add_skill(self) -> str:
        skill = self.create_skill()
        return f'{skill} was added.'

# Concrete Creators
class WarriorSkillFactory(SkillFactory):
    def create_skill(self) -> Skill:
        return PowerStrike()

class WizardSkillFactory(SkillFactory):
    def create_skill(self) -> Skill:
        return Fireball()

class ArcherSkillFactory(SkillFactory):
    def create_skill(self) -> Skill:
        return MultiStrike()

warrior_skill_factory = WarriorSkillFactory()
wizard_skill_factory = WizardSkillFactory()
archer_skill_factory = ArcherSkillFactory()

warrior_skill = warrior_skill_factory.create_skill()
wizard_skill = wizard_skill_factory.create_skill()
archer_skill = archer_skill_factory.create_skill()
print(warrior_skill.description())
print(wizard_skill.description())
print(archer_skill.description())

class DummyHero:
    def __init__(self, name, attack=10, intelligence=5, hp=100):
        self.name = name
        self.attack = attack
        self.intelligence = intelligence
        self.hp = hp

    def is_dead(self) -> bool:
        if self.hp <= 0:
            print(f'{self.name} hero is dead')
        return self.hp <= 0

warrior = DummyHero('Conan', attack=15)
wizard = DummyHero('Merlin', intelligence=12, hp=90)
archer = DummyHero('Legolas', attack=12, intelligence=12, hp=90)

print(' ')
# Conan атакует Мерлина
warrior_skill.cast(warrior, wizard)
print(f'Merlin HP after hit: {wizard.hp}')
wizard.is_dead()
warrior_skill.cast(warrior, wizard)
print(f'Merlin HP after hit: {wizard.hp}')
wizard.is_dead()
warrior_skill.cast(warrior, wizard)
print(f'Merlin HP after hit: {wizard.hp}')
wizard.is_dead()
print(' ')
# Мерлин отвечает заклинанием
wizard_skill.cast(wizard, warrior)
print(f'Conan HP after hit: {warrior.hp}')
print(' ')
# Legolas атакует Wizard-a
archer_skill.cast(archer, wizard)
print(f'Wizzard, HP after hit: {wizard.hp}')
print(' ')

# -------------
from abc import ABC, abstractmethod


# Product
class Color(ABC):

    def __init__(self, is_metallic: bool, is_matte: bool):
        self.is_metallic = is_metallic
        self.is_matte = is_matte

    @abstractmethod
    def name(self) -> str:
        pass

    def paint(self):
        print(f'Painting car in {self.name()} color')

        if self.is_metallic:
            print('Metalic color was added')
        else:
            print('No metallic added')

        if self.is_matte:
            print('Matte color was added')
        else:
            print('No matte added')

        print('Painting done!')


# Concrete products
class ColorBlack(Color):
    def name(self) -> str:
        return 'black'

class ColorRed(Color):
    def name(self) -> str:
        return 'red'

class ColorBlue(Color):
    def name(self) -> str:
        return 'blue'

# Concrete factory
class ColorFactory(ABC):
    @abstractmethod
    def create(self) -> Color:
        pass

# Factory
class ColorBlackMetalicFactory(ColorFactory):
    def create(self) -> Color:
        return ColorBlack(is_metallic=True, is_matte=False)

class ColorRedMatteFactory(ColorFactory):
    def create(self) -> Color:
        return ColorRed(is_metallic=False, is_matte=True)

class ColorBlueMatteFactory(ColorFactory):
    def create(self) -> Color:
        return ColorBlue(is_metallic=False, is_matte=True)

# Client code
def paint_car(factory: ColorFactory):
    color = factory.create()
    color.paint()


paint_car(ColorBlackMetalicFactory())
print(' ')
paint_car(ColorRedMatteFactory())
print(' ')
paint_car(ColorBlueMatteFactory())

class ColorNoABC:
    def __init__(self, name: str, is_metallic: bool, is_matte: bool):
        self.name = name
        self.is_metallic = is_metallic
        self.is_matte = is_matte

    def paint(self):
        print(f'Painting {self.name}')

        if self.is_metallic:
            print(f'Painting {self.name} metallic')
        else:
            print('Metallic not added')

        if self.is_matte:
            print(f'Painting {self.name} matte')
        else:
            print('Matte not added')

color_black = ColorNoABC(name='Black', is_metallic=True, is_matte=False)
color_red = ColorNoABC(name='Red', is_metallic=True, is_matte=False)
color_blue = ColorNoABC(name='Blue', is_metallic=False, is_matte=True)

def paint_a_car(color: ColorNoABC):
    print('Car is being pass to painting factory')
    color.paint()

paint_a_car(color_black)
print(' ')
paint_a_car(color_red)
print(' ')
paint_a_car(color_blue)
