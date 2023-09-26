# Chatapp

- User registration: POST /api/register/
- User login: POST /api/login/
- Get online users: GET /api/online-users/
- Start a chat: POST /api/chat/start/
- Send a message: WEBSOCKET /api/chat/send/

## Test this API on your local machine:
### 1. Creating a Python Virtual Environment
```sh
python -m venv <virtual_environment_name>
```

### 2. Activating the Virtual Environment
```sh
cd <virtual_environment_name>
Scripts/activate
```

### 3. Installing Django, Channels and Daphne
```sh
pip install django
```
```sh
pip install channels
```
```sh
pip install daphne
```
### 4. Clone this repo into your local machine
```sh
git clone https://github.com/laminarss/django-chatapp.git
```

### 5. Run Development Server
```sh
cd django-chatapp
python manage.py runserver
```

### 6. Test the API
> To test the API, a web browser or a tool like Postman can be used.
