from TextFormatter import Pyphen, pyphenInstance


# Language of the device
globalLanguage : str = "spanish"
# Minimum confidence of the overall image. Else image will be blocked
CONFIDENCE_THRESHOLD = 70
# Confidence needed per line. Else, line will be removed
CONFIDENCE_PER_LINE = 85


class Global:
    @staticmethod
    def getLanguage():
        global globalLanguage
        return globalLanguage

    @staticmethod
    def setLanguage(language):
        global globalLanguage, pyphenInstance

        globalLanguage = language

        if globalLanguage.lower() == "english":
            pyphenInstance = Pyphen(lang = "en")
        else:
            pyphenInstance = Pyphen(lang = "es")