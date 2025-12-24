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
	save.items(items)

	total = cantitate * pret

	print(
		f"Articol adaugat cu succes: {name} "
		f"(cantitate: {cantitate}, pret: {pret}, total: {total}, categorie: {categorie})
)

def main():
	items = load_items()
	print("Lista curenta de cumparaturi:")
	print(items)

if __name__ ==  "__main__":

	main()

