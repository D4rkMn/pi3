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
    
    # Sample text
    text= "Probando texto para el protoboard en Python"
    
    # Format text and covert to braille 
    splitString = TextFormatter.format(text)
    brailleList = BrailleConverter.generateFromList(splitString)

    # Define the ports 
    usbPort = "COM3"
    serialPort = 9600
    
    # Create the output generator
    outputGenerator = OutputGenerator()
    outputGenerator.assignSerialPort(serialPort)
    outputGenerator.assignUsbPort(usbPort)
    
    # Output test
    print(brailleList)
    outputGenerator.generate(brailleList)