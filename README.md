# Flask User Authentication Application

This is a user authentication application based on the Flask framework, which supports user registration, login, logout, and viewing personal information. The application uses a SQLite database to store user information, and the password is hashed to ensure security. The application also uses a session object to store user IDs to track their state after logging in.

## Install Dependencies

Before running the application, make sure that all required dependencies are installed. You can install the dependencies using the following command:

```
pip install -r requirements.txt
```

## Run the Application

To run the application, enter the following command in the command line:

```
python app.py
```

This command will start the Flask application and run it on the default port (5000) of localhost. Open `http://localhost:5000` in your browser to access the application homepage.

## List of Features

The application supports the following features:

- User registration
- User login
- User logout
- View personal information

## File Structure

The file structure of the application is as follows:

```
.
├── app.py
├── README.md
├── requirements.txt
├── static
│   └── style.css
└── templates
    ├── home.html
    ├── login.html
    └── register.html
```

- `app.py`: The main code of the Flask application.
- `README.md`: This file.
- `requirements.txt`: A list of dependencies for the application.
- `static`: A directory for storing static files, such as CSS style sheets.
- `templates`: A directory for storing HTML template files.

## Developers

- [Your Name](https://github.com/YourGitHubUsername)

## License

The application is licensed under the MIT license. See the LICENSE file for more information.