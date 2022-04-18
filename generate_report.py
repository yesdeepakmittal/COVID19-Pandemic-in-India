from fpdf import FPDF
WIDTH = 210
HEIGHT = 297

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 24)
pdf.image('img/india.png',x=30,h=80,)
pdf.ln(50)

pdf.write(5, f"Impact of Covid19 in India")
pdf.ln(13)
pdf.set_font('Times', 'I', 16)
pdf.write(1, f"Graphical Report designed using Python by ")
pdf.cell(w=0,txt='Deepak Mittal',align='L',link='https://github.com/yesdeepakmittal/')


pdf.add_page()
pdf.image('img/1.png',10,30,WIDTH)

pdf.add_page()
pdf.image('img/2.png',7,30,WIDTH-10)

pdf.add_page()
pdf.image('img/3.png',7,10,WIDTH-10)

# pdf.add_page()
pdf.image('img/4.png',7,HEIGHT/2+10,WIDTH-10)

pdf.add_page()
pdf.image('img/5.png',7,5,WIDTH-10)

# pdf.add_page()
pdf.image('img/6.png',7,int(HEIGHT/3),WIDTH-10)

# pdf.add_page()
pdf.image('img/7.png',7,int(2*HEIGHT/3),WIDTH-10)

pdf.add_page()
pdf.image('img/8.png',10,30,WIDTH-10)

# pdf.add_page()
pdf.image('img/9.png',10,HEIGHT/2,WIDTH-10)

pdf.add_page()
pdf.image('img/10.png',10,30,WIDTH-10)

# pdf.add_page()
pdf.image('img/11.png',10,HEIGHT/2,WIDTH-10)


pdf.output('report.pdf', 'F')