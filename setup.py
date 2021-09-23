from setuptools import setup, find_packages
  
with open('requirements.txt') as f:
    requirements = f.readlines()
  
long_description = 'A CLI Tools to setup a Flask App Efficiently without requiring multi-step setup.'
  
setup(
        name ='flinit',
        version ='1.0.0',
        author ='Tanmoy Sen Gupta',
        author_email ='tanmoysps@gmail.com',
        url ='https://github.com/TanmoySG/flinit',
        description ='Flask App Initializer.',
        long_description = long_description,
        long_description_content_type ="text/markdown",
        license ='MIT',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                'flinit = flinit.flinit:main'
            ]
        },
        classifiers =(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
        keywords ='flask tanmoy starter',
        install_requires = requirements,
        zip_safe = False
)