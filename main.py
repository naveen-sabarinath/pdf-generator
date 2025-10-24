from fpdf import FPDF
import pandas as pd
pdf = FPDF(orientation="p",unit="mm",format="a4")
data = pd.read_csv("topics.csv")
pdf.set_auto_page_break(auto=False,margin=0)
for i,row in data.iterrows():
    # header of the file
    pdf.add_page()
    pdf.set_font(family="Times",style="B",size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12,txt=row["Topic"],align="L",ln=1)
    pdf.line(10,21,200,21)
    for __ in range(10):
        pdf.ln(25)
        pdf.line(10,21,200,21)


    #footer fo this page
    pdf.ln(260)
    pdf.set_font(family="times",style="I",size=15)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=12,txt= row["Topic"],align="R")


    for __ in range(row["Pages"]-1):
        pdf.add_page()
    #footer fo this page
        pdf.ln(272)
        pdf.set_font(family="times",style="I",size=15)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0,h=12,txt= row["Topic"],align="R")

pdf.output("output.pdf")


