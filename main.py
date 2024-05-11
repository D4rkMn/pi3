from TextExtractorFactory import TextExtractorFactory

# este main es para testear y debugear. usenlo como sea necesario
if __name__ == "__main__":
    with open("test.txt", "w") as f:

        # Image Case:
        sourceString = "strassen.jpg"
        #sourceString = "b.jpg" # ejemplo de imagen invalida
        extractor = TextExtractorFactory.create("Image")
        extractor.assign(sourceString)

        try:
            text = extractor.extract()
            f.write(text)
            f.write("\n\n")
        except ValueError as e:
            print(f"{e}")

        #Pdf Case:
        sourceString = "Empresa.pdf"
        extractor = TextExtractorFactory.create("Pdf")
        extractor.assign(sourceString)

        try:
            text = extractor.extract()
            f.write(text)
        except ValueError as e:
            print(f"{e}")