**Django Server**

### Development environment

1. Python 3.7.4
2. Django 2.2.6

Project initially set up on a 

- Macbook with Mac OS 10.14.5 (macOS Mojave)
- Visual Studio Code 1.39.2

### Steps to setup

python -m pip install Django==2.2.6
1. Clone the repository using terminal/command-prompt
    
    'git clone https://github.com/sumitmukhija/Sustainable-City-Management-Django.git'

2. Move to the directory with 'manage.py'
3. Run anaconda prompt as admin
4. Run 'pip install -r requirements.txt' to install dependencies
5. To run server 

    'python manage.py runserver'

    For Mac, 
    
    'python3 manage.py runserver'

6. The default port is 8000. Open browser and go to localhost:8000


### Cron

* Initiate cron

`python3 manage.py runtask execute_pollution_job`

* List of tasks registered in Kronos

`python3 manage.py showtasks`
