from setuptools import setup, find_packages


def getRequirements():
    with open('requirements.txt') as f:
        content = f.read()
        requirements = content.split('\n')
    return requirements


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='flinit',
    version='0.1.7',
    author='Tanmoy Sen Gupta',
    author_email='tanmoysps@gmail.com',
    url='https://github.com/TanmoySG/flinit',
    description='Flask App Initializer.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
            'console_scripts': [
                'flinit = flinit.flinit:main'
            ]
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    keywords=['flask', 'tanmoy', 'python', 'project'],
    install_requires=getRequirements(),
    zip_safe=False
)
