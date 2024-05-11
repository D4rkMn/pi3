from iSourceTextExtractor import iSourceTextExtractor
from PyPDF2 import PdfReader
import re
class PdfTextExtractor(iSourceTextExtractor):
    """
    PdfTextExtractor

    Class that contains methods to extract text from Pdfs as source.
    """

    def __init__(self):
        self.pdf : PdfReader = None
        pass

    def assign(self, sourceString: str) -> None:
        self.pdf = PdfReader(sourceString)
        pass
        
    def extract(self) -> str:
        AllText = ""
        for PagePdf in range (len(self.pdf.pages)):
            Page = self.pdf.pages[PagePdf]
            TextWithLineBreaks = Page.extract_text() 
            AllText += re.sub(r'\n',' ', TextWithLineBreaks)
        return AllText