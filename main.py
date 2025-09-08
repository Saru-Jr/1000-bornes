import random

class game:
    def __init__(self, born, defense, attack, special):
        self.born = born
        self.defense = defense
        self.attack = attack
        self.special = special

        # Distance cards values and their quantities
        self.born_cards = {
            '25km': {"value": 25, "quantity": 18},
            '50km': {"value": 50, "quantity": 10},
            '75km': {"value": 75, "quantity": 10},
            '100km': {"value": 100, "quantity": 12},
            '200km': {"value": 200, "quantity": 4}
        }

        # Total number of distance cards is 54
        #self.total_distance_cards = sum(card["quantity"] for card in self.born_cards.values())

        # Defense cards values and their quantities
        self.defense_cards = {
            "essence": {"value": essence, "quantity": 5},
            "roue de secours": {"value": roue_de_secours, "quantity": 6},
            "reparation": {"value": reparation, "quantity": 6},
            "fin de limitation de vitesse": {"value": fin_de_limitation_de_vitesse, "quantity": 6},
        }
            
        # Total number of defense cards is 23
        #self.total_defense_cards = sum(card["quantity"] for card in self.defense_cards.values())

        # Attack cards values and their quantities
        self.attack_cards = {
            "panne d'essence": {"value": panne_dessence, "quantity": 5},
            "crevaison": {"value": crevaison, "quantity": 4},
            "accident": {"value": accident, "quantity": 4},
            "limitation de vitesse": {"value": limitation_de_vitesse, "quantity": 3},
            "feu rouge": {"value": feu_rouge, "quantity": 5},
        }

        # Total number of attack cards is 21
        #self.total_attack_cards = sum(card["quantity"] for card in self.attack_cards.values())

        # Special cards values and their quantities
        self.special_cards = {
            "increvable": {"value": increvable, "quantity": 1},
            "vehicule prioritaire": {"value": vehicule_prioritaire, "quantity": 1},
            "as du volant": {"value": as_du_volant, "quantity": 1},
            "citerne d'essence": {"value": citerne_dessence, "quantity": 1},
        }

        # Total number of special cards is 4
        #self.total_special_cards = sum(card["quantity"] for card in self.special_cards.values())
