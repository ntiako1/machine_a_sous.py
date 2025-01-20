# Jeu machine à sous - casino
import random
import time

# Initialisation des données
argent_final = 1000 # Pot de départ
argent_initial = argent_final
depense = 0
tour = 0
multiplicateur_bonus = 1 # Par défaut 1, pas de bonus
plus_gros_gain = 0
plus_grosse_perte = 0
tours_gagnes = 0
tours_perdus = 0

def afficher_regle():
    print(f"""
📖 Règles :
    - Chaque tour, vous misez une somme d'argent.
    - Trois symboles apparaissent au hasard.
    - Les combinaisons gagnantes rapportent des gains.
    - Perdez tout votre argent, et le jeu se termine.
===== TOUR n°{tour} =====
    """)

def afficher_statistiques():
    """Affiche les statistiques du joueur."""
    print(f"""
===== STATISTIQUES =====
    - Argent initial : {argent_initial}€
    - Argent actuel : {argent_final}€
    - Total dépensé : {depense}€
    - Plus gros gain : {plus_gros_gain}€
    - Plus grosse perte : {plus_grosse_perte}€
    - Tours joués : {tour}
    - Tours gagnés : {tours_gagnes}
    - Tours perdus : {tours_perdus}
===== STATISTIQUES =====
    """)

def afficher_commandes():
    """"Affiche les commandes disponibles."""
    print("""
===== COMMANDES =====
    - [0] Quitter le jeu
    - [1] Voir les règles
    - [2] Voir les statistiques
===== COMMANDES =====
    """)

# Afficher les règles au début
print("""
===== MACHINE A SOUS by NTIAKO =====
    📖 Règles :
        - Chaque tour, vous misez une somme d'argent.
        - Trois symboles apparaissent au hasard.
        - Les combinaisons gagnantes rapportent des gains.
        - Perdez tout votre argent, et le jeu se termine.

    🫰 Symboles et gains :
        🍋 🍋 🍋 : 5x votre mise
        🍒 🍒 🍒 : 10x votre mise
        ⭐ ⭐ ⭐ : 20x votre mise
        💎 💎 💎 : 50x votre mise
        Tout autre combinaison : Perte de votre mise

    🧨 Bonus :
        🎟️ 🎟️ 🎟️ : Active un bonus multiplicateur pour le prochain gain
===== MACHINE A SOUS by NTIAKO =====
""")

while argent_final > 0:
    tour+= 1

    # Affichage d'infos utiles
    afficher_commandes()
    print(f"\n===== TOUR n°{tour} =====""")
    print(f"    - Vous disposez de {argent_final}€.")

    try:
        entree = input("    - Entrez une mise ou une commande : ")

        # Mettre fin au jeu
        if entree == "0":
            print(f"👋 Merci d'avoir joué à notre jeu ! Vous avez fait un bénéfice de {argent_final - argent_initial}€ en {tour} tour.s.\n===== TOUR n°{tour} =====")
            break
        elif entree == "1":
            afficher_regle()
            continue
        elif entree == "2":
            afficher_statistiques()
            continue

        # Entrée d'une mise
        mise = int(entree)

        # Mise trop élevée
        if mise <= 0 or mise > argent_final:
            print(f"    Mise invalide. Vous devez miser entre 1 et {argent_final}€.")
            continue
    except ValueError:
        print("    Veuillez entrer un montant valide.")
        continue

    depense += mise
    print("    🎰 La machine tourne", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
    print("\n")

    tirage = random.choices(["🍒", "🍋", "⭐", "🍇", "🔔", "💎", "🎟️"], k=3) # Tirage

    print("    🎰 Vous avez tirez : ", " | ".join(tirage))

    gain = 0
    # Gains selon les combinaisons
    if tirage == ['🍋', '🍋', '🍋']:
        gain = entree * 5
    elif tirage == ['🍒', '🍒', '🍒']:
        gain = entree * 10
    elif tirage == ['⭐', '⭐', '⭐']:
        gain = entree * 20
    elif tirage == ['💎', '💎', '💎']:
        gain = entree * 50
    elif tirage == ['🎟️', '🎟️', '🎟️']:
        print("\n    👍 Bonus activé ! Lancez 3 mini-tirages pour déterminer votre multiplicateur.")
        gain = 0

        # Système de bonus multiplicateur
        mini_multiplicateur = 0
        for i in range(3):
            time.sleep(1)
            mini_tirage = random.choices(['💴', '💵', '💶', '💷'], k=3)
            print(f"        Mini-tirage {i+1} : {' | '.join(mini_tirage)}")
            if mini_tirage == ['💵', '💵', '💵']:
                print("        💵 Bonus de x1.5 ajouté !")
                mini_multiplicateur += 1.5
            elif mini_tirage == ['💶', '💶', '💶']:
                print("        💶 Bonus de x2 ajouté !")
                mini_multiplicateur += 2
            elif mini_tirage == ['💷', '💷', '💷']:
                print("        💷 Bonus de x3 ajouté !")
                mini_multiplicateur += 3
        multiplicateur_bonus = max(1, mini_multiplicateur)  # Assurez un bonus minimum de x1
        print(f"        🎉 Votre multiplicateur total pour le prochain gain est de x{multiplicateur_bonus} !")

    if gain > 0:
        gain *= multiplicateur_bonus # Appliquer le multiplicateur bonus
        argent_final += gain
        multiplicateur_bonus = 1
        plus_gros_gain = max(plus_gros_gain, gain)
        print(f"    🎉 Bravo ! Vous gagnez {gain}€ avec un multiplicateur de x{multiplicateur_bonus} !\n===== TOUR n°{tour} =====")
    else:
        argent_final -= mise
        tours_perdus += 1
        plus_grosse_perte = max(plus_grosse_perte, mise)
        print(f"    😔 Perdu... Réessayez ?\n===== TOUR n°{tour} =====")

# Fin du jeu
if argent_final == 0:
    print(f"\n\n😥 Vous êtes à sec.. Vous avez dépensé un total de : {depense}€ en {tour} tour.s.")