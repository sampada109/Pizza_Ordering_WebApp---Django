# 🍕 Pizza Ordering Web App

This project is about Pizza Ordering Web App is a full-featured web application built using Django. The web App allows users to browse a variety of pizzas through the pizza menu, create accounts, place orders, add pizzas to cart, customize their orders, view their order history, and make payments seamlessly. The project showcases skills in web development, robust implementation of Django, user authentication, with deployment on Render and media storage on Cloudinary.

---

## Table of Contents
1. [Project Setup](#project-setup)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Testing](#testing)
6. [Project Structure](#project-structure)
7. [Screenshots](#screenshots)
8. [Technologies Used](#technologies-used)
9. [Contributing](#contributing)
10. [Contact](#contact)

---

## Project Setup
This project was created with the following setup:

- Django Project: pizza_orders
- Django App: orders
### Environment Setup
- Python Version: 3.6 or later
- Django Version: 3.2 or later
- pip (Python package installer)

1. Create a virtual environment : ```python -m venv venv```
2. Activate the virtual environment :
   - Windows: ```.venv\Scripts\activate```
   - macOS\Linux: ```source venv/bin/activate```
3. Install Dependencies: ```pip install django```

---

## Features
- **User Authentication 🪪**: Users can sign up, log in, and log out.
- **Menu Display 📃**: View available pizzas.
- **Order Placement 🛒**: Add pizzas to cart, also feature to customize pizzas available, and place orders.
- **User Account 🔐**: Users can create accounnt where they can edit their profile details, change password and logout.
- **Order History ⌛**: View all history of orders (pending and completed orders).
- **Admin Interface 👨🏻‍💼**: Manage pizzas, order items, users, customer orders, pizza category, pizza pricing and etc.
- **Payment Integration 🏧**: Integrated with Instamojo for secure payments (using only testing mode - Instamojo sandbox testing).
- **Responsive Design 📱**: Fully responsive design, works on all devices.
- **Media Storage 🖼️**: Images are stored and served from Cloudinary (as render free tier does not provide presistent storage/disk storage).

---

## Installation
1. Clone the repository: <br>
   - ```
     git clone https://github.com/sampada109/Pizza_Ordering_WebApp---Django.git
2. Navigate to the project directory: <br>
   - ```
     cd Pizza_Ordering_WebApp
3. Install the dependencies:<br>
   - ```
     pip install -r requirements.txt
4. Set up the database: If you want to use any other databse then follow its documentation to integrate it.
5. Set up the environment variables: <br>
   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   
   - IF YOU WANT TO USE ANY CLOUD FOR STORING THE MEDIA FILES
     HERE I HAVE USED CLOUDINARY BECAUSE RENDER DOES NOT PROVIDE ANY DISK STORAGE IN FREE TIER
      CLOUD_NAME=your_cloudinary_cloud_name
      CLOUD_API_KEY=your_cloudinary_api_key
      CLOUD_API_SECRET=your_cloudinary_api_secret
   
   - FOR PAYMENT GATEWAY I HAVE USED INSTAMOJO, YOU CAN USE ANYOTHER GATEWAY AS WELL
     I HAVE USED INSTAMOJO SANDBOX TESTING API AS I'M NOT USING ANY REAL PAYMENT 
      INSTAMOJO_API_KEY=your_instamojo_api_key
      INSTAMOJO_AUTH_TOKEN=your_instamojo_auth_token
      INSTAMOJO_ENDPOINT=your_instamojo_endpoint

8. Apply Migrations : <br>
   - ```
     python manage.py migrate
7. Create a superuser for accessing the admin pannel:
   - ```
     python manage.py createsuperuser
9. Run the development server:
    - ```
      python manage.py runserver

---

## Usage
### Running the Application
  1. Start the server:
     ```python manage.py runserver```
  2. Access the app in your browser:
### User Interactions
  - **Sign Up/Login**: Create an account or log in.
  - **View Menu**: Browse available pizzas.
  - **Place Orders**: Select pizzas, customize them, and place orders.
  - **Order History**: Check previous orders on account page

---

## Testing
### Running Tests
To run the tests, use the following command:
```python manage.py test```

---

## Project Structure
- ```
   pizza_orders/
   |----media/
   |     |----pizza_images/
   |----orders/
   |     |----migrations/
   |     |----management/
   |     |----__init__.py
   |     |----admin.py
   |     |----apps.py
   |     |----models.py
   |     |----tests.py
   |     |----views.py
   |     |----urls.py
   |----pizza_orders/
   |     |----__init__.py
   |     |----asgi.py
   |     |----settings.py
   |     |----urls.py
   |     |----wsgi.py
   |----static/
   |----staticfiles/
   |----templates/
   |----theme/
   |----build.sh
   |----db.sqlite3
   |----manage.py
   |----requirements.txt
   |----venv/
   |----.env
   |----.gitignore
   |----README.md


---

## Screenshots
will be updated during the progress of the project

---

## Technologies Used
- **Backend**: Django
- **Frontend**: HTML, CSS, Tailwind CSS
- **Database**: SQLite
- **Deployment**: Render
- **Media Storage**: Cloudinary
- **Payment Gateway**: Instamojo Sandbox Testing

---

## Contributing
Contributions are welcome! Please create a pull request or open an issue for suggestions or bug reports.

---

## Contact
Feel free to reach out for any questions or suggestions:

Email: sampada.kaushik.cseds.2020@miet.ac.in <br>
LinkedIn: https://www.linkedin.com/in/sampada-kaushik/ <br>
GitHub: https://github.com/sampada109/

---
