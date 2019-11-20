
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
 ```
 python manage.py runserver
 ```
 [Goto localhost:8000/]: http://127.0.0.1:8000/
