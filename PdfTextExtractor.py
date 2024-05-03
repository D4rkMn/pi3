from iSourceTextExtractor import iSourceTextExtractor
import PyPDF2
class PdfTextExtractor(iSourceTextExtractor):
    """
    PdfTextExtractor

    Class that contains methods to extract text from Pdfs as source.
    """

    def __init__(self):
        self.pdf = PyPDF2
        pass

    def assign(self,sourceString: str) -> None:
        self.pdf = self.pdf.PdfReader(sourceString)
        pass
        
    def extract(self) -> str:
        AllText = ""
        for PagePdf in range (len(self.pdf.pages)):
            Page = self.pdf.pages[PagePdf]
            AllText += Page.extract_text()
        return AllText