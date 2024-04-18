import os
import json

# Importeer de functie die je hebt geschreven om facturen te genereren
from generate_invoices import generate_invoices

# Pad naar de map met JSON-bestanden
map_pad = 'JSON_IN/'

# Pad naar de map waar je de PDF-bestanden wilt opslaan
output_map_pad = 'INVOICE'

# Controleer of de uitvoermap bestaat, zo niet, maak deze dan aan
if not os.path.exists(output_map_pad):
    os.makedirs(output_map_pad)

# Loop door alle bestanden in de map
for bestandsnaam in os.listdir(map_pad):
    # Controleer of het bestand een JSON-bestand is
    if bestandsnaam.endswith('.json'):
        # Open het JSON-bestand en laad de gegevens
        with open(os.path.join(map_pad, bestandsnaam)) as json_bestand:
            factuur_data = json.load(json_bestand)
        
        # Genereer een unieke naam voor de factuur
        factuur_naam = os.path.splitext(bestandsnaam)[0] + '_factuur.pdf'
        
        # Genereer de factuur met de gegevens uit het JSON-bestand
        # en sla deze op onder de unieke naam in de uitvoermap
        output_bestandsnaam = os.path.join(output_map_pad, factuur_naam)
        generate_invoices(factuur_data, output_bestandsnaam)

        # Verplaats het oorspronkelijke JSON-bestand naar de output-map
        os.replace(os.path.join(map_pad, bestandsnaam), os.path.join(output_map_pad, bestandsnaam))
