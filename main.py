import argparse  # Import du module pour gérer les arguments en ligne de commande
import os        # Import du module pour manipuler le système de fichiers
from mindmap.manager import MindMapManager  # Import de la classe principale de gestion de carte mentale

SAVE_PATH = "data/auto_save.json"  # Chemin par défaut pour la sauvegarde automatique

def main():
    parser = argparse.ArgumentParser(description="MindMap CLI")  # Création d'un parser d'arguments avec une description
    subparsers = parser.add_subparsers(dest="command")  # Sous-commandes, le choix de commande sera dans args.command

    # Commande 'create' pour créer une nouvelle carte mentale avec un titre
    subparsers.add_parser("create").add_argument("title")

    # Commande 'add' pour ajouter un enfant à un parent donné
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("parent")  # Nom du nœud parent
    add_parser.add_argument("child")   # Nom du nœud enfant à ajouter

    # Commande 'list' pour afficher la carte mentale actuelle
    subparsers.add_parser("list")

    # Commande 'delete' pour supprimer un nœud par son nom
    del_parser = subparsers.add_parser("delete")
    del_parser.add_argument("name")  # Nom du nœud à supprimer

    # Commande 'save' pour sauvegarder la carte dans un fichier spécifique
    save_parser = subparsers.add_parser("save")
    save_parser.add_argument("filepath")  # Chemin du fichier

    # Commande 'load' pour charger une carte depuis un fichier
    load_parser = subparsers.add_parser("load")
    load_parser.add_argument("filepath")  # Chemin du fichier

    # Commande 'search' pour rechercher un nœud par son nom
    search_parser = subparsers.add_parser("search")
    search_parser.add_argument("name")  # Nom à chercher

    # Commande 'delete-map' pour supprimer la carte mentale auto-sauvegardée
    subparsers.add_parser("delete-map")

    args = parser.parse_args()  # Analyse des arguments passés en ligne de commande
    manager = MindMapManager()  # Instanciation du gestionnaire de carte mentale

    # Charger la carte automatique sauf pour certaines commandes (create, load, delete-map)
    if args.command not in ["create", "load", "delete-map"]:
        if os.path.exists(SAVE_PATH):  # Vérifie si la sauvegarde automatique existe
            manager.load(SAVE_PATH)    # Charge la carte auto-sauvegardée
        else:
            print("Aucune carte trouvée. Créez-en une avec `create`.")  # Message d'erreur si aucune carte chargée
            return  # Quitte la fonction

    # Gestion des commandes
    if args.command == "create":
        manager.create(args.title)   # Crée une nouvelle carte avec le titre donné
        manager.save(SAVE_PATH)      # Sauvegarde automatiquement

    elif args.command == "add":
        manager.add_node(args.parent, args.child)  # Ajoute un enfant sous un parent
        manager.save(SAVE_PATH)                     # Sauvegarde automatique

    elif args.command == "list":
        manager.display()  # Affiche la carte mentale dans la console

    elif args.command == "delete":
        manager.delete_node(args.name)  # Supprime un nœud
        manager.save(SAVE_PATH)         # Sauvegarde automatique

    elif args.command == "save":
        manager.save(args.filepath)  # Sauvegarde dans un fichier choisi

    elif args.command == "load":
        manager.load(args.filepath)  # Charge la carte depuis un fichier
        manager.save(SAVE_PATH)      # Sauvegarde automatique dans le fichier par défaut

    elif args.command == "search":
        manager.search(args.name)  # Recherche un nœud par nom

    elif args.command == "delete-map":
        if os.path.exists(SAVE_PATH):  # Vérifie si le fichier de sauvegarde existe
            os.remove(SAVE_PATH)       # Supprime le fichier auto_save.json
            print("Carte mentale supprimée (fichier auto_save.json).")
        else:
            print("Aucune carte à supprimer.")  # Message si aucune carte auto-sauvegardée

    else:
        parser.print_help()  # Affiche l'aide si commande non reconnue


if __name__ == "__main__":
    main()  # Point d'entrée principal quand le script est exécuté directement
