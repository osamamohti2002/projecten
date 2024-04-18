import sqlite3

# Definieer functie om facturen naar de database te schrijven
def write_to_database(data):
    conn = sqlite3.connect('om_diensten.db')
    cursor = conn.cursor()

    # Tabel facturen (Invoices) aanmaken
    cursor.execute('''CREATE TABLE IF NOT EXISTS facturen (
                    Factuur_id INTEGER PRIMARY KEY,
                    order_nr TEXT,
                    order_datum TEXT,
                    betaaltermijn TEXT
                    )''')

    # Tabel klanten (Customers) aanmaken
    cursor.execute('''CREATE TABLE IF NOT EXISTS klanten (
                    klant_id INTEGER PRIMARY KEY,
                    naam TEXT,
                    adres TEXT,
                    postcode TEXT,
                    stad TEXT,
                    kvk_nummer TEXT,
                    order_nr TEXT
                    )''')

    # Tabel producten (Products) aanmaken
    cursor.execute('''CREATE TABLE IF NOT EXISTS producten (
                    product_id INTEGER PRIMARY KEY,
                    aantal INTEGER,
                    productnaam TEXT,
                    prijs_per_stuk_excl_btw REAL,
                    btw REAL,
                    order_nr TEXT
                    )''')

    # Veranderingen committen en cursor en connectie sluiten
    conn.commit()

    # Haal factuurinformatie op
    order_number = data['order']['ordernummer']
    order_date = data['order']['orderdatum']
    payment_terms = data['order']['betaaltermijn']

    # Voeg factuurinformatie toe aan de database
    cursor.execute('INSERT INTO facturen ("order_nr", "order_datum", "betaaltermijn") VALUES (?, ?, ?)',
                   (order_number, order_date, payment_terms))
    conn.commit()

    # Haal klantinformatie op
    customer_name = data['order']['klant']['naam']
    customer_address = data['order']['klant']['adres']
    customer_postcode = data['order']['klant']['postcode']
    customer_city = data['order']['klant']['stad']
    customer_kvk_number = data['order']['klant']['KVK-nummer']

    # Voeg klantinformatie toe aan de database
    cursor.execute('INSERT INTO klanten ("naam", "adres", "postcode", "stad", "kvk_nummer", "order_nr") VALUES (?, ?, ?, ?, ?, ?)',
                   (customer_name, customer_address, customer_postcode, customer_city, customer_kvk_number, order_number))
    conn.commit()

    # Haal productinformatie op en voeg deze toe aan de database
    for product in data['order']['producten']:
        product_amount = product['aantal']
        product_name = product['productnaam']
        product_price_per_unit_excl_btw = product['prijs_per_stuk_excl_btw']
        product_btw = product['btw_percentage']

        cursor.execute('INSERT INTO producten ("aantal", "productnaam", "prijs_per_stuk_excl_btw", "btw", "order_nr") VALUES (?, ?, ?, ?, ?)',
                       (product_amount, product_name, product_price_per_unit_excl_btw, product_btw, order_number))
        conn.commit()

    # Sluit de databaseconnectie
    conn.close()


