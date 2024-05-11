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
        substrings : List[str] = re.findall(r'[a-zA-Z]+|\d+', text)
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
            if(brailleType[i][0]): wordSize += brailleType[i][0]
            if(brailleType[i][1] > 0): wordSize += brailleType[i][1]
            if(indexProtoboardSize + wordSize <= PROTOBOARD_SIZE - 1):
                indexProtoboardSize += wordSize
                TextLine += text[i]
                print("Parte normal: " + text[i] + " index: " + str(indexProtoboardSize))
                if(indexProtoboardSize < PROTOBOARD_SIZE - 1):
                    TextLine += " "
                    indexProtoboardSize += 1
                else: 
                    TextLine += '\n' 
                    indexProtoboardSize = 0
            else:
                syllableOfText = TextFormatter.__splitInSyllables(text[i])
                print(syllableOfText)
                
                for j in range (len(syllableOfText)):
                    #ayuda
                    MayusSyllable = sum(1 for caracter in syllableOfText[j] if caracter.isupper())
                    if(MayusSyllable + indexProtoboardSize + len(syllableOfText[j]) <= PROTOBOARD_SIZE - 2):
                        TextLine += syllableOfText[j]
                        indexProtoboardSize += len(syllableOfText[j]) + MayusSyllable
                        indexProtoboardSize %= (PROTOBOARD_SIZE - 1)
                    elif(j==0):
                        TextLine +='\n'
                        TextLine += syllableOfText[j]
                        indexProtoboardSize = len(syllableOfText[j]) + MayusSyllable
                    else:
                        TextLine += '-'
                        TextLine += '\n'
                        TextLine += syllableOfText[j]
                        indexProtoboardSize += (1 + (len(syllableOfText[j]))) + MayusSyllable
                        indexProtoboardSize %= (PROTOBOARD_SIZE - 1)
                    print("Mayus: " + str(MayusSyllable))
                if(indexProtoboardSize + MayusSyllable < PROTOBOARD_SIZE - 1):
                    TextLine += " "
                    indexProtoboardSize +=1
                indexProtoboardSize %= (PROTOBOARD_SIZE - 1)
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
            try:
                decimalText = float(textSplit[i])
                decimalTextBool = True
            except:
                decimalTextBool = False
            digitInWord = sum(1 for caracter in textSplit[i] if caracter.isdigit())
            MayusInWord = sum(1 for caracter in textSplit[i] if caracter.isupper())
            if(MayusInWord>0):
                brailleType[i][0] += MayusInWord
            if(textSplit[i].isdigit() | decimalTextBool):
                brailleType[i][1] += digitInWord   
        TextComplete = TextFormatter.__formatProtoboard(textSplit,brailleType)
        return (textSplit,brailleType)
    