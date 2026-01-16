import json
import sys
import csv

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

def remove_item(nume):
    items = load_items()
    items_noi = []

    gasit = False

    for item in items:
        if item["nume"] == nume:
            gasit = True
        else:
            items_noi.append(item)
    if not gasit:
        print(f"Articolul '{nume}' nu a fost gasit.")
        return

    save_items(items_noi)
    print(f"Articolul '{nume}' a fost sters cu succes.")

def total_cost():
    items = load_items()

    total = 0
    for item in items:
        total += item["cantitate"] * item["pret"]

    print(f"Cost total: {total} RON")
    print(f"Articole: {len(items)}")

def search_by_category(categorie):
    items = load_items()
    gasite = False

    print(f"Articole din categoria: '{categorie}':")

    for item in items:
        if item["categorie"] == categorie:
            total = item["cantitate"] * item["pret"]
            print(
                f"- {item['nume']} | cantitate: {item['cantitate']} "
                f"| pret: {item['pret']} | total: {total}"
            )
            gasite = True

    if not gasite:
        print("Nu exista articole in aceasta categorie")

def subtotal_pe_categorie():
    items = load_items()
    if not items:
        print("Lista de cumparaturi este goala.")
        return

    subtotal = {}
    for item in items:
        subtotal[item["categorie"]] = subtotal.get(item["categorie"], 0) + item["cantitate"] * item["pret"]

    print("Subtotaluri pe categorii:")
    for categorie, total in subtotal.items():
        print(f"- {categorie}: {total} RON")

def export_csv(filename):
    items = load_items()

    if not items:
        print("Lista de cumparaturi este goala")
        return

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["nume", "cantitate", "pret", "categorie", "total"])

        for item in items:
            total = item["cantitate"] * item["pret"]
            writer.writerow([
                item["nume"],
                item["cantitate"],
                item["pret"],
                item["categorie"],
                total
            ])

    print(f"Lista a fost exportata cu succes in {filename}")

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

def help():
    print("Aplicatie - Lista de cumparaturi")
    print()
    print("Comenzile disponibile sunt:")
    print(" add <nume> <cantitate> <pret> <categorie>")
    print("     Adauga un articol nou in  lista")
    print()
    print(" remove <nume>")
    print("     Sterge un articol dupa nume")
    print()
    print(" list [--sort <nume|pret|categorie>]")
    print("     Afiseaza lista de cumparaturi (optional sortata)")
    print()
    print(" search --category <categorie>")
    print("     Afiseaza articolele dintr-o categorie")
    print()
    print(" total")
    print("     Afiseaza costul total al listei")
    print()
    print(" subtotal")
    print("     Afiseaza subtotalul pe fiecare categorie")
    print()
    print(" export <fisier.csv>")
    print("     Exporta lista in format CSV")
    print()
    print(" help")
    print("     Afiseaza meniul de ajutor")

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

    elif command == "remove":
        if len(sys.argv) != 3:
            print("Folosire: remove <nume>")
            return

        nume = sys.argv[2]
        remove_item(nume)

    elif command == "list":
        sort_key = None
        if len(sys.argv) == 4  and sys.argv[2] == "--sort":
            sort_key = sys.argv[3]

        list_items(sort_key)

    elif command == "total":
        total_cost()

    elif command == "subtotal":
        subtotal_pe_categorie()

    elif command == "search":
        if len(sys.argv) != 4 or sys.argv[2] != "--category":
            print("Folosire: search --category <categorie>")
            return

        categorie = sys.argv[3]
        search_by_category(categorie)

    elif command == "export":
        if len(sys.argv) != 3:
            print("Folosire: export <fisier.csv>")
            return

        filename = sys.argv[2]
        export_csv(filename)

    elif command == "help":
        help()

    else:
        print(f"Comanda introdusa nu exista: {command}")

if __name__ ==  "__main__":
    main()


