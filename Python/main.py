from TextExtractorFactory import TextExtractorFactory
from TextFormatter import TextFormatter
from BrailleConverter import BrailleConverter
from OutputGenerator import OutputGenerator

# este main es para testear y debugear. usenlo como sea necesario
if __name__ == "__main__":

    # Ejemplo de imagen válida:
    imageLocation = "Input/imagen_valida.png"
    imageExtractor = TextExtractorFactory.create("Image")
    imageExtractor.assign(imageLocation)
    imageValidText = imageExtractor.extract()

    # Ejemplo de imagen inválida:
    try:
        imageLocation = "Input/imagen_invalida.jpg"
        imageExtractor.assign(imageLocation)
        imageInvalidText = imageExtractor.extract()
    except ValueError as e:
        print(f"Error: {e}")

    # Ejemplo de Pdf:
    pdfLocation = "Input/pdf.pdf"
    extractor = TextExtractorFactory.create("Pdf")
    extractor.assign(pdfLocation)
    pdfText = extractor.extract()

    # Outputeamos el texto en el archivo "test.txt"
    with open("test.txt", "w") as f:
        f.write(imageValidText)
        f.write("\n\n")
        f.write(pdfText)

    # Probando con un texto mas pequeño para el ESP32
    text = "Probando texto para el protoboard en Python"
    
    # Formateamos el texto y lo covertimos a Braille 
    splitString = TextFormatter.format(text)
    brailleList = BrailleConverter.generateFromList(splitString)

    # Definimos los puertos para la placa 
    usbPort = "COM3"
    serialPort = 9600
    
    # Creamos el output generator
    outputGenerator = OutputGenerator()
    outputGenerator.assignSerialPort(serialPort)
    outputGenerator.assignUsbPort(usbPort)
    
    # Output test
    print(brailleList)
    outputGenerator.generate(brailleList)