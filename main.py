from TextExtractorFactory import TextExtractorFactory
from TextFormatter import TextFormatter
# este main es para testear y debugear. usenlo como sea necesario
if __name__ == "__main__":
    with open("test.txt", "w") as f:
        # # Image Case:
        # sourceString = "strassen.jpg"
        # extractor = TextExtractorFactory.create("Image")
        # extractor.assign(sourceString)
        # text = extractor.extract()
        # #print(text)

        # f.write(text)
        
        # #Pdf Case:
        # sourceString = "Empresa.pdf"
        # extractor = TextExtractorFactory.create("Pdf")
        # extractor.assign(sourceString)
        # text= extractor.extract()
        # #print(text)

        # f.write(text)
        print(TextFormatter.format("ACA que ponemos aca esto es un testeo ya fue ya todos"))

        #A#M#A#N#E #C#E#R