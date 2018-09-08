
class summon:
    name = ""
    starting_hp = 0
    hp = 0
    
    def __init__(self,name,start_hp):
        self.name = name
        self.starting_hp = start_hp
        self.hp = start_hp
    
    def inflict_damage(self,dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
            
    def heal_hp(self,hp):
        self.hp += hp
        if self.hp > self.starting_hp:
            self.hp = self.starting_hp
            
    