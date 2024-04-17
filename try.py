import os
import json

# Importeer de functie die je hebt geschreven om facturen te genereren
from generate_invoices import generate_invoices

oude_pad = 'test_set_softwareleverancier/2000-018.json'


nieuw_pad = 'JSON_IN/2000-018.json'


os.rename(oude_pad, nieuw_pad)