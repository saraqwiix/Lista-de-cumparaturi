import json
FILE_PATH = "lista_de_cumparaturi.json"
def load_items():
	try:
		with open(FILE_PATH, "r") as f:
			return json.load(f)
	except FileNotFoundError:
		return []

def main():
	items = load_items()
	print("Lista curenta de cumparaturi:")
	print(items)

if __name__ ==  "__main__":
	main()

