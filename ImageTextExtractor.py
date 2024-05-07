from iSourceTextExtractor import iSourceTextExtractor

import pytesseract
from PIL import Image

class ImageTextExtractor(iSourceTextExtractor):
    """
    ImageTextExtractor

    Class that contains methods to extract text from images as source.
    """

    def __init__(self):
        self.image : Image = None

    def assign(self, sourceString: str) -> None:
        self.image = Image.open(sourceString)
        
    def extract(self) -> str:
        text : str = pytesseract.image_to_string(self.image)
        return text