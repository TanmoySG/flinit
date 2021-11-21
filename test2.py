import argparse
import os
import sys
import subprocess
from pathlib import Path
import shutil
from emoji import emojize



def getPyPreRequisites():
    pyPath = "python"
    pipPath = "pip"

    if shutil.which("python") != None :
        if int(os.popen('python --version').read().split(" ")[1].replace("\n", "").split(".")[0]) >= 3 :
            pyPath = "python"
        else :
            print("Python 2 or lower is not supported")
    elif shutil.which("python3") != None :
        if int(os.popen('python3 --version').read().split(" ")[1].replace("\n", "").split(".")[0]) >= 3 :
            pyPath = "python3"
        else :
            print("Python 2 or lower is not supported")
    elif shutil.which("py") != None :
        if int(os.popen('py --version').read().split(" ")[1].replace("\n", "").split(".")[0]) >= 3 :
            pyPath = "py"
        else :
            print("Python 2 or lower is not supported")
    else :
        print("Python PATH issue")

    if shutil.which("pip") != None :
        pipPath = "pip"
    elif os.popen("python -m pip --version").read() !=None:
        pipPath = pyPath+" -m pip"
    else:
        os.popen(pyPath+" -m ensurepip --upgrade")
        if shutil.which("pip") != None :
            pipPath = "pip"
        elif os.popen("python -m pip --version").read() !=None:
            pipPath = pyPath+" -m pip"

    return pyPath, pipPath

    


def main():
    pythonCMD, pipCMD = getPyPreRequisites()
    # print(os.popen("python -m pip --version").read())
    print(pythonCMD, pipCMD)


if __name__ == "__main__":
    main()