import argparse
import os
import sys
import subprocess
from pathlib import Path
import shutil

APPpy_CALLER = {
    "flask": "app = flask.Flask(__name__)",
    "cors": "flask_cors.CORS(app)"
}

APPpy_TEMPLATE = '''\n@app.route("/") \ndef hello_world(): \n\treturn "<p>Hello, World!</p>"'''


def systemSpecificPath(workingPath):
    if sys.platform in ["cygwin", "win32"]:
        return workingPath.replace("/", "\\")
    elif sys.platform in ["linux",  "darwin"]:
        return workingPath.replace("\\", "/")


def createAPPpy(workingDirectory):
    Path(workingDirectory+"/app.py").touch()
    print(u'\u2714', "Created app.py!")


def importModuleToAPPpy(workingDirectory, package):
    with open(workingDirectory+"/app.py", "a+") as app:
        app.write("import "+package+"\n")


def addModuleCallerToAPPpy(workingDirectory, caller):
    with open(workingDirectory+"/app.py", "a+") as app:
        app.write(caller+"\n")


def writeTEMPLATEtoAPPpy(workingDirectory):
    with open(workingDirectory+"/app.py", "a+") as app:
        app.write(APPpy_TEMPLATE)


def generateRequirementTXT(workingDirectory):
    if sys.platform in ["cygwin", "win32"]:
        os.system('. {0} && pip freeze > {1}/requirements.txt'.format(systemSpecificPath(
            workingDirectory+"\\virtualenv\\Scripts\\activate"), systemSpecificPath(workingDirectory)))
    elif sys.platform in ["linux",  "darwin"]:
        os.system('. {0} && pip freeze > {1}/requirements.txt'.format(systemSpecificPath(
            workingDirectory+"virtualenv/bin/activate"), systemSpecificPath(workingDirectory)))
    print(u'\u2714', "Requirement.txt Generated!")


def installFlask(workingDirectory):
    if sys.platform in ["cygwin", "win32"]:
        os.system('. {0} && pip -q install -q Flask'.format(systemSpecificPath(
            workingDirectory+"\\virtualenv\\Scripts\\activate")))
    elif sys.platform in ["linux",  "darwin"]:
        os.system('. {0} && pip -q install -q Flask'.format(
            systemSpecificPath(workingDirectory+"virtualenv/bin/activate")))
    print(u'\u2714', "Flask Installed!")


def installCORS(workingDirectory):
    if sys.platform in ["cygwin", "win32"]:
        os.system('. {0} && pip -q install -U -q flask-cors'.format(systemSpecificPath(
            workingDirectory+"\\virtualenv\\Scripts\\activate")))
    elif sys.platform in ["linux",  "darwin"]:
        os.system('. {0} && pip -q install -U -q flask-cors'.format(
            systemSpecificPath(workingDirectory+"virtualenv/bin/activate")))
    print(u'\u2714', "Cors Installed!")


def createProjectDirectory(workingDirectory, projectName):
    destination = workingDirectory+"/"+projectName+"/"
    if not os.path.isdir(destination):
        subprocess.run(["mkdir", destination])
        print(u'\u2714', "Working Directory Created!")
    else:
        print(u'\u2714', "Working Directory Exists!")
    return destination


def createVirtualEnvironment(workingDirectory):
    if sys.platform != "aix":
        try:
            subprocess.run(
                ["python", "-m", "venv", systemSpecificPath(workingDirectory)+"virtualenv"])
            print(u'\u2714', "Virtual Environment Created!")
        except subprocess.CalledProcessError as e:
            print(
                "There was an error creating virtual environment. Check the error in errors.txt")
            with open(workingDirectory+"/error.txt", "w+") as err:
                err.write(e)
            print(u'\u2718', "Flinit Initialize Project Failed")
            sys.exit()
        installFlask(workingDirectory)
    else:
        print(u'\u2718', "System not supported. Flinit Initialize Project Failed")
        sys.exit()


def createREADME(location, projectName):
    Path(location+"README.md").touch()
    with open(location+"README.md", "w+") as readme:
        readme.write("# {0} is a Python-Flask Project".format(projectName))
    print(u'\u2714', "README.md Created!")


def generateGITignore(workingDirectory):
    Path(workingDirectory+".gitignore").touch()
    shutil.copyfile("./gitignore-template.txt", workingDirectory+"/tree.gitignore")
    '''with open(workingDirectory+".gitignore", "a+") as readme:
        readme.write(open("./gitignore-template.txt", "r").read())'''
    print(u'\u2714', ".gitignore Generated!")


def addGIT(workingDirectory):
    if shutil.which("git") != None:
        generateGITignore(workingDirectory)
        os.system("cd {0} && git init -q && git add . && git commit -m 'Initial Commit' -q".format(
            systemSpecificPath(workingDirectory)))
        print(u'\u2714', "Git Setup Complete.")
        print(u'\u2714', "Code Initialized and Committed.")
    else:
        print(u'\u2718', "Git not Installed. Skipped setting up Git.")


def runner(location, projectName, iCors=False, iREADME=False, iGit=False):
    workingDirectory = createProjectDirectory(location, projectName)
    createVirtualEnvironment(workingDirectory)
    createAPPpy(workingDirectory)
    installFlask(workingDirectory)
    importModuleToAPPpy(workingDirectory, "flask")
    if iCors:
        installCORS(workingDirectory)
        importModuleToAPPpy(workingDirectory, "flask_cors")
    addModuleCallerToAPPpy(workingDirectory, APPpy_CALLER["flask"])
    if iCors:
        addModuleCallerToAPPpy(workingDirectory, APPpy_CALLER["cors"])
    writeTEMPLATEtoAPPpy(workingDirectory)
    generateRequirementTXT(workingDirectory)
    if iREADME:
        createREADME(workingDirectory, projectName)
    if iGit:
        addGIT(workingDirectory)
    print(u'\u2714', "flinit Complete!")


if __name__ == "__main__":
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

    runner(location=args.location, projectName=args.projectName,
           iCors=args.needCORS, iREADME=args.needREADME, iGit=args.needGIT)
