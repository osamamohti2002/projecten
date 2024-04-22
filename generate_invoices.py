from fpdf import FPDF
import json
from math import ceil
 
 
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
    pdf.cell(120, 10, '>> | OM Diensten', ln=True)
    pdf.set_draw_color(0, 0, 0)  # Zwarte kleur
    pdf.set_line_width(0.5)  # Breedte van de lijn
    pdf.line(pdf.get_x(), pdf.get_y(), pdf.get_x() + 120, pdf.get_y())  # Lijn van dezelfde breedte als de tekst
    pdf.ln(10)  # Extra spatiëring na de lijn
 
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'FACTUURNUMMER', ln=1, align='L')
    pdf.set_font('Arial', '', 11)
    pdf.cell(0, 10, data['order']['ordernummer'], ln=1, align='L')
    pdf.ln(-15)
 
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(80, 50, 'Datum', ln=True)
    pdf.ln(-40)
    pdf.set_font('Arial', '', 12)
    pdf.cell(80, 50, data['order']['orderdatum'], ln=True)
 
 
    # Infomatie over de klant
    pdf.ln(5)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(120, 10, 'FACTUUR AAN: ', ln=True)
    pdf.set_font('Arial', '', 11)
    pdf.cell(120, 5, data['order']['klant']['naam'], ln=True)
    pdf.cell(120, 5, data['order']['klant']['adres'], ln=True)
    pdf.cell(120, 5, data['order']['klant']['postcode'], ln=True)
    pdf.cell(120, 5, data['order']['klant']['stad'], ln=True)
    pdf.cell(120, 5, f"KVK-nummer: {data['order']['klant']['KVK-nummer']}", ln=True)
    pdf.cell(120, 5, f"Betaaltermijn {data['order']['betaaltermijn']}", ln=True)
 
 
    # Infomatie over de eigenaar
    pdf.ln(-45)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(180, -120, 'OM Diensten', ln=True, align='R')
    pdf.set_font('Arial', '', 11)
    pdf.cell(180, 135, 'Osama Mohti', ln=1, align='R')
    pdf.cell(180, -120, 'Lindelaan 56', ln=1, align='R')
    pdf.cell(180, 135, '2651 TL, Berkel en Rodenrijd', ln=1, align='R')
    pdf.cell(180, -120, '0618383611', ln=1, align='R')
    pdf.cell(180, 135, 'Oosama.motee@gmail.com', ln=1, align='R')
    pdf.cell(180, -120, 'KVK-nummer: 57689432', align='R')
 
 
 
    # ----------------------------------------------------------------
    pdf.ln(25)
    pdf.set_fill_color(255, 255, 255)
 
    # Information about products
    pdf.set_font('Arial', '', 12)
    pdf.ln(10)
    pdf.cell(30, 15, 'AANTAL', border=0)
    pdf.cell(60, 15, 'OMSCHRIJVING', border=0)
    pdf.cell(60, 15, 'PRIJS PER EENHEID', border=0)
    pdf.cell(50, 15, 'REGELTOTAAL', border=0)
    pdf.ln(7)
 
    # Iterate over products
    subtotal = 0
    for product in data["order"]["producten"]:
        pdf.cell(30, 15, str(product["aantal"]), border=0)
        pdf.cell(60, 15, product["productnaam"], border=0)
        pdf.cell(60, 15, str(product["prijs_per_stuk_excl_btw"]), border=0)
        # pdf.cell(50, 15, str(product["aantal"] * product["prijs_per_stuk_excl_btw"]), border=0)
        pdf.cell(50, 15, str(round(product["aantal"] * product["prijs_per_stuk_excl_btw"], 2)), border=0)

        pdf.ln(7)
        subtotal += product["aantal"] * product["prijs_per_stuk_excl_btw"]
    pdf.ln(15)
 
    btw = subtotal / 100 * 21
    total = (subtotal + btw)
 
 
    total_bedrag = [
        {'subtotal': round(float(subtotal), 2)},
        {'BTW': round(float(btw), 2)},
        {'total': round(float(total), 2)}
    ]
 
    pdf.set_font('Arial', '', 12)
    for data_row in total_bedrag:
        for datum, value in data_row.items():
            pdf.cell(170, 3, str(datum), align='R')
            pdf.cell(-165, 3, str(value), ln=True)
 
        pdf.ln()
 
    # Footer
    pdf.set_y(260)
    pdf.set_font('Arial', '', 10)
    footer_text = """
    U wordt verzocht het vermelde bedrag binnen 14 dagen over te maken op het onderstaande rekeningnummer.
                                                        Wij danken u voor uw vertrouwen in ons.
            """
    pdf.multi_cell(0, 5, footer_text, 0, 'L')
 
    pdf.output(pdf_filename)
 
with open('C:/Users/lithe/OneDrive/school/how_to_make_money/projecten/JSON_IN/2000-474.json') as json_file:
    factuur_data = json.load(json_file)
 
 
file_name = 'factuur_form_json1.pdf'
generate_invoices(factuur_data, file_name)