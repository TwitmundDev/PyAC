# Test de detecteur de cheat minecraft

# file = open("C:/Users/twitm/AppData/Roaming/.az-client/logs/latest.log", "r")
# files = file.readlines()
# List = []

#                               Utils


def menuTxt():
    txtCmd = "Log Analyser 1 |\nFile Analyser 2 | \n"
    return txtCmd


def menuInterract(value):
    if value == 0:
        return Main()
    elif value == 1:
        return logAnalyzer()
    elif value == 2:
        return checkDirectory()
    else:
        return


def setMinecraftPath():
    minecraftFilePath = str(input(".Minecraft Path directory ")).replace('\\', '/')
    return minecraftFilePath


def checkFile(file_path, word_list):
    with open(file_path, 'r') as f:
        results = {word: [] for word in word_list}
        for num, line in enumerate(f, start=1):
            for word in word_list:
                if word in line:
                    results[word].append(num)
    return results


#                                       Checker

def logAnalyzer():
    logWords = ["_Tr1_gran_vitece", "Wurst", "Metro"]
    result = checkFile(setMinecraftPath() + "/logs/latest.log", logWords)
    print("Log Analyzer \n :")
    print(result)
    return menuInterract(0)


def checkDirectory():
    print("Pas fini mdr")


if __name__ == '__main__':
    def Main():
        menu = int(input(menuTxt()))
        menuInterract(menu)


    Main()
