import os
import json
from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, factuur_data):
        super().__init__()
        self.factuur_data = factuur_data  # JSON-data opslaan in object

    def header(self):
        bedrijf = self.factuur_data.get("bedrijf", {})
        
        self.set_font('helvetica', 'B', 12)
        self.cell(0, 10, bedrijf.get("naam", "Bedrijfsnaam"), ln=True, align='L')
        self.set_font('helvetica', '', 10)
        self.cell(0, 10, bedrijf.get("adres", "Adres onbekend"), ln=True, align='L')
        self.cell(0, 10, f'Postcode: {bedrijf.get("postcode", "Onbekend")}', ln=True, align='L')
        self.cell(0, 10, f'BTW-nummer: {bedrijf.get("btw_nummer", "Onbekend")}', ln=True, align='L')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.cell(0, 10, f'Pagina {self.page_no()}', 0, 0, 'C')

    def add_factuurregels(self):
        self.set_font('helvetica', 'B', 12)
        self.cell(50, 10, 'Omschrijving', border=1)
        self.cell(30, 10, 'Aantal', border=1)
        self.cell(30, 10, 'Prijs', border=1)
        self.cell(30, 10, 'Totaal', border=1)
        self.ln(10)

        # Factuurregels uit JSON halen
        self.set_font('helvetica', '', 12)
        totaal = 0
        for item in self.factuur_data.get("items", []):
            omschrijving = item.get("omschrijving", "")
            aantal = item.get("aantal", 0)
            prijs = item.get("prijs", 0.0)
            totaal_item = aantal * prijs
            totaal += totaal_item

            self.cell(50, 10, omschrijving, border=1)
            self.cell(30, 10, str(aantal), border=1)
            self.cell(30, 10, f"€ {prijs:.2f}", border=1)
            self.cell(30, 10, f"€ {totaal_item:.2f}", border=1)
            self.ln(10)

        # Totaal weergeven
        self.cell(110, 10, "Totaal", border=1)
        self.cell(30, 10, f"€ {totaal:.2f}", border=1)
        self.ln(10)

# 1. JSON-bestand inlezen
json_pad = 'factuur.json'
if not os.path.exists(json_pad):
    print(f"Fout: Het JSON-bestand '{json_pad}' bestaat niet.")
    exit()

with open(json_pad, 'r') as f:
    factuur_data = json.load(f)

# 2. Map maken voor de PDF
map_pad = 'PDF_INVOICE'
if not os.path.exists(map_pad):
    os.makedirs(map_pad)

# 3. PDF genereren
pdf = PDF(factuur_data)
pdf.add_page()
pdf.add_factuurregels()

# 4. PDF opslaan
pdf_output_pad = os.path.join(map_pad, 'jouw_factuur.pdf')
pdf.output(pdf_output_pad)
print(f'Factuur opgeslagen als: {pdf_output_pad}')

