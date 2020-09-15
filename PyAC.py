# Test de detecteur de cheat minecraft
# Imports
import os


#                               Utils


def Jumps(n):
    for n in range(n):
        if n == 1:
            print("\n")
        print("\n")


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


def getMinercaftPath():
    return setMinecraftPath()


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
    Jumps(1)
    logWords = ["_Tr1_gran_vitece", "Wurst", "Metro"]
    result = checkFile(getMinercaftPath() + "/logs/latest.log", logWords)
    Jumps(1)
    print("Log Analyzer \n :")
    print(result)
    Jumps(1)
    return menuInterract(0)


def checkDirectory():
    McPath = getMinercaftPath()
    FoundedMinecraftDir = []
    VerDir = McPath + "/version"
    FoundedVerDir = []

    # Check dans le .minecraft
    if os.path.exists(McPath + "/Wurst"):
        FoundedMinecraftDir.insert(0, "Wurst")
    if os.path.exists(McPath + "/Metro"):
        FoundedMinecraftDir.insert(0, "Metro")
    if os.path.exists(McPath + "/Metro 5.1"):
        FoundedMinecraftDir.insert(0, "Metro 5.1")
    if os.path.exists(McPath + "/Metro 6.0"):
        FoundedMinecraftDir.insert(0, "Metro 6.0")
    if os.path.exists(McPath + "/Huzuni"):
        FoundedMinecraftDir.insert(0, "Huzuni")


    # Check dans les .minecraft/version
    if os.path.exists(VerDir + "Wurst"):
        FoundedVerDir.insert(0, "Wurst")

    Jumps(1)
    print("Founded in .Minecraft :")
    print(FoundedMinecraftDir)
    Jumps(1)
    print("Founded in .minecraft/version")
    print(FoundedVerDir)
    return menuInterract(0)


if __name__ == '__main__':
    def Main():
        menu = int(input(menuTxt()))
        menuInterract(menu)


    Main()
