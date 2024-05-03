from typing import List

from TextExtractorFactory import TextExtractorFactory
from BrailleConverter import BrailleConverter

# Use these like:
#
# textExtractor = TextExtractorFactory.create("Image")
# textExtractor.assign("abc")
# text = textExtractor.extract()
# brailleList = BrailleConverter.generateFromString(text)

class BrailleFileGenerator:
    """
    BrailleFileGenerator

    Static class that generates text files containing the given braille integers
    """

    @staticmethod
    def generateFromList(brailleList : List[int]) -> None:
        """
        Generates a text file from a given integer list.

        Args:
            brailleList: List of ints representing the braille characters
        """

        # TODO: Implement.
        pass