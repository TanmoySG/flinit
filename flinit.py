import argparse
import os
import subprocess
from pathlib import Path


def createProjectDirectory(workingDirectory, projectName):
    destination = workingDirectory+"/"+projectName+"/"
    if not os.path.isdir(destination) :
        subprocess.run(["mkdir", destination])
        print(u'\u2714', "Project Working Directory Created!")
    else:
        print(u'\u2714', "Project Working Directory Exists!")
    return destination


def createVirtualEnvironment():
    pass


def createREADME(location, projectName):
    Path(location+"README.md").touch()
    with open(location+"README.md", "w+") as readme :
        readme.write("# {0} is a Python-Flask Project".format(projectName))
    print(u'\u2714', "README.md Created!")


def dontCreateREADME():
    print(u'\u2718', "README.md not Created!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("projectName", type=str,
                        help="Name of the Project")

    parser.add_argument(
        "location", type=str, help="The Location where the Project is to be created")

    parser.add_argument("--git", "-gt", "-g", dest="shouldREADMEbeCreated",
                        action="store_const", const=createREADME, default=dontCreateREADME)

    parser.add_argument("--cors", "-cr", "-c", dest="shouldREADMEbeCreated",
                        action="store_const", const=createREADME, default=dontCreateREADME)

    parser.add_argument("--readme", "-rd", "-r", dest="shouldREADMEbeCreated",
                        action="store_const", const=createREADME, default=dontCreateREADME)

    args = parser.parse_args()

    workingDirectory = createProjectDirectory(args.location, args.projectName)

    args.shouldREADMEbeCreated(workingDirectory, args.projectName)
    print(u'\u2714', "flinit Complete!")
