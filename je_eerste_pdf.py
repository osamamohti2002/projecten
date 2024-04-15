from fpdf import FPDF

# Maak een FPDF-object aan
pdf = FPDF('P', 'mm', 'Letter')
pdf.add_page()

# Vraag de gebruiker om invoer
user_input = input("Voer de tekst in die je wilt toevoegen aan het PDF-bestand: ")

# Voeg de ingevoerde tekst toe aan het PDF-bestand
pdf.set_font('helvetica', '', 16)
pdf.cell(40, 10, user_input)

# Sla het PDF-bestand op
pdf.output('pdf_1.pdf')
