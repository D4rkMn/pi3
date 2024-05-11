from TextExtractorFactory import TextExtractorFactory
from TextFormatter import TextFormatter
# este main es para testear y debugear. usenlo como sea necesario
if __name__ == "__main__":

    # TODO: fix this test case
    string = "Probando, aca, un, texto, en, maximo, 10, caracteres, palabra233, si, 434343"
    test = TextFormatter.format(string)
    print(test)

    exit()

    with open("test.txt", "w") as f:

        # Image Case:
        sourceString = "strassen.jpg"
        #sourceString = "b.jpg" # ejemplo de imagen invalida
        extractor = TextExtractorFactory.create("Image")
        extractor.assign(sourceString)
        text = extractor.extract()
        #print(text)

        f.write(text)
        
        #Pdf Case:
        sourceString = "Empresa.pdf"
        extractor = TextExtractorFactory.create("Pdf")
        extractor.assign(sourceString)
        text= extractor.extract()
        #print(text)

        f.write(text)