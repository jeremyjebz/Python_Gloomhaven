#
# Player Character class
#

from summon import summon

class player_character(object):
    
    name = ""
    conditions = {}
    valid_conditions = ["poison", "wound", "muddle", "blind", "paralyze","invisible","strength"]
    experience = 0
    starting_hp = 0
    hp = 0
    gold = 0
    summons = {}
    
    def __init__(self,name,start_hp):
        self.name = name
        self.starting_hp = start_hp
        self.hp = start_hp
               
    def inflict_condition(self,condition):
        if condition in self.valid_conditions:
            self.conditions[condition] = True
            
    def remove_condition(self,condition):
        del self.conditions[condition]
            
    def add_exp(self,exp):
        self.experience += exp
        
    def inflict_damage(self,dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
            
    def add_gold(self,gold):
        self.gold += gold   
            
    def heal_hp(self,hp):
        self.hp += hp
        if self.hp > self.starting_hp:
            self.hp = self.starting_hp       
     
    def add_summon(self,name,hp):
        new_summon = summon(name,hp)
        
        self.summons[name] = new_summon 
        
    def remove_summon(self,name):
        del self.summons[name]
    
    def describe(self):
        print(self)
        print("Name: %s" % self.name)
        
        for cond in self.conditions:
            print("Afflicted by: %s" % cond)  
            
        print("Experience: %d" % self.experience)    
        
        print("Current HP: %d" % self.hp)
        print("Max HP: %d" % self.starting_hp)
        
        print("Current Gold: %d" % self.gold)
        
        for name in self.summons:
            print("Summon: %s" % self.summons[name].name)
        
        
        
        
        
        
        
        
        
        
        
        
        
        