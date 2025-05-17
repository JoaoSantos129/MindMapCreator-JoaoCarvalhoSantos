import json  # Module pour manipuler JSON

def save_to_file(data, path):
    # Sauvegarde les données (dictionnaire) dans un fichier JSON avec indent pour lisibilité
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)  # ensure_ascii=False pour supporter les accents

def load_from_file(path):
    # Charge et retourne les données JSON depuis un fichier
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)
