# Blogger

## Description

Blogger is a full-stack web application built using Django and MySQL, enabling users to create and interact with blog posts. The platform features secure user authentication and a responsive frontend for an engaging user experience.

## Features

- Secure user authentication (registration, login, logout)
- Blog post creation, editing, and deletion
- User comments for interaction
- Responsive frontend using HTML and CSS
- MySQL database integration for efficient data management

## Technologies Used

- **Backend:** Django (Python)
- **Database:** MySQL
- **Frontend:** HTML, CSS

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/blogger.git
   cd blogger
   ```
2. Set up a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Configure database settings in `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```
5. Apply migrations and create a superuser:
   ```sh
   python manage.py migrate
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```sh
   python manage.py runserver
   ```
7. Open your browser and visit `http://127.0.0.1:8000/` to access the application.

## Usage

- Register or log in to the application.
- Create and publish blog posts.
- Comment on posts and engage with other users.
- Manage posts via the Django admin panel (`/admin`).

## Contribution

Contributions are welcome! Feel free to fork this repository and submit a pull request with improvements.

## License

This project is licensed under the MIT License.

