**Django Server**

### Development environment

1. Python 3.7.4
2. Django 2.2.6

Project initially set up on a 

- Macbook with Mac OS 10.14.5 (macOS Mojave)
- Visual Studio Code 1.39.2

### Steps to setup


1. Clone the repository using terminal/command-prompt
    
    `git clone https://sumitmukhijaa@bitbucket.org/cs7cs3/scm-backend.git`

2. Move to the directory with `manage.py`
3. To run server 

    `python manage.py runserver`

    For Mac, 
    
    `python3 manage.py runserver`

4. The default port is 8000. Open browser and go to localhost:8000
5. A JSON response like below should be seen.
   
    `{
        "message": "It's working!", 
        "time": "2019-11-07T13:12:46.906"
    }`