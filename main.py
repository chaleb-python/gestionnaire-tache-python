taches = []

while True:
    print("\n--- GESTIONNAIRE DE TÂCHES ---")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Supprimer une tâche")
    print("4. Quitter")

    choix = input("Choisis une option : ")

    if choix == "1":
        tache = input("Entre ta tâche : ")
        taches.append(tache)
        print("Tâche ajoutée !")

    elif choix == "2":
        if len(taches) == 0:
            print("Aucune tâche.")
        else:
            print("\nTes tâches :")
            for i, tache in enumerate(taches, 1):
                print(f"{i}. {tache}")

    elif choix == "3":
        if len(taches) == 0:
            print("Aucune tâche à supprimer.")
        else:
            for i, tache in enumerate(taches, 1):
                print(f"{i}. {tache}")

            numero = int(input("Numéro de la tâche à supprimer : "))

            if 1 <= numero <= len(taches):
                taches.pop(numero - 1)
                print("Tâche supprimée !")
            else:
                print("Numéro invalide.")

    elif choix == "4":
        print("À bientôt !")
        break

    else:
        print("Choix invalide.")
