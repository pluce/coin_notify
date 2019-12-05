# CoinNotify

## Launching the server
Install the requierements with :
```
pip3 install -r coin_notify/requirements.txt 
```

Add the cronjob for the alert system :
```
python coin_notify/manage.py crontab add
```

Launch the server with : 
```
python coin_notify/manage.py runserver
```

## Using the API

You can create a new user with curl, like this :
```
curl -d "username=user&email=user@example.com&password1=12345678secret&password2=12345678secret" -X POST http://localhost:8000/api/rest-auth/registration/
```
Now you can access every path with the given token.  

For example if you want to list all the current users in the database :
```
curl -X GET http://localhost:8000/api/users/ -H "Authorization:Token YOUR ATHORIZATION-TOKEN"
```

You can access the api's documentation at ```http://localhost:8000/api/doc/``` on your web browser.
