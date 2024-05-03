from TextExtractorFactory import TextExtractorFactory

# este main es para testear y debugear. usenlo como sea necesario
if __name__ == "__main__":
    # Image Case:
    sourceString = "strassen.jpg"
    extractor = TextExtractorFactory.create("Image")
    extractor.assign(sourceString)
    text = extractor.extract()
    #print(text)

    #Pdf Case:
    sourceString = "Empresa.pdf"
    extractor = TextExtractorFactory.create("Pdf")
    extractor.assign(sourceString)
    text= extractor.extract()
    print(text)
