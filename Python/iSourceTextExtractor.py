from abc import ABC, abstractmethod

# DONT implement the methods. This is an abstract class.
class iSourceTextExtractor(ABC):
    """
    iSourceTextExtractor

    Interface to hold different implementations of text extractors
    """

    @abstractmethod
    def assign(self, sourceString : str) -> None:
        """
        Assigns a file location to the extractor

        Args:
            sourceString: String that contains the location of the file.
        """

        # Implement it like "self.source = sourceString (or however you like)"
        pass

    @abstractmethod
    def extract(self) -> str:
        """
        Extracts the text from the previously assigned source.

        Returns:
            The string extracted from the assigned source.
        """

        pass