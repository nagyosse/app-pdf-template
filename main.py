from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 22, 200, 22)
"""
pdf.add_page()

pdf.set_font(family="times", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hello there!", align="L", ln=1, border=1)
pdf.set_font(family="times", style="B", size=10)
pdf.cell(w=0, h=12, txt="Hi there!", align="L", ln=1, border=1)
"""
pdf.output("output.pdf")
