from fpdf import FPDF

# create FPDF object
# Loyout ('P', 'L')
# UNit ('mm', 'cm', 'in')
# Format ('A4', 'A3', (default), 'Letter', 'Legal', (100,150))
pdf = FPDF('P', 'mm', 'A4')


# Add a page
pdf.add_page()


# Specify font
pdf.set_font('helvetica', '', 16)


# Add text
# w = width
# h = height
# txt = yout text
# ln (0 False; 1 True - move cursor down to next line)
# border ()


# FActuur, Datum, dag & maand
pdf.set_font('Arial', 'B', 20)
pdf.cell(120, 10, 'FACTUUR', ln=True)
pdf.ln(10)

pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'FACTUURNUMMER', ln=1, align='C')
pdf.cell(0, 10, '20240415', ln=1, align='C')
pdf.ln(-15)

pdf.set_font('Arial', 'B', 16)
pdf.cell(80, 50, 'Datum', ln=True)
pdf.ln(-40)
pdf.set_font('Arial', '', 16)
pdf.cell(80, 50, '15-04-2024', ln=True)


# Infomatie over de klant
pdf.set_font('Arial', 'B', 14)
pdf.cell(120, 10, 'FACTUUR AAN: ', ln=True)
pdf.set_font('Arial', '', 16)
pdf.cell(120, 10, 'Lithe Jnaid', ln=True)
pdf.cell(120, 10, 'Waalstraat 21', ln=True)
pdf.cell(120, 10, '2991 AL, Barendrecht', ln=True)
pdf.cell(120, 10, '0628799719', ln=True)
pdf.cell(120, 10, 'lithejnaid27@gmail.com', ln=True)


# Infomatie over de eigenaar
pdf.ln(-50)
pdf.set_font('Arial', 'B', 14)
pdf.cell(180, -113, 'OM Diensten', ln=True, align='R')
pdf.set_font('Arial', '', 14)
pdf.cell(180, 135, 'Osama Mohti', ln=1, align='R')
pdf.cell(180, -115, 'Lindelaan 56', ln=1, align='R')
pdf.cell(180, 135, '2651 TL, Berkel en Rodenrijd', ln=1, align='R')
pdf.cell(180, -115, '0618383611', ln=1, align='R')
pdf.cell(180, 135, 'Oosama.motee@gmail.com', ln=1, align='R')



pdf.ln(110)
pdf.set_font('helvetica', 'I', 10)
pdf.cell(0, 10, 'Wij bedanken u voor uw vertrouwen in ons', align='C')


pdf.output('pdf_testzelf.pdf')

