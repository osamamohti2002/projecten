from fpdf import FPDF

# create FPDF object



def generate_invoices(data):
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
    pdf.cell(0, 10, '20240415', ln=1, align='L')
    pdf.ln(-15)

    pdf.set_font('Arial', 'B', 12)
    pdf.cell(80, 50, 'Datum', ln=True)
    pdf.ln(-40)
    pdf.set_font('Arial', '', 12)
    pdf.cell(80, 50, '15-04-2024', ln=True)


    # Infomatie over de klant
    pdf.ln(-10)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(120, 10, 'FACTUUR AAN: ', ln=True)
    pdf.set_font('Arial', '', 11)
    pdf.cell(120, 5, 'Lithe Jnaid', ln=True)
    pdf.cell(120, 5, 'Waalstraat 21', ln=True)
    pdf.cell(120, 5, '2991 AL, Barendrecht', ln=True)
    pdf.cell(120, 5, '0628799719', ln=True)
    pdf.cell(120, 5, 'lithejnaid27@gmail.com', ln=True)
    pdf.cell(120, 5, 'Betaaltermijn 30 dagen', ln=True)


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

    pdf.set_fill_color(255, 255, 255)




    # information about products
    TABLE_DATA = (
        ("AANTAL", "OMSCHRIJVING", "PRIJS PER EENHEID", "REGELTOTAAL"),
        ("5", "MOUSE", "$8,99", "$44,95")

    )


    # create table
    pdf.set_font('Arial', '', 12)
    pdf.ln(10)
    for data_row in TABLE_DATA:
        for data in data_row:
            pdf.cell(50, 15, data, border=0)
        pdf.ln(7)

    pdf.ln(10)


    # create table to chek out
    total_bedrag = [
        {'subtotal': '0'},
        {'BTW': '0'},
        {'total': '0'}
    ]

    pdf.set_font('Arial', '',12)
    for data_row in total_bedrag:
        for datum, value in data_row.items():
            pdf.cell(140, 3, str(datum), border=0, align='R')
            pdf.cell(15, 3, str(value), border=0, ln=True, align='R')

        pdf.ln()






    # footer
    pdf.set_y(-15)
    pdf.set_font('Arial', '', 12)
    footer_text = """
    U wordt verzocht het vermelde bedrag binnen 14 dagen over te maken op het onderstaande rekeningnummer.
    Het totaalbedrag dient binnen 14 dagen te worden voldaan.
    Bij achterstallige rekeningen wordt de wettelijk verschuldigde rente in rekening gebracht.
    NL04INGB0101712499 tav O Mothi

                                Wij danken u voor uw vertrouwen in ons.
            """ 
    pdf.multi_cell(0, 5, footer_text, 0, 'L')

    # pdf.ln(110)
    # pdf.set_font('helvetica', 'I', 10)
    # pdf.cell(0, 10, 'Wij bedanken u voor uw vertrouwen in ons', align='C')


    pdf.output('pdf_testzelf.pdf')