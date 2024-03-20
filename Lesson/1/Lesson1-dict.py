# Python Pro | Ders 1 
# Note = Note.md

sozluk = {
    "bilahare": "1. sonradan",
    "fiktil": "1. Suni, Yapay",
    "teyyehüc": "1. Heyecan",
    "meskene": "1. Miskin"
}

# Ekstra
while True:
    a = str(input("Search for Word(TR) >>"))
    a = a.lower()
    if a in sozluk:
        print(f"{a} | " + sozluk[a])
    else:
        print("Sözcük Bulunamadı ... ")