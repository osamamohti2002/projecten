from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Mijn Tabel zonder Randen', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Pagina {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_table(self, header, data):
        # Header
        for col in header:
            self.cell(40, 7, col, 0, 0, 'C')
        self.ln()
        # Data
        for row in data:
            for col in row:
                self.cell(40, 6, str(col), 0, 0, 'C')
            self.ln()

pdf = PDF()
pdf.add_page()
pdf.chapter_title('Voorbeeld van een Tabel zonder Randen')
pdf.chapter_body('Dit is een voorbeeld van een tabel zonder randen.')
header = ['Naam', 'Leeftijd', 'Stad']
data = [
    ['John Doe', 30, 'New York'],
    ['Jane Smith', 25, 'Los Angeles'],
    ['Bob Johnson', 40, 'Chicago']
]
pdf.add_table(header, data)
pdf.output('tabel_zonder_randen.pdf')
