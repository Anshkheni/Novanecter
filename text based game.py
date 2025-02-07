import time
import random

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

class Character:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.health = 100
        self.inventory = []
    
    def add_to_inventory(self, item):
        self.inventory.append(item)
        slow_print(f"{item} has been added to your inventory!")
    
    def show_inventory(self):
        slow_print("Inventory: " + ", ".join(self.inventory) if self.inventory else "Your inventory is empty.")

def character_creation():
    slow_print("Welcome, traveler! What is your name?")
    name = input("Enter your name: ")
    
    slow_print(f"Greetings, {name}! Choose your role:")
    roles = ["Warrior", "Mage", "Rogue"]
    for i, role in enumerate(roles, 1):
        slow_print(f"{i}. {role}")
    
    while True:
        try:
            choice = int(input("Enter the number of your chosen role: "))
            if 1 <= choice <= len(roles):
                return Character(name, roles[choice - 1])
            else:
                slow_print("Invalid choice. Try again.")
        except ValueError:
            slow_print("Please enter a number.")

def start_adventure(player):
    slow_print(f"{player.name}, the {player.role}, your journey begins now...")
    slow_print("You arrive at a fork in the road. Do you:")
    slow_print("1. Take the left path into the dark forest")
    slow_print("2. Take the right path towards the mountains")
    
    while True:
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            dark_forest(player)
            break
        elif choice == "2":
            mountains(player)
            break
        else:
            slow_print("Invalid choice. Try again.")

def dark_forest(player):
    slow_print("You step into the eerie darkness of the forest...")
    slow_print("A shadowy figure approaches! Do you fight or flee?")
    
    while True:
        choice = input("Type 'fight' or 'flee': ").lower()
        if choice == "fight":
            fight(player)
            break
        elif choice == "flee":
            slow_print("You escape safely back to the fork.")
            start_adventure(player)
            break
        else:
            slow_print("Invalid choice. Try again.")

def fight(player):
    slow_print("You prepare for battle...")
    enemy_health = random.randint(50, 100)
    while enemy_health > 0 and player.health > 0:
        damage = random.randint(10, 30)
        enemy_health -= damage
        slow_print(f"You strike! Enemy health: {enemy_health}")
        if enemy_health <= 0:
            slow_print("You defeated the enemy!")
            player.add_to_inventory("Mystic Sword")
            return
        
        enemy_damage = random.randint(5, 20)
        player.health -= enemy_damage
        slow_print(f"The enemy strikes! Your health: {player.health}")
        if player.health <= 0:
            slow_print("You have fallen in battle. Game Over.")
            exit()

def mountains(player):
    slow_print("You venture towards the towering mountains...")
    slow_print("A mysterious old man offers you a riddle: 'I speak without a mouth and hear without ears. What am I?'")
    
    answer = input("Your answer: ").strip().lower()
    if answer == "echo":
        slow_print("Correct! He grants you a magical amulet.")
        player.add_to_inventory("Magical Amulet")
    else:
        slow_print("Incorrect. The old man vanishes, leaving you to ponder your journey.")
    
    slow_print("Your journey continues...")
    start_adventure(player)

if __name__ == "__main__":
    player = character_creation()
    start_adventure(player)
