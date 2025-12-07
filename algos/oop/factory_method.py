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
