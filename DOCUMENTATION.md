# Initializing Flask Project with flinit

Reduce 12 lines of Commands to set up a perfect Flask Project by using **flinit**

```
flinit projectName location [-h] [--version] [--git] [--cors] [--readme] 
```

# Initializing a Flask Project on windows - without flinit
Creating a Project Working Directory
```
> mkdir sampleFlaskProject
```

Creating a Virtual Environment
```
> cd sampleFlaskProject
> python3 -m venv virtualenv
```

Activating Virtual Environment
```
> virualenv\Scripts\activate.bat
```

Installing Flask and CORS within the Virtual Environment
```
> pip install Flask
> pip install flask-CORS
```

Creating the Flask app.py File
```
> touch app.py
```

Setting Up Git and README for the project (Optional)
```
> git init 
> touch .gitignore
> git add .
> git commit -m 'Initial Commit'
> touch README.md
```

This sets-up a end to end flask app.

# Initializing a Flask Project on Linux/macOS(Unix) - without flinit

Creating a Project Working Directory
```
$ mkdir sampleFlaskProject
```

Creating a Virtual Environment
```
$ cd sampleFlaskProject
$ python3 -m venv virtualenv
```

Activating Virtual Environment
```
$ source virualenv/bin/activate
```

Installing Flask and CORS within the Virtual Environment
```
$ pip install Flask
$ pip install flask-CORS
```

Creating the Flask app.py File
```
$ touch app.py
```

Setting Up Git and README for the project (Optional)
```
$ git init 
$ touch .gitignore
$ git add .
$ git commit -m 'Initial Commit'
$ touch README.md
```

This sets-up a end to end flask app on Linux/UNIX.
