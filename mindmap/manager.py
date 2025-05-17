from mindmap.models import Node  # Import de la classe Node (représentation des nœuds)
from mindmap.storage import save_to_file, load_from_file  # Fonctions de sauvegarde/chargement JSON

class MindMapManager:
    def __init__(self):
        self.root = None  # Nœud racine de la carte mentale, initialement vide

    def create(self, title):
        self.root = Node(title)  # Création d'un nouveau nœud racine avec le titre donné
        print(f"Carte créée avec le titre : {title}")  # Message de confirmation

    def add_node(self, parent_name, child_name):
        parent = self.find_node(self.root, parent_name)  # Recherche du parent dans l'arbre
        if parent:
            if self.get_depth(parent) >= 2:  # Limite la profondeur à 3 niveaux (0-based)
                print("Erreur : profondeur maximale atteinte (3 niveaux)")
                return
            parent.children.append(Node(child_name))  # Ajoute un nouveau nœud enfant
            print(f"Nœud '{child_name}' ajouté sous '{parent_name}'")
        else:
            print(f"Nœud parent '{parent_name}' introuvable.")  # Message si parent non trouvé

    def find_node(self, node, name):
        if node.name == name:  # Si le nœud courant correspond au nom cherché
            return node
        for child in node.children:  # Sinon, recherche récursive chez les enfants
            found = self.find_node(child, name)
            if found:
                return found
        return None  # Retourne None si non trouvé

    def get_depth(self, node, depth=0):
        if not node.children:  # Si pas d'enfants, profondeur = profondeur actuelle
            return depth
        # Renvoie la profondeur maximale parmi les enfants (récursif)
        return max(self.get_depth(child, depth + 1) for child in node.children)

    def display(self, node=None, indent=0):
        if self.root is None:
            print("Aucune carte chargée.")  # Message si aucune carte existante
            return
        if node is None:
            node = self.root  # Si pas de nœud donné, commence à la racine
        print("  " * indent + f"- {node.name}")  # Affiche le nœud avec indentation
        for child in node.children:  # Affiche récursivement les enfants avec indentation croissante
            self.display(child, indent + 1)

    def delete_node(self, name):
        if self.root.name == name:
            print("Impossible de supprimer la racine.")  # On ne peut pas supprimer la racine
            return
        if self._delete_node(self.root, name):  # Lance la suppression récursive
            print(f"Nœud '{name}' supprimé.")
        else:
            print(f"Nœud '{name}' introuvable.")  # Message si non trouvé

    def _delete_node(self, parent, name):
        for i, child in enumerate(parent.children):  # Parcourt les enfants du parent
            if child.name == name:
                del parent.children[i]  # Supprime le nœud enfant
                return True
            if self._delete_node(child, name):  # Recherche récursive chez les enfants
                return True
        return False  # Nœud non trouvé dans ce sous-arbre

    def save(self, path):
        if not self.root:
            print("Aucune carte à sauvegarder.")  # Message si aucune carte en mémoire
            return
        save_to_file(self.root.to_dict(), path)  # Sauvegarde la carte convertie en dict
        print(f"Carte sauvegardée dans '{path}'")

    def load(self, path):
        data = load_from_file(path)  # Charge les données JSON depuis le fichier
        self.root = Node.from_dict(data)  # Reconstruit l'arbre à partir du dict
        print(f"Carte chargée depuis '{path}'")

    def search(self, name):
        path = []  # Liste pour stocker le chemin trouvé
        if self._search(self.root, name, path):  # Recherche récursive
            print(" > ".join(path))  # Affiche le chemin sous forme "racine > ... > nœud"
        else:
            print(f"Nœud '{name}' non trouvé.")

    def _search(self, node, name, path):
        path.append(node.name)  # Ajoute le nœud courant au chemin
        if node.name == name:
            return True  # Trouvé
        for child in node.children:
            if self._search(child, name, path):  # Recherche récursive
                return True
        path.pop()  # Si non trouvé ici, enlève le nœud du chemin (backtracking)
        return False
