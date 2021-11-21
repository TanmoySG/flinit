import argparse
import os
import sys
import subprocess
from pathlib import Path
import shutil
from emoji import emojize


gitIGNOREtemplate = '''
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
*.manifest
*.spec
pip-log.txt
pip-delete-this-directory.txt
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
*.mo
*.pot
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal
instance/
.webassets-cache
.scrapy
docs/_build/
target/
.ipynb_checkpoints
profile_default/
ipython_config.py
.python-version
__pypackages__/
celerybeat-schedule
celerybeat.pid
*.sage.py
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
.spyderproject
.spyproject
.ropeproject
/site
.mypy_cache/
.dmypy.json
dmypy.json
.pyre/
'''

APPpy_CALLER = {
    "flask": "app = flask.Flask(__name__)",
    "cors": "flask_cors.CORS(app)"
}

APPpy_TEMPLATE = '''\n@app.route("/") \ndef hello_world(): \n\treturn "<p>Hello, World!</p>"'''

# Convert Path to Work with present working system
def systemSpecificPath(workingPath):
    if sys.platform in ["cygwin", "win32"]:
        return workingPath.replace("/", "\\")
    elif sys.platform in ["linux",  "darwin"]:
        return workingPath.replace("\\", "/").replace("//", "/")

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


def createProjectDirectory(workingDirectory, projectName):
    destination = systemSpecificPath(workingDirectory+"/"+projectName+"/")
    if not os.path.isdir(destination):
        os.system("mkdir {0}".format(destination))
        print(emojize(":check_mark_button:"), "Working Directory Created!")
    else:
        print(emojize(":check_mark_button:"), "Working Directory Exists!")
    return destination


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


def createREADME(location, projectName):
    Path(location+"README.md").touch()
    with open(location+"README.md", "w+") as readme:
        readme.write("# {0} is a Python-Flask Project".format(projectName))
    print(emojize(":check_mark_button:"), "README.md Created!")


def generateGITignore(workingDirectory):
    Path(workingDirectory+".gitignore").touch()
    with open(workingDirectory+".gitignore", "a+") as gitignore:
        gitignore.write(gitIGNOREtemplate)
    print(emojize(":check_mark_button:"), ".gitignore Generated!")


def addGIT(workingDirectory):
    if shutil.which("git") != None:
        generateGITignore(workingDirectory)
        os.system("cd {0} && git init -q && git add . && git commit -q -m 'Initial'".format(
            systemSpecificPath(workingDirectory)))
        print(emojize(":check_mark_button:"), "Git Setup Complete.")
        print(emojize(":check_mark_button:"),
              "Code Initialized and Committed.")
    else:
        print(emojize(":cross_mark:"),
              "Git not Installed. Skipped setting up Git.")


class linuxUNIXRunner:
    def __init__(self, location, projectName, iCors=False, iREADME=False, iGit=False) -> None:
        print(emojize(":star-struck:"), "\033[93mWelcome to Flinit @ 0.1-beta\033[0m")
        self.pythonCommand , self.pipCommand = getPyPreRequisites()
        self.projectName = projectName
        self.location = location
        self.iCors = iCors
        self.iREADME = iREADME
        self.iGit = iGit
        self.workingDirectory = createProjectDirectory(self.location, self.projectName)

    def createVirtualEnvironment(self):
        os.system('cd {0} && {1} -m venv {2}'.format(
                systemSpecificPath(self.workingDirectory),
                self.pythonCommand,
                systemSpecificPath("virtualenv")
            )
        )
        print(emojize(":check_mark_button:"), "Virtual Environment Created!")

    def generateRequirementTXT(self):
        os.system('. {0} && {1} -q freeze > {2}/requirements.txt  -q'.format(
                systemSpecificPath(self.workingDirectory +"virtualenv/bin/activate"),
                self.pipCommand, 
                systemSpecificPath(self.workingDirectory)
            )
        )
        print(emojize(":check_mark_button:"), "Requirement.txt Generated!")

    def installFlask(self):
        os.system('. {0} && {1} -q install -q Flask'.format(
                systemSpecificPath(self.workingDirectory +"virtualenv/bin/activate"),
                self.pipCommand
            )
        )
        print(emojize(":check_mark_button:"), "Installed Flask!")

    def installCORS(self):
        os.system('. {0} && {1} -q install -U -q flask-cors'.format(
                systemSpecificPath(self.workingDirectory+"virtualenv/bin/activate"),
                self.pipCommand
            )
        )
        print(emojize(":check_mark_button:"), "Installed CORS!")

    def linuxUNIXFlowRunner(self):
        self.createVirtualEnvironment()
        createAPPpy(self.workingDirectory)
        self.installFlask()
        importModuleToAPPpy(self.workingDirectory, "flask")
        if self.iCors:
            self.installCORS()
            importModuleToAPPpy(self.workingDirectory, "flask_cors")
        addModuleCallerToAPPpy(self.workingDirectory, APPpy_CALLER["flask"])
        if self.iCors:
            addModuleCallerToAPPpy(self.workingDirectory, APPpy_CALLER["cors"])
        writeTEMPLATEtoAPPpy(self.workingDirectory)
        self.generateRequirementTXT()
        if self.iREADME:
            createREADME(self.workingDirectory, self.projectName)
        if self.iGit:
            addGIT(self.workingDirectory)
        print(emojize(":clinking_beer_mugs:"),
            "\033[93m\033[1mflinit Complete!\033[0m\033[0m")


