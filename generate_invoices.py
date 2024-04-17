from fpdf import FPDF
<<<<<<< HEAD
from math import ceil
=======
>>>>>>> 0f4d4138c9e4df4c420221f38b27f04e4e04c9f1
import json


def generate_invoices(data, pdf_filename):
    pdf = FPDF('P', 'mm', 'A4')


    # Add a page
    pdf.add_page()


    # Aad achtergrond color 
    pdf.set_fill_color(255, 255, 255)
    pdf.rect(0, 0, pdf.w, pdf.h / 2, 'F')



    # Specify font
    pdf.set_font('helvetica', '', 16)


    pdf.set_font('Arial', 'B', 20)
    pdf.cell(120, 10, 'FACTUUR', ln=True)
    pdf.ln(10)

    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'FACTUURNUMMER', ln=1, align='L')
    pdf.set_font('Arial', '', 11)
    pdf.cell(0, 10, data["order"]["ordernummer"], ln=1, align='L')
    pdf.ln(-15)

    pdf.set_font('Arial', 'B', 12)
    pdf.cell(80, 50, 'Datum', ln=True)
    pdf.ln(-40)
    pdf.set_font('Arial', '', 12)
    pdf.cell(80, 50, data["order"]["orderdatum"], ln=True)


    # Infomatie over de klant
<<<<<<< HEAD
    pdf.ln(40)
=======
    pdf.ln(5)
>>>>>>> 0f4d4138c9e4df4c420221f38b27f04e4e04c9f1
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(120, 10, 'FACTUUR AAN: ', ln=True)
    pdf.set_font('Arial', '', 11)
    pdf.cell(120, 5, data["order"]["klant"]["naam"], ln=True)
    pdf.cell(120, 5, data["order"]["klant"]["adres"], ln=True)
    pdf.cell(120, 5, data["order"]["klant"]["postcode"], ln=True)
    pdf.cell(120, 5, data["order"]["klant"]["stad"], ln=True)
    pdf.cell(120, 5, f"KVK-nummer: {data['order']['klant']['KVK-nummer']}", ln=True)
    pdf.cell(120, 5, f"Betaaltermijn {data['order']['betaaltermijn']}", ln=True)


    # Infomatie over de eigenaar
    pdf.ln(-50)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(180, -120, 'OM Diensten', ln=True, align='R')
    pdf.set_font('Arial', '', 11)
    pdf.cell(180, 135, 'Osama Mohti', ln=1, align='R')
    pdf.cell(180, -120, 'Lindelaan 56', ln=1, align='R')
    pdf.cell(180, 135, '2651 TL, Berkel en Rodenrijd', ln=1, align='R')
    pdf.cell(180, -120, '0618383611', ln=1, align='R')
    pdf.cell(180, 135, 'Oosama.motee@gmail.com', ln=1, align='R')


<<<<<<< HEAD
    





=======
>>>>>>> 0f4d4138c9e4df4c420221f38b27f04e4e04c9f1

    # ----------------------------------------------------------------
    pdf.ln(25)
    pdf.set_fill_color(255, 255, 255)

    # Information about products
    pdf.set_font('Arial', '', 12)
    pdf.ln(10)
<<<<<<< HEAD
    pdf.cell(50, 15, 'AANTAL', border=0)
    pdf.cell(50, 15, 'OMSCHRIJVING', border=0)
    pdf.cell(50, 15, 'PRIJS PER EENHEID', border=0)
    pdf.cell(50, 15, 'REGELTOTAAL', border=0)
    pdf.ln(7)

    subtotal = 0
    # Iterate over products
    for product in data["order"]["producten"]:
        pdf.cell(50, 15, str(product["aantal"]), border=0)
        pdf.cell(50, 15, product["productnaam"], border=0)
        pdf.cell(50, 15, str(product["prijs_per_stuk_excl_btw"]), border=0)
        pdf.cell(50, 15, str(product["aantal"] * product["prijs_per_stuk_excl_btw"]), border=0)
        pdf.ln(7)
        subtotal += product["aantal"] * product["prijs_per_stuk_excl_btw"]

    pdf.ln(10)

    # Create table to check out
    # subtotal = sum(product["prijs_per_stuk_excl_btw"])
    btw = subtotal / 100 * 21
    total = (subtotal + btw)


    total_bedrag = [
        {'subtotal': round(float(subtotal), 2)},
        {'BTW': round(float(btw), 2)},
        {'total': round(float(total), 2)}
=======
    pdf.cell(30, 15, 'AANTAL', border=0)
    pdf.cell(60, 15, 'OMSCHRIJVING', border=0)
    pdf.cell(60, 15, 'PRIJS PER EENHEID', border=0)
    pdf.cell(50, 15, 'REGELTOTAAL', border=0)
    pdf.ln(7)

    # Iterate over products
    for product in data["order"]["producten"]:
        pdf.cell(30, 15, str(product["aantal"]), border=0)
        pdf.cell(60, 15, product["productnaam"], border=0)
        pdf.cell(60, 15, str(product["prijs_per_stuk_excl_btw"]), border=0)
        pdf.cell(50, 15, str(product["aantal"] * product["prijs_per_stuk_excl_btw"]), border=0)
        pdf.ln(7)

    pdf.ln(15)

    # Create table to check out
    # subtotal = sum(product["prijs_per_stuk_excl_btw"])
    # btw = subtotal / 100 * 21
    # total = (subtotal + btw)


    total_bedrag = [
        {'subtotal': '022'},
        {'BTW': '0'},
        {'total': '0'}
>>>>>>> 0f4d4138c9e4df4c420221f38b27f04e4e04c9f1
    ]

    pdf.set_font('Arial', '', 12)
    for data_row in total_bedrag:
        for datum, value in data_row.items():
<<<<<<< HEAD
            pdf.cell(140, 3, str(datum), border=0, align='R')
            pdf.cell(15, 3, str(value), border=0, ln=True, align='R')
=======
            pdf.cell(170, 3, str(datum), align='R')
            pdf.cell(-165, 3, str(value), ln=True)
>>>>>>> 0f4d4138c9e4df4c420221f38b27f04e4e04c9f1

        pdf.ln()

    # Footer
    pdf.set_y(-15)
<<<<<<< HEAD
    pdf.set_font('Arial', '', 12)
=======
    pdf.set_font('Arial', '', 10)
>>>>>>> 0f4d4138c9e4df4c420221f38b27f04e4e04c9f1
    footer_text = """
    U wordt verzocht het vermelde bedrag binnen 14 dagen over te maken op het onderstaande rekeningnummer.
    Het totaalbedrag dient binnen 14 dagen te worden voldaan.
    Bij achterstallige rekeningen wordt de wettelijk verschuldigde rente in rekening gebracht.
    NL04INGB0101712499 tav O Mothi

<<<<<<< HEAD
                                Wij danken u voor uw vertrouwen in ons.
=======
                                                        Wij danken u voor uw vertrouwen in ons.
>>>>>>> 0f4d4138c9e4df4c420221f38b27f04e4e04c9f1
            """ 
    pdf.multi_cell(0, 5, footer_text, 0, 'L')

    pdf.output(pdf_filename)

with open('test_set_softwareleverancier/2000-018.json') as json_file:
    factuur_data = json.load(json_file)


file_name = 'factuur_form_json1.pdf'
<<<<<<< HEAD
generate_invoices(factuur_data, file_name)
=======
generate_invoices(factuur_data, file_name)
>>>>>>> 0f4d4138c9e4df4c420221f38b27f04e4e04c9f1
