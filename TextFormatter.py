from typing import List,Tuple
from pyphen import Pyphen
import re

CODE_MAYUS = "֍"
CODE_NUMBER = "߷"
PROTOBOARD_SIZE = 10

pyphenInstance = Pyphen(lang = "es")


class TextFormatter:
    """
    TextFormatter

    Static class that converts given strings into the correct format for the braille device. 
    """

    @staticmethod
    def setLanguage(lang : str) -> None:
        pyphenInstance = Pyphen(lang = lang)

    @staticmethod
    def __formatWordString(text : str) -> List[str]:
        textWitHyphen = pyphenInstance.inserted(text,'-')
        syllableOfText = textWitHyphen.split('-')
        return syllableOfText

    @staticmethod
    def __formatNumberString(text : str) -> List[str]:
        result = [digit for digit in text]
        return result

    @staticmethod
    def __splitInSyllables(text : str) -> List[str]:
        substrings : List[str] = re.findall(r'[a-zA-Z]+|\d+|[.,!?]+', text)
        result = []

        for substring in substrings:
            temp = None

            if substring.isnumeric():
                temp = TextFormatter.__formatNumberString(substring)

            else:
                temp = TextFormatter.__formatWordString(substring)

            result.extend(temp)

        print(f"split string: {result}")

        return result

    @staticmethod
    def __preProcess(text: str) -> str:
        for word in text:
            text = text.replace(CODE_MAYUS,"")
            text = text.replace(CODE_NUMBER, "")
        return text

    @staticmethod
    def __formatProtoboard(text: List[str], brailleType: List[List[int]]) -> List[str]:
        totalText = []
        indexProtoboardSize = 0
        TextLine = ""
        for i in range (len(text)):
            wordSize = len(text[i])
            wordSize += brailleType[i][0]
            wordSize += brailleType[i][1] 
            print("Parte normal: " + text[i] + " index: " + str(indexProtoboardSize) + " extra: " + str(brailleType[i][1]))
            if(indexProtoboardSize + wordSize <= PROTOBOARD_SIZE - 1):
                indexProtoboardSize += wordSize
                TextLine += text[i]
                if(indexProtoboardSize < PROTOBOARD_SIZE - 1):
                    TextLine += " "
                    indexProtoboardSize += 1
                else: 
                    TextLine += '\n' 
                    indexProtoboardSize = 0
            else:
                syllableOfText = TextFormatter.__splitInSyllables(text[i])
                for j in range (len(syllableOfText)):
                    #ayuda
                    wordSize = sum(1 for caracter in syllableOfText[j] if caracter.isupper())
                    if(syllableOfText[j].isdigit()):
                        wordSize = 1
                    if(wordSize + indexProtoboardSize + len(syllableOfText[j]) <= PROTOBOARD_SIZE - 2):
                        TextLine += syllableOfText[j]
                        indexProtoboardSize += len(syllableOfText[j]) + wordSize
                    elif(j==0):
                        TextLine +='\n'
                        TextLine += syllableOfText[j]
                        indexProtoboardSize = len(syllableOfText[j]) + wordSize
                    else:
                        TextLine += '-'
                        TextLine += '\n'
                        TextLine += syllableOfText[j]
                        indexProtoboardSize = ((len(syllableOfText[j]))) + wordSize
                    print("parte no normal: " + syllableOfText[j]  + " num: " + str(brailleType[i][1]) + " index: " + str(indexProtoboardSize) )
                if(indexProtoboardSize < PROTOBOARD_SIZE - 1):
                    TextLine += " "
                    print("index + 1")
                    indexProtoboardSize += 1
                indexProtoboardSize %= (PROTOBOARD_SIZE)
                print("indice: "+ str(indexProtoboardSize) + " silaba: " + syllableOfText[j])
        print(TextLine)
                        


    @staticmethod
    def format(text : str) -> Tuple[ List[str], List[List[int]]]:
        """
        Formats the given string for the braille device.

        Args:
            text: String to be formatted
        
        Returns:
            An array of strings representing the formatted text
        """
        text = TextFormatter.__preProcess(text)
        textSplit = text.split()
        
        brailleType = [[0] * 2 for _ in range (len(textSplit)) ]
                  
        for i in range(len(textSplit)):
            digitInWord = sum(1 for caracter in textSplit[i] if caracter.isdigit())
            MayusInWord = sum(1 for caracter in textSplit[i] if caracter.isupper())
            brailleType[i][0] += MayusInWord
            brailleType[i][1] += digitInWord   
        TextComplete = TextFormatter.__formatProtoboard(textSplit,brailleType)
        return (textSplit,brailleType)
    