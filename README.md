# AuctionApp

## Setting the project

Create environment
```
python -m venv env
```

Activate environment
```
// Linux/MacOS
source env/bin/activate

// Windows
env/Scripts/activate

```
Install dependencies
``` 
pip3 install -r requirements.txt
```

Setup django
```
python3 manage.py migrate
python3 manage.py seed
python3 manage.py runserver
```

## Open app
Go to the browser to http://localhost:8000/login

## Users
You have access to 2 test users (both with password 'p@ssw0rd'):
user_1, user_2
