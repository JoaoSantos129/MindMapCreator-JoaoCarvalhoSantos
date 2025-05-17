
# 🧠 MindMap CLI

Un outil en ligne de commande pour créer, gérer et sauvegarder des **cartes mentales** sous forme d’arborescences hiérarchiques simples.

---

## 🌟 Fonctionnalités

### ✅ Fonctionnalités principales
- **Créer** une nouvelle carte avec un titre racine
- **Ajouter** un nœud (idée) à un nœud parent (profondeur maximale : 3 niveaux)
- **Afficher** la carte mentale dans le terminal sous forme d’arborescence
- **Supprimer** un nœud (et toutes ses sous-idées)
- **Sauvegarder** une carte mentale dans un fichier `.json`
- **Charger** une carte mentale depuis un fichier `.json`
- **Rechercher** un nœud et afficher son chemin depuis la racine

### 🧪 Fonctionnalités bonus
- ✅ Auto-sauvegarde de la carte dans `data/auto_save.json`
- ✅ Suppression de la carte mentale auto-sauvegardée (`delete-map`)
- ✅ Vérification automatique de la **profondeur maximale** autorisée

---

## ⚙️ Installation

### 1. Cloner le dépôt
```bash
git clone https://github.com/votre-utilisateur/mindmap-cli.git
cd mindmap-cli
```

### 2. Installer Python 3 (requis)

Ce projet nécessite Python 3.7 ou une version ultérieure.

- 🔗 Téléchargez Python ici : https://www.python.org/downloads/

Vérifiez l’installation avec :
```bash
python3 --version
# ou
python --version
```

Aucune autre dépendance externe n’est nécessaire. Le script utilise uniquement les bibliothèques standards de Python.


---

## 🚀 Lancement de l'application

Utilisez Python en ligne de commande pour exécuter l’outil :

```bash
python main.py <commande> [arguments]
```

### Exemple :
```bash
python main.py create "Ma Carte"
python main.py add "Ma Carte" "Idée 1"
python main.py list
```

---

## 📖 Commandes disponibles

| Commande       | Description |
|----------------|-------------|
| `create <titre>` | Crée une nouvelle carte mentale |
| `add <parent> <child>` | Ajoute un enfant à un nœud parent |
| `list`         | Affiche la carte mentale actuelle |
| `delete <nom>` | Supprime un nœud et ses enfants |
| `save <fichier>` | Sauvegarde dans un fichier `.json` |
| `load <fichier>` | Charge une carte depuis un fichier `.json` |
| `search <nom>` | Recherche un nœud et affiche son chemin |
| `delete-map`   | Supprime la sauvegarde automatique (`data/auto_save.json`) |

---

## 💡 Structure du projet

```
mindmap-cli/
│
├── main.py                   # Point d’entrée CLI
├── mindmap/
│   ├── __init__.py
│   ├── manager.py            # Logique de gestion de carte mentale
│   ├── models.py             # Représentation des nœuds
│   └── storage.py            # Fonctions de lecture/écriture JSON
│
├── data/
│   └── auto_save.json        # Sauvegarde automatique
└── README.md
```

---

## 🧪 Exemple visuel

```bash
$ python main.py create "Projet"
$ python main.py add "Projet" "Étude"
$ python main.py add "Étude" "Recherche"
$ python main.py list
- Projet
  - Étude
    - Recherche
```

---

## 📂 Sauvegarde

Les cartes peuvent être :
- **Auto-sauvegardées** dans `data/auto_save.json`
- **Sauvegardées manuellement** avec la commande `save`
- **Restaurées** à tout moment avec la commande `load`

---

## 👤 Auteur

NOM Prénom : CARVALHO SANTOS João 
Profil Github : JoaoSantos129