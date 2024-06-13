import PyPDF2

def extract_text_from_paf(pdf_file: str)->[str]:
    with open(pdf_file, "rb") as pdf:
        reader= PyPDF2.PdfFileReader(pdf, strict=False)
        pdf_text=[]

        for page in reader.pages:
            content=page.extract_text()
            pdf_text.append(content)
        return pdf_text

if __name__=="__main__":
    extract_text=extract_text_from_paf("D:\Pyn\Test_work\Electrol Bond Data\eb_purchase_details.pdf")
    for text in extract_text:
        print(text)