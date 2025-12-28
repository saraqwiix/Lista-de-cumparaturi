
import json
import sys

FILE_PATH = "lista_de_cumparaturi.json"

def load_items():
    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_items(items):
    with open(FILE_PATH, "w") as f:
        json.dump(items, f, indent=2)

def add_item(nume, cantitate, pret, categorie):
    if cantitate <= 0:
        print("Eroare: cantitatea trebuie sa fie mai mare decat 0")
        return

    if pret < 0:
        print("Eroare: pretul  trebuie sa fie pozitiv")
        return

    items = load_items()
    item = {
        "nume": nume,
        "cantitate": cantitate,
        "pret": pret,
        "categorie": categorie
    }

    items.append(item)
    save_items(items)

    total = cantitate * pret

    print(
        f"Articol adaugat cu succes: {nume} "
        f"(cantitate: {cantitate}, pret: {pret}, total: {total}, categorie: {categorie})"
    )

def list_items(sort_key = None):
    items = load_items()

    if not items:
        print("Lista de cumparaturi este goala")
        return
    if sort_key:
        if sort_key not in ["nume", "pret", "categorie"]:
            print(f"Sortarea nu s-a putut realiza: {sort_key}")
            return
        items.sort(key=lambda x: x[sort_key])
    print("Lista de cumparaturi:")
    for item in items:
        total = item["cantitate"] * item["pret"]
        print(
            f"- {item['nume']} | "
            f"cantitate: {item['cantitate']} | "
            f"pret: {item['pret']} | "
            f"total: {total} | "
            f"categorie: {item['categorie']}"
        )

def main():
    if len(sys.argv) < 2:
        print("Folosire: python3 app/main.py add <nume> <cantitate> <pret> <categorie>")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) !=6:
            print("Folosire: add <nume> <cantitate> <pret> <categorie>")
            return

        nume = sys.argv[2]
        cantitate = int(sys.argv[3])
        pret = float(sys.argv[4])
        categorie = sys.argv[5]

        add_item(nume, cantitate, pret, categorie)
    elif command == "list":
        sort_key = None
        if len(sys.argv) == 4  and sys.argv[2] == "--sort":
            sort_key = sys.argv[3]

        list_items(sort_key)

    else:
        print(f"Comanda introdusa nu exista: {command}")

if __name__ ==  "__main__":
    main()


