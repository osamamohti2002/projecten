import os
import json
from generate_invoices import generate_invoices

JSON_IN = 'C:/Users/lithe/OneDrive/school/how_to_make_money/projecten/JSON_IN'
INVOICE = 'C:/Users/lithe/OneDrive/school/how_to_make_money/projecten/INVOICE'
JSON_PROCESSED = 'C:/Users/lithe/OneDrive/school/how_to_make_money/projecten/JSON_PROCESSED'

eigenaar_gegevens = {
    'Bedrijfsnaam': 'OM Diensten',
    'naam': 'Osama Mohti',
    'adres': 'Lindenlaan 56',
    'Postcode en plaats': '2651TL, Berkel en Rodenrijs',
    'telefoonnummer': '0618383611',
    'email': 'osama@test.nl'
}

if not os.path.exists(INVOICE):
    os.makedirs(INVOICE)

if not os.path.exists(JSON_PROCESSED):
    os.makedirs(JSON_PROCESSED)

for filename in os.listdir(JSON_IN):
    if filename.endswith('.json'):
        file_path = os.path.join(JSON_IN, filename)
        output_file_path = os.path.join(INVOICE, filename)
        output_pdf_path = os.path.splitext(output_file_path)[0] + '.pdf'  # Voeg '.pdf' toe aan het uitvoerbestand
        project_file_path = os.path.join(JSON_PROCESSED, filename)  # Pad naar de map PROJECT

        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        # Voeg eigenaarsgegevens toe
        data['eigenaar_gegevens'] = eigenaar_gegevens

        # Bereken subtotal, btw en totaal en voeg ze toe aan de factuurgegevens
        subtotal = 0
        for product in data['order']['producten']:
            aantal = product['aantal']
            prijs = product['prijs_per_stuk_excl_btw']
            subtotal += prijs * aantal

        btw = subtotal / 100 * 21
        totaal = subtotal + btw

        afrekenen = {
            'subtotal': round(subtotal, 2),
            'btw': round(btw, 2),
            'totaal': round(totaal, 2)
        }

        data['afrekenen'] = afrekenen

        # Genereer de factuur en sla deze op
        generate_invoices(data, output_pdf_path)

        # Schrijf de bijgewerkte factuurgegevens naar het uitvoerbestand in de map 'INVOICE'
        with open(output_file_path, 'w') as output_file:
            json.dump(data, output_file, indent=4)

        os.replace(file_path, project_file_path)
