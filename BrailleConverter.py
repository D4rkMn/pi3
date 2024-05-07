from typing import List

class BrailleConverter:
    """
    BrailleConverter

    Static class that converts given chars and strings into braille characters, represented as ints
    """

    @staticmethod
    def generateFromChar(inputChar : str) -> int:
        """
        Generates a braille int from a given char.

        Args:
            inputChar: String that represents a char to be converted.

        Returns:
            Integer representing the braille value.
        """

        # TODO: Implement.
        
        pass

    @staticmethod
    def generateFromString(inputString : str) -> List[int]:
        """
        Generates a braille int from a given string.

        Args:
            inputChar: String that represents a string to be converted.

        Returns:
            List of integers representing the braille values.
        """

        result : List[int] = []

        for char in inputString:
            brailleInt : int = BrailleConverter.generateFromChar(char)
            result.append(brailleInt)
        
        return result