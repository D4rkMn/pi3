from TextExtractorFactory import TextExtractorFactory
from TextFormatter import TextFormatter
from BrailleConverter import BrailleConverter
from OutputGenerator import OutputGenerator

# este main es para testear y debugear. usenlo como sea necesario
if __name__ == "__main__":

    # Pdf Case:
    #sourceString = "Empresa.pdf"
    #extractor = TextExtractorFactory.create("Pdf")
    #extractor.assign(sourceString)
    #text = extractor.extract()

    # Write Pdf text to "test.txt"
    #f = open("test.txt","w")
    #f.write(text)
    #f.close()
    
    text= "Probando texto para el protoboard en Python"
    # Convert to braille and store output in "BrailleFile.txt"
    splitString = TextFormatter.format(text)
    
    brailleList = BrailleConverter.generateFromList(splitString)

    usbPort = "COM3"
    serialPort = 9600
    outputGenerator = OutputGenerator()
    outputGenerator.assignSerialPort(serialPort)
    outputGenerator.assignUsbPort(usbPort)
    
    outputGenerator.generate(brailleList)