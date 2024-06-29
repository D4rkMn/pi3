from Python.TextFormatter import CODE_MAYUS, CODE_NUMBER, PROTOBOARD_SIZE
from Python.Global import Global

from typing import List

"""
    ● ●
    ● o = '111100' (Counting by columns before by rows)
    ● o
"""

SPANISH_TABLE = {
    # special prefixes
    CODE_MAYUS: '000101', # prefix for uppercase letters
    CODE_NUMBER: '001111', # prefix for numbers
    # normal letters
    'a': '100000',
    'b': '110000',
    'c': '100100',
    'd': '100110',
    'e': '100010',
    'f': '110100',
    'g': '110110',
    'h': '110010',
    'i': '010100',
    'j': '010110',
    'k': '101000',
    'l': '111000',
    'm': '101100',
    'n': '101110',
    'o': '101010',
    'p': '111100',
    'q': '111110',
    'r': '111010',
    's': '011100',
    't': '011110',
    'u': '101001',
    'v': '111001',
    'w': '010111',
    'x': '101101',
    'y': '101111',
    'z': '101011',
    # letters with accent
    'á': '111011',
    'é': '011101',
    'í': '001100',
    'ó': '001101',
    'ú': '011111',
    'ü': '110011',
    'ñ': '110111',
    # numbers
    '1': '100000',
    '2': '110000',
    '3': '100100',
    '4': '100110',
    '5': '100010',
    '6': '110100',
    '7': '110110',
    '8': '110010',
    '9': '010100',
    '0': '010110',
    # extra characters
    ' ': '000000', # empty character
    '.': '001000',
    ',': '010000',
    ';': '011000',
    ':': '010010',
    '-': '001001',
    '¿': '010001',
    '?': '010001',
    '¡': '011010',
    '!': '011010',
    '“': '011001',
    '”': '011001',
    '"': '011001',
    '(': '110001',
    ')': '001110',
}

ENGLISH_TABLE = {
    # special prefixes
    CODE_MAYUS: '000101', # prefix for uppercase letters
    CODE_NUMBER: '001111', # prefix for numbers
    # normal letters
    'a': '100000',
    'b': '110000',
    'c': '100100',
    'd': '100110',
    'e': '100010',
    'f': '110100',
    'g': '110110',
    'h': '110010',
    'i': '010100',
    'j': '010110',
    'k': '101000',
    'l': '111000',
    'm': '101100',
    'n': '101110',
    'o': '101010',
    'p': '111100',
    'q': '111110',
    'r': '111010',
    's': '011100',
    't': '011110',
    'u': '101001',
    'v': '111001',
    'w': '010111',
    'x': '101101',
    'y': '101111',
    'z': '101011',
    # numbers
    '1': '100000',
    '2': '110000',
    '3': '100100',
    '4': '100110',
    '5': '100010',
    '6': '110100',
    '7': '110110',
    '8': '110010',
    '9': '010100',
    '0': '010110',
    # extra characters (TODO: change this for english)
    ' ': '000000', # empty character
    '#': '001111',
    '.': '010011',
    ',': '010000',
    ';': '011000',
    ':': '010010',
    '-': '001001',
    '?': '011001',
    '!': '011010',
    '“': '011001',
    '”': '001011',
    '(': '111011',
    ')': '011111',
    "'": '001000'
}

class BrailleConverter:
    """
    BrailleConverter

    Static class that converts given chars and strings into braille characters, represented as strings
    """

    @staticmethod
    def generateFromChar(inputChar : str) -> str:
        """
        Generates a braille char from a given char.

        Args:
            inputChar: String that represents a char to be converted.

        Returns:
            String representing the braille char.
        """

        if Global.getLanguage() == "spanish":
            return SPANISH_TABLE[inputChar]
        
        if Global.getLanguage() == "english":
            return ENGLISH_TABLE[inputChar]

    @staticmethod
    def generateFromString(inputString : str) -> List[str]:
        """
        Generates a braille string from a given string.

        Args:
            inputString: String that represents a string to be converted.

        Returns:
            List of strings representing the braille string.
        """

        result : List[str] = []

        for brailleChar in inputString:
            try: 
                brailleString = BrailleConverter.generateFromChar(brailleChar)
            except:
                brailleString = ["0"*PROTOBOARD_SIZE]
            result.append(brailleString)
        
        return result
    
    @staticmethod
    def generateFromList(inputList : List[str]) -> List[List[str]]:
        """
        Generates a list of braille strings from a given string list.

        Args:
            inputList: List of strings that represents multiple strings to be converted.

        Returns:
            Matrix of strings representing the list of braille strings.
        """

        result : List[List[str]] = []

        for brailleString in inputList:
            brailleList = BrailleConverter.generateFromString(brailleString)
            result.append(brailleList)
        
        return result