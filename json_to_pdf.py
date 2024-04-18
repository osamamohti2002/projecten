import os
import json

# Importeer de functie die je hebt geschreven om facturen te genereren
from generate_invoices import generate_invoices

oud_pad = 'JSON_IN'
json_to_pdf_pad = 'INVOICE'
# Pad naar de map met JSON-bestanden
map_pad = 'JSON_IN'
aantal_pdf = len(os.listdir(map_pad))
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
            rsult = os.listdir(json_to_pdf_pad).append(bestandsnaam)
            print(rsult)
    os.rename(oud_pad, json_to_pdf_pad)
    aantal_pdf -= 1