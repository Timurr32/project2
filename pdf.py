import os
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 12)
        self.cell(0, 10, 'XYZ Services B.V.', ln=True, align='L')
        self.set_font('helvetica', '', 10)
        self.cell(0, 10, '123, 1234 AB Amsterdam', ln=True, align='L')
        self.cell(0, 10, 'Postcode: 1234 AB', ln=True, align='L')
        self.cell(0, 10, 'BTW-nummer: NL123456789B01', ln=True, align='L')
        self.ln(10)

    def footer(self):
        
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.cell(0, 10, f'Pagina {self.page_no()}', 0, 0, 'C')

    def add_factuurregels(self):
        self.set_font('helvetica', '', 12)
        
        
        self.cell(50, 10, 'Omschrijving', border=1)
        self.cell(30, 10, 'Aantal', border=1)
        self.cell(30, 10, 'Prijs', border=1)
        self.cell(30, 10, 'Totaal', border=1)
        self.ln(10)
        
        
        self.cell(50, 10, '', border=1)
        self.cell(30, 10, '', border=1)
        self.cell(30, 10, '', border=1)
        self.cell(30, 10, '', border=1)
        self.ln(10)
        
        
        self.cell(50, 10, '', border=1)
        self.cell(30, 10, '', border=1)
        self.cell(30, 10, '', border=1)
        self.cell(30, 10, '', border=1)
        self.ln(10)
        
        
        self.cell(50, 10, 'Totaal', border=1)
        self.cell(30, 10, '', border=1)
        self.cell(30, 10, '', border=1)
        self.cell(30, 10, '', border=1)
        self.ln(10)


map_pad = 'PDF_INVOICE'
if not os.path.exists(map_pad):
    os.makedirs(map_pad)


pdf = PDF('P', 'mm', 'letter')
pdf.add_page()


pdf.add_factuurregels()


pdf_output_pad = os.path.join(map_pad, 'jouw_factuur.pdf')
pdf.output(pdf_output_pad)
