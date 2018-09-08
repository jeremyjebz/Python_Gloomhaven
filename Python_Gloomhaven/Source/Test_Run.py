from player_character import player_character
from tkinter import *

player = player_character("Player",13)
player.inflict_condition("poison")
player.inflict_condition("wound")
player.inflict_condition("invalid condition")
player.add_exp(5)
player.add_exp(7)
player.inflict_damage(8)
player.heal_hp(2)
player.add_gold(53)
player.add_gold(-10)
player.add_summon("Creature 1", 6)
player.add_summon("Creature 2", 15)
player.describe()