
# This is the backend part of the project.

Used Tech Stack

## 1.Django
## 2.Mysql
## 3.GraphQl

## Running on your Machine
First install requirements.txt file by the following command

```
pip install -r requirements.txt
```
***
After the successfull installation goto backend/app/app/settings.py
Then inside setting.py edit the database credentials
  -> Provide database name
  -> Provide database username
  -> Provide database password
  
 ***
 Now run the following command to sync mysql database with the migrations
 ```
 python manage.py makemigrations
 python manage.py migrate
 ```
 
 ***
 All right now you are ready to fly
 
 Finally run the below command to start the server

 `python manage.py runserver`

 [goto localhost:8000/](http://127.0.0.1:8000/)
 
 ***
 ## Graphql Api Uses
  ***
  hit [localhost:8000/graphql/](http://127.0.0.1:8000/graphql/)
  now in the graphql explorer you can perform following queries
  ***
 ### To get all the tracks list
 Tracks:
 ![tracks](https://github.com/arifbd2221/Django-Graphql-Reactjs/blob/master/Backend/app/API-Images/tracks.png "Tracks")
 
 ### To get a token for a user
 Token:
 ![token](https://github.com/arifbd2221/Django-Graphql-Reactjs/blob/master/Backend/app/API-Images/token.png "Token")
