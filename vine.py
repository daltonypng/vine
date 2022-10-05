from os import walk

class terminal_colors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    END = '\033[0m'

printed_files = []

#*****************************************************************************#

def try_open(file, n):

    encodingsList = ["utf8", "cp1252", "iso-8859-1", "iso-8859-2"]
    maxExcondingsSuported = len(encodingsList)

    try:
        currentEncoding = encodingsList[n]
        currentFile = open(file,encoding=currentEncoding)
        fileContent = currentFile.readlines()
        if fileContent:
            return fileContent

    except:

        n += 1
        if n < maxExcondingsSuported:
            return try_open(file, n)

    return ""

#*****************************************************************************#

def seek_and_print(item):

    fileContent = try_open(item, 0)

    n = 0

    for line in fileContent:

        n += 1

        if search_pattern in line:

            if item not in printed_files:
                print("\n", terminal_colors.CYAN, item, terminal_colors.END, "\n")
                printed_files.append(item)

            print(terminal_colors.GREEN, str(n), ":", terminal_colors.END, line.strip())

#*****************************************************************************#

def list_files(path, extension):

    search_len = len(extension) * -1

    for (dirpath, dirnames, filenames) in walk(path):
        if dirnames:
            for sub_dir in dirnames:
                list_files(path + sub_dir + "/", extension)

        for fileName in filenames:
            if fileName[search_len:] == extension:
                seek_and_print(dirpath + fileName)

#*****************************************************************************#

def vine():

    path = input("File path: ")
    extension = input("File extension *.")

    if not path:
        path = "./"
    elif path[-1] not in "/":
        path += "/"

    if extension:
        extension = "." + extension

    list_files(path, extension)

#*****************************************************************************#

if __name__ == "__main__":

    search_pattern = input("Search pattern: ")
    vine()
