import os
import json

<<<<<<< HEAD
#kifak


=======
>>>>>>> 0f4d4138c9e4df4c420221f38b27f04e4e04c9f1
# Importeer de functie die je hebt geschreven om facturen te genereren
from je_eerste_pdf import generate_invoices

# Pad naar de map met JSON-bestanden
map_pad = 'test_set_softwareleverancier'
aantal_pdf = len(os.listdir(map_pad))
print(aantal_pdf)
while aantal_pdf > 0:
# Loop door alle bestanden in de map
    for bestandsnaam in os.listdir(map_pad):
        # Controleer of het bestand een JSON-bestand is
        if bestandsnaam.endswith('.json'):
            # Open het JSON-bestand en laad de gegevens
            with open(os.path.join(map_pad, bestandsnaam)) as json_bestand:
                factuur_data = json.load(json_bestand)
            
            # Genereer een unieke naam voor de factuur
            factuur_naam = os.path.splitext(bestandsnaam)[0] + '_factuur.pdf'
            # Genereer de factuur met de gegevens uit het JSON-bestand en sla deze op onder de unieke naam
            generate_invoices(factuur_data, factuur_naam)
<<<<<<< HEAD
    aantal_pdf -= 1
=======
    aantal_pdf -= 1
>>>>>>> 0f4d4138c9e4df4c420221f38b27f04e4e04c9f1
