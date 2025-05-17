class Node:
    def __init__(self, name):
        self.name = name        # Nom du nœud
        self.children = []      # Liste des enfants (initialement vide)

    def to_dict(self):
        # Convertit le nœud et ses enfants récursivement en dictionnaire pour JSON
        return {
            'name': self.name,
            'children': [child.to_dict() for child in self.children]
        }

    @staticmethod
    def from_dict(data):
        node = Node(data['name'])  # Création d'un nœud avec le nom fourni
        # Reconstruction récursive des enfants à partir des données
        node.children = [Node.from_dict(child) for child in data.get('children', [])]
        return node
