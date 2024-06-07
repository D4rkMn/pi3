from iSourceTextExtractor import iSourceTextExtractor
from ImageTextExtractor import ImageTextExtractor
from PdfTextExtractor import PdfTextExtractor

class TextExtractorFactory:
    """
    TextExtractorFactory

    Static class that creates text extractors.
    """

    @staticmethod
    def create(extractProvider : str) -> iSourceTextExtractor:
        """
        Creates a text extractor from a given provider string.

        Args:
            extractProvider: String to identify the type of provider to be created (Image or Pdf). 
        
        Returns:
            The created text extractor.
        """
        
        if extractProvider == "Image":
            return ImageTextExtractor()
        if extractProvider == "Pdf":
            return PdfTextExtractor()