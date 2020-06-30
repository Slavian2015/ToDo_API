<h1>ToDo API</h1>

<h4>Clone the project: </h4>
$ git clone https://github.com/Slavian2015/ToDo_API.git <br>
 <br> 

<h4>Make migrations: </h4>
(todo) $ python manage.py makemigrations todos <br>
(todo) $ python manage.py migrate <br>
 <br>

<h4>Create superuser and run server: </h4>
(todo) $ python manage.py createsuperuser <br>
(todo) $ python manage.py runserver <br>

 <br> 
<h4>Navigate to http://127.0.0.1:8000/admin and log in with your new superuser account: </h4>
- add several todos in admin panel <br>


<h4>How to get token: </h4>
python manage.py drf_create_token username <br>

<h4>After you have your token - you can make API requests by using TEST_request.py: </h4>
http://127.0.0.1:8000/apis/v1   - shows the list of tasks <br>
http://127.0.0.1:8000/apis/v1/1 - shows the task with id #1 <br>
http://127.0.0.1:8000/apis/v1/2 - shows the task with id #2 <br>
