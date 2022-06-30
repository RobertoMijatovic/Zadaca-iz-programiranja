'''Iz podataka učitanih iz datoteke rezultati.csv sortirati listu po prezimenima.
Napraviti novi rječnik gdje će se po bodovnom rangu upisivati broj ostvarenih ocjena.'''

from csv import reader

with open('rezultati.csv', encoding="utf8") as read_obj:
    csv_reader = reader(read_obj)
    rezultati = list(csv_reader)

rezultati.sort(key=lambda element: element[1])

for i in rezultati:
    print(i)

rijecnik = {
    "Nedovoljnih:" : 0,
    "Dovoljnih:" : 0,
    "Dobrih:" : 0,
    "Vrlo dobrih:" : 0,
    "Odličnih:": 0,
}

for ime,prezime,bodovi in rezultati:
    if int(bodovi) < 50:
        rijecnik["Nedovoljnih:"] += 1
    elif int(bodovi) > 49 and int(bodovi) < 65:
        rijecnik["Dovoljnih:"] += 1
    elif int(bodovi) > 64 and int(bodovi) < 80:
        rijecnik["Dobrih:"] += 1
    elif int(bodovi) > 79 and int(bodovi) < 90:
        rijecnik["Vrlo dobrih:"] += 1
    else:
        rijecnik["Odličnih:"] += 1

for i in rijecnik:
    print(i, rijecnik[i])

print("Ukupno:",len(rezultati))
