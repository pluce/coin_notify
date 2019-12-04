# CoinNotify

You can create a new user with curl like this :
```
curl -d "username=user&email=user@example.com&password1=12345678secret&password2=12345678secret" -X POST http://localhost:8000/api/rest-auth/registration/
```
Now you can access every path with the given token.  

For example if you want to list all the current users in the database :
```
curl -X GET http://localhost:8000/api/users/ -H "Authorization:Token 9e1adb13783e339cce772665c6f66668a52ba5a5"
```

You can access the api's documentation at ```http://localhost:8000/api/doc/``` on your web browser.
