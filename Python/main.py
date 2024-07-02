import sys
from TextExtractorFactory import TextExtractorFactory
from TextFormatter import TextFormatter
from BrailleConverter import BrailleConverter
from OutputGenerator import OutputGenerator

# este main es para testear y debugear. usenlo como sea necesario
if __name__ == "__main__":

    # # Ejemplo de imagen válida:
    # imageLocation = "Input/imagen_valida.png"
    # imageExtractor = TextExtractorFactory.create("Image")
    # imageExtractor.assign(imageLocation)
    # imageValidText = imageExtractor.extract()

    # # Ejemplo de imagen inválida:
    # try:
    #     imageLocation = "Input/imagen_invalida.jpg"
    #     imageExtractor.assign(imageLocation)
    #     imageInvalidText = imageExtractor.extract()
    # except ValueError as e:
    #     print(f"Error: {e}")

    # Ejemplo de Pdf:
    if(len(sys.argv)!=2):
        print("Fue ps")
        sys.exit(1)
    
    pdfLocation = sys.argv[1]
    extractor = TextExtractorFactory.create("Pdf")
    extractor.assign(pdfLocation)
    pdfText = extractor.extract()
    # Outputeamos el texto en el archivo "test.txt"
    with open("test.txt", "w") as f:
        #f.write(imageValidText)
        #f.write("\n\n")
        f.write(pdfText)

    # input("Output en test.txt.\nPresione enter para continuar...")

    # Probando con un texto mas pequeño para el ESP32
    text = pdfText
    text = "Probando texto AAAA para el protoboard en Python"

    # Le damos el formato adecuado al texto
    splitString = TextFormatter.format(text)
    # Imprimos el string formateada para probar su funcionamiento correcto
    # for string in splitString:
    #     print(string)
    # print()

    # input("Presione enter para continuar...")

    # Convertimos el texto formateado a Braille y lo imprimimos
    brailleList = BrailleConverter.generateFromList(splitString)
    print(brailleList)

    # input("Presione enter para continuar...")

    # # Definimos los puertos para la placa 
    # usbPort = "COM3"
    # serialPort = 9600
    
    # # Creamos el output generator
    # outputGenerator = OutputGenerator()
    # outputGenerator.assignSerialPort(serialPort)
    # outputGenerator.assignUsbPort(usbPort)
    
    # # Output test
    # outputGenerator.generate(brailleList)