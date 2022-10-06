class file_opener:

    def __init__(self):

        self.encodingsList = ["utf8", "cp1252", "iso-8859-1", "iso-8859-2"]
        # add new file encodings if you need ;)

        self.maxExcondingsSuported = len(self.encodingsList)

    #*****************************************************************************#

    def letsgo(self, file):
        
        n = 0
        
        try:
            currentEncoding = self.encodingsList[n]
            currentFile = open(file,encoding=currentEncoding)
            fileContent = currentFile.readlines()

            if fileContent:
                return fileContent
    
        except:
    
            n += 1
            if n < self.maxExcondingsSuported:
                return "" #self.open(self, file, n)
    
        return ""
    
    #*****************************************************************************#
        
