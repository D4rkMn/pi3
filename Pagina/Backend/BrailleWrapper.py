from Python.TextExtractorFactory import TextExtractorFactory
from Python.TextFormatter import TextFormatter
from Python.BrailleConverter import BrailleConverter
import sys
sys.path.append('../../')
def procesarArchivo(archivoLocation):
    fileLocation = archivoLocation
    isPdf = fileLocation.endswith('.pdf')
    print("Que es?: " + str(isPdf))
    if(isPdf):
    # Ejemplo de Pdf:
        fileExtractor = TextExtractorFactory.create("Pdf")
    else:
    # Ejemplo de Imagen:
        fileExtractor = TextExtractorFactory.create("Image")
    fileExtractor.assign(fileLocation)
    # Probando con un texto mas pequeño para el ESP32

    text = fileExtractor.extract()
    # Le damos el formato adecuado al texto
    splitString = TextFormatter.format(text)

    # Convertimos el texto formateado a Brail   le y lo imprimimos
    brailleList = BrailleConverter.generateFromList(splitString)
    guardarArchivo(brailleList)

def guardarArchivo(brailleList,filename= 'resultados.py'):
    with open(filename,'w') as f:
        f.write(f"brailleList = {brailleList}")




