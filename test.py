import argparse
import os
import sys
import subprocess
from pathlib import Path
import shutil
from emoji import emojize


gitIGNOREtemplate = '''
'''

APPpy_CALLER = {
    "flask": "app = flask.Flask(__name__)",
    "cors": "flask_cors.CORS(app)"
}

APPpy_TEMPLATE = '''\n@app.route("/") \ndef hello_world(): \n\treturn "<p>Hello, World!</p>"'''


def systemSpecificPath(workingPath):
    if sys.platform in ["cygwin", "win32"]:
        return workingPath.replace("/", "\\")
    elif sys.platform in ["linux",  "darwin"]:
        return workingPath.replace("\\", "/").replace("//", "/")


def createAPPpy(workingDirectory):
    Path(workingDirectory+"/app.py").touch()
    print(emojize(":check_mark_button:"), "Created app.py!")


def importModuleToAPPpy(workingDirectory, package):
    with open(workingDirectory+"/app.py", "a+") as app:
        app.write("import "+package+"\n")


def addModuleCallerToAPPpy(workingDirectory, caller):
    with open(workingDirectory+"/app.py", "a+") as app:
        app.write(caller+"\n")


def writeTEMPLATEtoAPPpy(workingDirectory):
    with open(workingDirectory+"/app.py", "a+") as app:
        app.write(APPpy_TEMPLATE)


class linuxUNIXRunner:
    def __init__(self, pythonCMD, pipCMD, workingDirectory) -> None:
        self.pythonCommand = pythonCMD
        self.pipCommand = pipCMD
        self.workingDirectory = workingDirectory

    def generateRequirementTXT(self):
        os.system('. {0} && {1} -q freeze > {2}/requirements.txt  -q'.format(systemSpecificPath(
            self.workingDirectory+"virtualenv/bin/activate"), self.pipCommand, systemSpecificPath(self.workingDirectory)))
        print(emojize(":check_mark_button:"), "Requirement.txt Generated!")


newOnj = linuxUNIXRunner("python", "pip")
newOnj.printConfigs()
