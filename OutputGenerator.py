from typing import List

from TextExtractorFactory import TextExtractorFactory
from BrailleConverter import BrailleConverter

from serial import Serial
import time

class OutputGenerator:
    """
    OutputGenerator

    Class that generates serial signals representing the given braille strings
    """
    
    def __init__(self):
        self.serialPort : int = None
        self.usbPort : str = None
        pass

    def assignSerialPort(self, serialPort : int) -> None:
        """
        Assigns a serial port to the class

        Args:
            serialPort: Integer representing the serial port to be assigned
        """
        self.serialPort = serialPort
        
    def assignUsbPort(self, usbPort : str) -> None:
        """
        Assigns a usb port to the class

        Args:
            usbPort: String representing the usb port to be assigned
        """
        self.usbPort = usbPort

    def generate(self, brailleList : List[List[str]]) -> None:
        """
        Generates a text file from a given list of braille strings.

        Args:
            brailleList: Matrix of strings representing the list of braille strings.
        """

        if self.serialPort is None:
            raise ValueError("No serial port has been assigned!")
        
        if self.usbPort is None:
            raise ValueError("No usb port has been assigned!")

        arduino = Serial(self.usbPort, self.serialPort)
        
        for brailleString in brailleList:
            for brailleChar in brailleString:
                for bit in brailleChar:
                    print(f"reading {bit}")
                    
                    for _ in range(5):
                        if bit == '0':
                            arduino.write(b'0')
                        else:
                            arduino.write(b'1')
                        time.sleep(0.5)
                        
        arduino.close()