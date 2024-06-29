from Python.TextExtractorFactory import TextExtractorFactory
from Python.TextFormatter import TextFormatter
from Python.BrailleConverter import BrailleConverter
def procesarArchivo(archivoLocation):
    pdfLocation = archivoLocation

    # Ejemplo de Pdf:
    extractor = TextExtractorFactory.create("Pdf")
    extractor.assign(pdfLocation)

    # Probando con un texto mas pequeño para el ESP32
    text = "Probando texto AAAA para el protoboard en Python"

    # Le damos el formato adecuado al texto
    splitString = TextFormatter.format(text)

    # Convertimos el texto formateado a Brail   le y lo imprimimos
    brailleList = BrailleConverter.generateFromList(splitString)
    guardarArchivo(brailleList)

def guardarArchivo(brailleList,filename= 'resultados.py'):
    with open(filename,'w') as f:
        f.write(f"brailleList = {brailleList}")




