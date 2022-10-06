from os import walk
from file_opener import file_opener 

class terminal_colors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    END = '\033[0m'

printed_files = []

def seek_and_print(search_pattern, item):

    opener = file_opener()
    fileContent = opener.letsgo(item)

    n = 0

    for line in fileContent:

        n += 1

        if search_pattern in line:

            if item not in printed_files:
                print("\n", terminal_colors.CYAN, item, terminal_colors.END, "\n")
                printed_files.append(item)

            print(terminal_colors.GREEN, str(n), ":", terminal_colors.END, line.strip())

#*****************************************************************************#

def list_files(search_pattern, path, extension):

    search_len = len(extension) * -1

    for (dirpath, dirnames, filenames) in walk(path):
        if dirnames:
            for sub_dir in dirnames:
                list_files(search_pattern, path + sub_dir + "/", extension)

        for fileName in filenames:
            if fileName[search_len:] == extension:
                seek_and_print(search_pattern, dirpath + fileName)

#*****************************************************************************#

def vine():

    search_pattern = input("Search pattern: ")
    path = input("File path: ")
    extension = input("File extension *.")

    if not path:
        path = "./"
    elif path[-1] not in "/":
        path += "/"

    if extension:
        extension = "." + extension

    list_files(search_pattern, path, extension)

#*****************************************************************************#

if __name__ == "__main__":

    vine()

