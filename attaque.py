import random
player_1 = input("Le nom de 1er joueur: ")
player_2 = input("Le nom de 2éme joueur: ")
fois = 0
nombre = 0
score_2 = 250
score_1 = 250
def attack(score,player):
    random_attack = bool(random.randint(0, 1))
    if random_attack == True:
        random_damage = random.randint(0, 100)
        score -= random_damage
        print("\tl'attaque est réussit\n vous infligera un dègats de",random_damage,"à votre ennemi",player)
    else:
        print("\tL'attaque est ratée\n C'est au tour de ",player) 
    return score
while fois < 2:
    fois += 1
    score_2 = attack(score_2,player_2)
    score_1 = attack(score_1,player_1)
print("\nFIN DU COMBAT !\n")
if score_1 > score_2:
    print(player_1,"a gagner le jeu avec un score de: ",score_1)
    print(player_2,"a échoué avec un score de :",score_2) 
else:
    print(player_2,"a gagner le jeu avec un score de: ",score_2)    
    print(player_1,"a échoué avec un score de :",score_1) 