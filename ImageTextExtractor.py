from Global import CONFIDENCE_THRESHOLD, CONFIDENCE_PER_LINE
from iSourceTextExtractor import iSourceTextExtractor

import pytesseract
from PIL import Image
from pandas import DataFrame

class ImageTextExtractor(iSourceTextExtractor):
    """
    ImageTextExtractor

    Class that contains methods to extract text from images as source.
    """

    def __init__(self):
        self.image : Image = None

    def __process(self, image):
        data : DataFrame = pytesseract.image_to_data(image, output_type = "data.frame")
        data = data[data.conf != -1]

        lineArray = data.groupby("block_num")["text"].apply(list)
        confidenceArray = data.groupby("block_num")["conf"].mean()

        averageConfidence = 0

        for i in range(len(confidenceArray.values)):
            averageConfidence += confidenceArray.values[i]
        
        averageConfidence /= len(confidenceArray.values)

        if averageConfidence < CONFIDENCE_THRESHOLD:
            raise ValueError("Image given is not of high quality. Please upload another picture.")

        textResult = ""

        for i in range(len(lineArray.values)):
            line = lineArray.values[i]
            s = ""

            for word in line:
                s += word + " "
            
            if confidenceArray.values[i] > CONFIDENCE_PER_LINE:
                textResult += s

        if len(lineArray.values) <= 0 or textResult.strip() == "":
            raise ValueError("Image given is not of high quality. Please upload another picture.")

        return textResult

    def assign(self, sourceString: str) -> None:
        self.image = Image.open(sourceString)
        
    def extract(self) -> str:
        text = self.__process(self.image)
        return text