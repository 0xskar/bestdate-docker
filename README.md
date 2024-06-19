# BestDate

BestDate is a dating app designed to match users based on core factors like religion, politics, handling money, hygiene, and lifestyle choices. Users can specify how they would like their potential matches to respond to the same questions and weight these responses based on importance.

This project is still very much in early stages of construction.

## Features

- User Registration ❌
- User Login (with options for Google and Facebook login) ✅
- Profile Management ❌
- Matching Algorithm ❌
- Messaging System ❌
- Privacy Settings ❌
- Event-Based Dating ❌

## Requirements

- Python 3.x
- Flask
- SQLAlchemy
- Flask-Migrate
- Flask-Login
- Flask-OAuthLib
- PostgreSQL
- Docker (for containerization)

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/bestdate.git
    cd bestdate
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Setup the database:

    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. Run the application:

    ```bash
    flask run
    ```

6. (Optional) Run the application in a Docker container:

    ```bash
    docker-compose up --build
    ```

## Directory Structure

```
bestdate/
│
├── app/
│ ├── init.py
│ ├── routes.py
│ ├── models.py
│ ├── forms.py
│ ├── templates/
│ │ ├── base.html
│ │ ├── index.html
│ │ ├── login.html
│ │ ├── register.html
│ └── static/
│ ├── styles.css
│ └── images/
│
├── .env
├── config.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Environment Variables

Create a `.env` file in the root directory and add the following variables:

```
SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=postgresql://postgres
@db:5432/postgres
OAUTHLIB_INSECURE_TRANSPORT=1
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
FACEBOOK_CLIENT_ID=your_facebook_client_id
FACEBOOK_CLIENT_SECRET=your_facebook_client_secret
```


## Contributing

Contributions are welcome! Please fork the repository and create a pull request.

## License

This project is licensed under the MIT License.
