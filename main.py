# Jeu machine à sous - casino
import random
import time

# Afficher les règles
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
===== MACHINE A SOUS by NTIAKO =====
""")

# Initialisation des données
argent_final = 1000 # Pot de départ
argent_initial = argent_final
depense = 0
tour = 0

while argent_final > 0:
    tour+= 1

    # Affichage d'infos utiles
    print(f"""
===== TOUR n°{tour} =====
    - Vous disposez de {argent_final}€.
    - Tapez 0 pour quitter le jeu.""")

    try:
        mise = int(input("    - Entrez une mise : ")) # Entrée d'une mise

        # Mettre fin au jeu
        if mise == 0:
            print(f"👋 Merci d'avoir joué à notre jeu ! Vous avez fait un bénéfice de {argent_final - argent_initial}€ en {tour} tour.s.")
            break

        # Mise trop élevée
        if mise > argent_final or mise <= 0:
            mise = print(f"    Mise invalide. Vous devez miser entre 1 et {argent_final}€.")
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

    tirage = random.choices(["🍒", "🍋", "⭐", "🍇", "🔔", "💎"], k=3) # Tirage
    print("    🎰 Vous avez tirez : ", " | ".join(tirage))

    # Mise x5
    if tirage == ['🍋', '🍋', '🍋']:
        print(f"    🎉 Bravo ! Vous gagnez {mise*5}€.")
        argent_final += mise*5

    # Mise x10
    elif tirage == ['🍒', '🍒', '🍒']:
        print(f"    🥳 Wow ! Vous gagnez {mise*10}€.")
        argent_final += mise*10

    # Mise x20
    elif tirage == ['⭐', '⭐', '⭐']:
        print(f"    🏆 Incroyable ! Vous gagnez {mise*20}€.")
        argent_final += mise*20

    elif tirage == ['💎', '💎', '💎']:
        argent_final += mise * 50
        print(f"    💎 JACKPOT ! Vous gagnez {mise*50}€.")

    # Perdu, joueur perd sa mise
    else:
        argent_final -= mise
        print(f"    Perdu.. Retentez votre chance ?\n===== TOUR n°{tour} =====")

# Fin, joueur à sec
if argent_final == 0:
    print(f"\n\n😥 Vous êtes à sec.. Vous avez dépensé un total de : {depense}€ en {tour} tour.s.")