from KeTechSystemsAnnouncerPlayer import Announce
import re
import os
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(f"{bcolors.FAIL}Northern Line{bcolors.ENDC}")
class root:
    none = "------------------"
    rootlist = []
    availableRootList = []
def menuHeader(root):
    print(f"{bcolors.WARNING}******************************************************************************{bcolors.ENDC}")
    print(f"{bcolors.WARNING}* KeTech Systems Northern Line Announcer System - Root:  " + root + f"  *{bcolors.ENDC}")
    print(f"{bcolors.WARNING}******************************************************************************{bcolors.ENDC}")
def defineErrorMenu(root):
    print(f"{bcolors.FAIL}******************************************************************************{bcolors.ENDC}")
    print(f"{bcolors.FAIL}*                      Warning! Defined root not found!                      *{bcolors.ENDC}")
    print(f"{bcolors.FAIL}*                                                                            *{bcolors.ENDC}")
    print(f"{bcolors.FAIL}*      Proceeding will cause root " + root + f" to be unavailable!      *{bcolors.ENDC}")
    print(f"{bcolors.FAIL}******************************************************************************{bcolors.ENDC}")
    print(f"{bcolors.FAIL}*                       | Proceed? | Yes: 1 | No: 2 |                        *{bcolors.ENDC}")
    print(f"{bcolors.FAIL}******************************************************************************{bcolors.ENDC}")
    return input("")
def fatalErrorMenu():
    print(f"{bcolors.FAIL}******************************************************************************{bcolors.ENDC}")
    print(f"{bcolors.FAIL}*                                Fatal Error!                                *{bcolors.ENDC}")
    print(f"{bcolors.FAIL}*                                                                            *{bcolors.ENDC}")
    print(f"{bcolors.FAIL}*        A fatal error has occurred and the system needs to shutdown!        *{bcolors.ENDC}")
    print(f"{bcolors.FAIL}******************************************************************************{bcolors.ENDC}")
    exit(1)
def mainMenu(availableRoots, rootlist):
    print(f"{bcolors.WARNING}* Select Root:-                                                              *{bcolors.ENDC}")
    b = 0
    for x in rootlist:
        b = b + 1
        if(x in availableRoots):
            print(f"{bcolors.WARNING}* " + x + f": " + str(b) + f"                                                      *{bcolors.ENDC}")
        if(x not in availableRoots):
            print(f"{bcolors.WARNING}* {bcolors.ENDC}" + f"{bcolors.FAIL}" + x + f": ?{bcolors.ENDC}" + f"{bcolors.WARNING}                                                      *{bcolors.ENDC}")
    print(f"{bcolors.WARNING}******************************************************************************{bcolors.ENDC}")
    return input("")
def loggedMenu():
    print(f"{bcolors.WARNING}* Select Function:-                                                          *{bcolors.ENDC}")
    print(f"{bcolors.WARNING}* Broadcast: 1                                                               *{bcolors.ENDC}")
    print(f"{bcolors.WARNING}******************************************************************************{bcolors.ENDC}")
    return input("")
def MESmenu():
    print(f"{bcolors.WARNING}* Select Broadcast:-                                                                *{bcolors.ENDC}")
    print(f"{bcolors.WARNING}* MES. ?                                                                     *{bcolors.ENDC}")
    print(f"{bcolors.WARNING}******************************************************************************{bcolors.ENDC}")
    return input("")
f = open("NL/VersionList.txt", "r")
result = re.search('Versions{(.*)}', f.read())
result = [x.strip() for x in result.group(1).split(',')]
i = 0
for x in result:
    root.rootlist.append(x)
    idenfile = "NL/" + x + "/identifier.txt"
    print("NL/" + x + "/identifier.txt")
    if os.path.isfile(idenfile) is True:
        print("Root :" + x + "loaded!")
        root.availableRootList.append(x)
    else:
        menuHeader(root.none)
        answer = defineErrorMenu(root.rootlist[i])
        if(answer != "1"):
            exit(1)
    i = i + 1

#loop
while True:
    menuHeader(root.none)
    selectedroot = mainMenu(root.availableRootList, root.rootlist)   
    try:
        if(root.rootlist[int(selectedroot) - 1] in root.availableRootList):
            rootsystem = root.rootlist[int(selectedroot) - 1]
        if(root.rootlist[int(selectedroot) - 1] not in root.availableRootList):
            menuHeader(root.none)
            fatalErrorMenu()
    except:
        menuHeader(root.none)
        fatalErrorMenu()
    print(f"{bcolors.OKGREEN}" + rootsystem + f"{bcolors.ENDC}")
    menuHeader(rootsystem)
    if(loggedMenu() == "1"):
        menuHeader(rootsystem)
        try:
            Announce(("NL/" + rootsystem + "/"), (int(MESmenu())))
        except:
            menuHeader(rootsystem)
            fatalErrorMenu()
    