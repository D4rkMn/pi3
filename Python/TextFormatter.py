from typing import List
from pyphen import Pyphen
import re

# Number of Braille Characters to display on the protobard
PROTOBOARD_SIZE = 6
# Prefix for uppercase characters
CODE_MAYUS = "֍"
# Prefix for numerical character
CODE_NUMBER = "߷"

pyphenInstance = Pyphen(lang = "es")

class TextFormatter:
    """
    TextFormatter

    Static class that converts given strings into the correct format for the braille device. 
    """

    @staticmethod
    def __formatWordString(text : str) -> List[str]:
        syllableOfText = text
        if((text!="--") & (text != "-")):
            textWitHyphen = pyphenInstance.inserted(text,'-')
            syllableOfText = textWitHyphen.split('-')
        return syllableOfText

    @staticmethod
    def __formatNumberString(text : str) -> List[str]:
        result = [digit for digit in text]
        return result

    @staticmethod
    def __splitInSyllables(text : str) -> List[str]:
        substrings = re.findall(r'[a-zA-Z]+|\d+|[-...,¡!¿?>==<{}"()\[\]]+', text)
        result = []
        for substring in substrings:
            splitSubstring = None

            if substring.isnumeric():
                splitSubstring = TextFormatter.__formatNumberString(substring)

            else:
                splitSubstring = TextFormatter.__formatWordString(substring)

            result.extend(splitSubstring)

        return result

    @staticmethod
    def __emergencySplit(string : str) -> List[str]:
        result = []
        for i in range(0,len(string),PROTOBOARD_SIZE - 1):
            substring = string[i: i + PROTOBOARD_SIZE - 1]
            if(len(string) >= (PROTOBOARD_SIZE + i)):
                substring += "-"
            result.append(substring)
        
            if(len(string) >= (PROTOBOARD_SIZE + i)):
                substring += "-"
            result.append(substring)
        
        return result

    @staticmethod
    def __preProcess(text: str) -> str:
        text = text.replace(CODE_MAYUS,"")
        text = text.replace(CODE_NUMBER, "")
        text= re.sub(r'(?<!-)-(?!-)',"",text)
        return text

    @staticmethod
    def __encodeFormatProtoboard(text: List[str]) -> List[str]:
        encodeText = []
        print("pre: " + str(text))
        for line in text:
            encodeLine = ""
            if not line:
                continue
            if not line:
                continue
            for character in line: 
                if (character.isupper()):
                    encodeLine += CODE_MAYUS + character.lower()

                elif(character.isdigit()):
                    encodeLine += CODE_NUMBER + character

                else:
                    encodeLine += character
            if len(encodeLine) > PROTOBOARD_SIZE:
                emergencyLines = TextFormatter.__emergencySplit(encodeLine)
                encodeText.extend(emergencyLines)            
            else:
                encodeText.append(encodeLine)

        return encodeText
    
    def __formatProtoboard(text: List[str], brailleType: List[List[int]]) -> List[str]:
        indexProtoboardSize = 0
        TextLine = ""
        for i in range (len(text)):
            wordSize = len(text[i])
            wordSize += brailleType[i][0]
            wordSize += brailleType[i][1] 
            if(indexProtoboardSize + wordSize <= PROTOBOARD_SIZE):
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
                    specialChar = syllableOfText[j] in ['.', ',', '!', '?', ';' , ':', '}', ')', ']', '>', '-', '"', "'"]
                    wordSize = sum(1 for caracter in syllableOfText[j] if caracter.isupper())
                    if(syllableOfText[j].isdigit()):
                        wordSize = 1
                        
                    if((wordSize + indexProtoboardSize + len(syllableOfText[j]) <= PROTOBOARD_SIZE - 1) | (specialChar & (indexProtoboardSize + 1 <= PROTOBOARD_SIZE))):
                        indexProtoboardSize += len(syllableOfText[j]) + wordSize

                    elif(j==0):
                        TextLine +='\n'
                        indexProtoboardSize = len(syllableOfText[j]) + wordSize

                    else:
                        TextLine += '-'
                        TextLine += '\n'
                        indexProtoboardSize = ((len(syllableOfText[j]))) + wordSize
                    TextLine += syllableOfText[j]
                
                if(indexProtoboardSize < PROTOBOARD_SIZE):
                    TextLine += " "
                    indexProtoboardSize += 1
        totalText = TextLine.splitlines()
        return totalText
                        
    @staticmethod
    def format(text : str) -> str:
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
            brailleType[i][1] += digitInWord  
        protoboardText = TextFormatter.__formatProtoboard(textSplit,brailleType)
        brailleConverterText = TextFormatter.__encodeFormatProtoboard(protoboardText)
        for i in range(len(brailleConverterText)):
            indexMaxRange = len(brailleConverterText[i])
            while(indexMaxRange<PROTOBOARD_SIZE):
                brailleConverterText[i]+=" "
                indexMaxRange+=1
        return (brailleConverterText)
    
    