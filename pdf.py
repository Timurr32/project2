import os
from fpdf import FPDF


map_pad = 'PDF_INVOICE'
if not os.path.exists(map_pad):
    os.makedirs(map_pad)

pdf = FPDF('P', 'mm', 'letter')
pdf.add_page()
pdf.set_font('helvetica', '', 16)

gebruiker = input("Voer de tekst in die je aan de PDF wilt toevoegen: ")
pdf.cell(40, 10, gebruiker)


pdf_output_pad = os.path.join(map_pad, 'opdrachttt3.pdf')
pdf.output(pdf_output_pad)
