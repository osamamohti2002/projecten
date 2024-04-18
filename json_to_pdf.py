import os
import json
# Importeer de functie die je hebt geschreven om facturen te genereren
from generate_invoices import *


# Pad naar de map met JSON-bestanden
JSON_PAD = 'C:/Users/lithe/OneDrive/school/how_to_make_money/projecten/JSON_IN'
# Pad naar de map waar je de PDF-bestanden wilt opslaan
INVOICE_PAD = 'C:/Users/lithe/OneDrive/school/how_to_make_money/projecten/INVOICE'
PROCESSED = 'C:/Users/lithe/OneDrive/school/how_to_make_money/projecten/JSON_PROCESSED'




# Controleer of de uitvoermap bestaat, zo niet, maak deze dan aan
if not os.path.exists(INVOICE_PAD):
    os.makedirs(INVOICE_PAD)

if not os.path.exists(PROCESSED):
    os.makedirs(PROCESSED)



# Loop door alle bestanden in de map
for bestandsnaam in os.listdir(JSON_PAD):
    # Controleer of het bestand een JSON-bestand is
    if bestandsnaam.endswith('.json'):
        # Open het JSON-bestand en laad de gegevens
        with open(os.path.join(JSON_PAD, bestandsnaam)) as json_bestand:
            factuur_data = json.load(json_bestand)

        # Genereer een unieke naam voor de factuur
        factuur_naam = os.path.splitext(bestandsnaam)[0] + '_factuur.pdf'
        
        # Genereer de factuur met de gegevens uit het JSON-bestand
        # en sla deze op onder de unieke naam in de uitvoermap
        output_bestandsnaam = os.path.join(INVOICE_PAD, factuur_naam)
        generate_invoices(factuur_data, output_bestandsnaam)

        # Verplaats het oorspronkelijke JSON-bestand naar de output-map
        os.replace(os.path.join(JSON_PAD, bestandsnaam), os.path.join(INVOICE_PAD, bestandsnaam))
        os.replace(os.path.join(INVOICE_PAD, bestandsnaam), os.path.join(PROCESSED, bestandsnaam))



