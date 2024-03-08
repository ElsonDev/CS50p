from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "", 28)
        self.cell(text="CS50 Shirtificate", border=0, align="C", center=True)


def main():
    name = input("Name: ")
    pdf = PDF()
    pdf.add_page()
    pdf.image("shirtificate.png", x="C", y=60, w=180)
    pdf.set_font("helvetica", "", 18,)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 220, text=f"{name} took CS50", border=0, align="C", center=True)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
