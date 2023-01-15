import re
import sys
class FileHandler(object):
    """This class deals with the aspect of extracting data from the text file selected by the user"""
    
    def __init__(self,fileName):
        self.fileName = fileName
        # Exception handling
        try:
            self.fileReader = open(fileName, 'r')
        except FileNotFoundError:
            self.fileName = "errorFileNotFound"
            return

    def get_content(self,tokenizationFlag=False):
        data = self.fileReader.read()

        # Removing special characters
        data = re.sub("[^a-zA-Z]", " ",data)

        # Changing case of all characters to lowercase
        data = data.lower()

        if(tokenizationFlag==True):
            # Tokenizig string content and return as array
            return data.split()
        else:
            return data

    def get_total_lines(self):
        with open(self.fileName) as lines:
            count = sum(1 for line in lines)
        return count

       
