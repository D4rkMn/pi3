from TextExtractorFactory import TextExtractorFactory
from TextFormatter import TextFormatter
from BrailleConverter import BrailleConverter
from BrailleFileGenerator import BrailleFileGenerator

# este main es para testear y debugear. usenlo como sea necesario
if __name__ == "__main__":

    # Pdf Case:
    sourceString = "Empresa.pdf"
    extractor = TextExtractorFactory.create("Pdf")
    extractor.assign(sourceString)
    text = extractor.extract()

    # Write Pdf text to "test.txt"
    f = open("test.txt","w")
    f.write(text)
    f.close()
    text= "Probando texto para el protoboard en Python"
    # Convert to braille and store output in "BrailleFile.txt"
    splitString = TextFormatter.format(text)
    
    for string in splitString:
        print(f"{string}")
    print()
    
    brailleList = BrailleConverter.generateFromList(splitString)
    BrailleFileGenerator.generate(brailleList)