class windowsRunner:
    def __init__(self, location, projectName, iCors=False, iREADME=False, iGit=False) -> None:
        print(emojize(":star-struck:"), "\033[93mWelcome to Flinit @ 0.1-beta\033[0m")
        self.pythonCommand , self.pipCommand = getPyPreRequisites()
        self.projectName = projectName
        self.location = location
        self.iCors = iCors
        self.iREADME = iREADME
        self.iGit = iGit
        self.workingDirectory = createProjectDirectory(self.location, self.projectName)

    def createVirtualEnvironment(self):
        os.system('cd {0} && {1} -m venv {2}'.format(
                systemSpecificPath(self.workingDirectory),
                self.pythonCommand,
                systemSpecificPath("virtualenv")
            )
        )
        print(emojize(":check_mark_button:"), "Virtual Environment Created!")

    def generateRequirementTXT(self):
        os.system('{0} && {1} -q freeze > {2}/requirements.txt  -q'.format(
                systemSpecificPath(self.workingDirectory+"\\virtualenv\\Scripts\\activate"),
                self.pipCommand,
                systemSpecificPath(self.workingDirectory)
            )
        )
        print(emojize(":check_mark_button:"), "Requirement.txt Generated!")

    def installFlask(self):
        os.system('{0} && {1} -q install -q Flask'.format(
                systemSpecificPath(self.workingDirectory+"\\virtualenv\\Scripts\\activate"),
                self.pipCommand
            )
        )
        print(emojize(":check_mark_button:"), "Installed Flask!")

    def installCORS(self):
        os.system('{0} && {1} -q install -U -q flask-cors'.format(
                systemSpecificPath(self.workingDirectory+"\\virtualenv\\Scripts\\activate"),
                self.pipCommand
            )
        )
        print(emojize(":check_mark_button:"), "Installed CORS!")

    def windowsFlowRunner(self):
        self.createVirtualEnvironment()
        createAPPpy(self.workingDirectory)
        self.installFlask()
        importModuleToAPPpy(self.workingDirectory, "flask")
        if self.iCors:
            self.installCORS()
            importModuleToAPPpy(self.workingDirectory, "flask_cors")
        addModuleCallerToAPPpy(self.workingDirectory, APPpy_CALLER["flask"])
        if self.iCors:
            addModuleCallerToAPPpy(self.workingDirectory, APPpy_CALLER["cors"])
        writeTEMPLATEtoAPPpy(self.workingDirectory)
        self.generateRequirementTXT()
        if self.iREADME:
            createREADME(self.workingDirectory, self.projectName)
        if self.iGit:
            addGIT(self.workingDirectory)
        print(emojize(":clinking_beer_mugs:"),
            "\033[93m\033[1mflinit Complete!\033[0m\033[0m")


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("projectName", type=str,
                        help="Name of the Project")

    parser.add_argument(
        "location", type=str, help="The Location where the Project is to be created")

    parser.add_argument("--git", "-gt", "-g", dest="needGIT", action="store_true",
                        help="Initialize Git for the Project. Works only if Git is installed.")

    parser.add_argument("--cors", "-cr", "-c", dest="needCORS", action="store_true",
                        help="Add Cross-origin resource sharing (CORS) to Flask App.")

    parser.add_argument("--readme", "-rd", "-r", dest="needREADME",
                        action="store_true", help="Add README.md for Project.")

    parser.set_defaults(needGIT=False, needCORS=False, needREADME=False)

    args = parser.parse_args()

    if sys.platform in ["cygwin", "win32"]:
        runner = windowsRunner(
            location=args.location, 
            projectName=args.projectName,
            iCors=args.needCORS, 
            iREADME=args.needREADME, 
            iGit=args.needGIT
        )
        runner.windowsFlowRunner()
    elif sys.platform in ["linux",  "darwin"]:
        runner = linuxUNIXRunner(
            location=args.location,
            projectName=args.projectName,
            iCors=args.needCORS,
            iREADME=args.needREADME, 
            iGit=args.needGIT
        )
        runner.linuxUNIXFlowRunner()