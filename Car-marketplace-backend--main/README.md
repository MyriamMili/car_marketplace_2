
## install requirement.txt
    ``` bash
    pip install -r requirements.txt ```
## creating database table
    ```bash
    python manage.py makemigrations
    python manage.py migrate ```

## runserver 
    ```bash
    python manage.py runserver ```

## API Reference


| URL                                     | Method    | Description                |
|:----------------------------------------| :------- | :------------------------- |
| `user/register/`                        | `POST` | **Register a new user** 
| `user/login/`                           | `POST` | **User login with a proper credentials and authentication token** |
| `user/profile/`                         | `GET` | **Displays profile page** |
| `user/changepassword/`                  | `POST` | **Changes User password** |
| `user/send-reset-password-email/`       | `POST` | **Sends the reset password email** |
| `user/reset-password/<uidb64>/<token>/` | `POST` | **url for the changing the password** |








## Login
- **Method**: POST
- **URL**: http://127.0.0.1:8000/user/login
- **Input**:
  ```json
  {
      "email": "wass@gmail.com",
      "password": "wassim"
  }
- **Output**:
  ```json
  {
    "token": {
        "refresh": "<refresh_token_value>",
        "access": "<access_token_value>"
    },
    "msg": "Login Success"
}

## registration
- **Method**: POST
- **URL**: http://127.0.0.1:8000/user/register/
- **Input**:
  ```json
  { "email": "wass@gmail.com",
  "full_name":"wassim",
  "phone":22222222,
  "location":"london ", 
  "password": "wassim",
  "password2":"wassim"}
- **Output**:
  ```json
  {
    "token": {
       "refresh": "<refresh_token_value>",
        "access": "<access_token_value>"},
    "msg": "Registration Success"}
    
## profile
- **Method**: GET
- **URL**: http://127.0.0.1:8000/user/profile/
- **Input**:
- input:  add  authorization Auth Type: bearer token : the value for token acces 
 
- **Output**:
  ```json
  {
    "id": 1,
    "email": "wass@gmail.com",
    "full_name": "wassim sghaier",
    "phone": 22222222,
    "location": "jdfienfi"
}
 
## change password
- **Method**: POST
- **URL**: http://127.0.0.1:8000/user/changepassword/
- **Input**:
-add  authorization Auth Type: bearer token : the value for token acces 

  ```json
  {"password":"wassim", 
  "password2": "wassim"}

- **Output**:
  ```json
  {"msg": "Password Changed Successfully"}
    
