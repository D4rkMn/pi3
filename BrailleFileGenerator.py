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

    Static class that generates text files containing the given braille strings
    """

    @staticmethod
    def generate(brailleList : List[List[str]]) -> None:
        """
        Generates a text file from a given list of braille strings.

        Args:
            brailleList: Matrix of strings representing the list of braille strings.
        """

        with open("BrailleFile.txt","w") as f:
            for brailleString in brailleList:
                for brailleChar in brailleString:
                    f.write(brailleChar)
                    f.write("\n")