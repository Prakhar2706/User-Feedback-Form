# User Feedback Form

User Feedback Form is a Django-based web application that allows users to create multiple feedback forms and collect responses efficiently. Admins can create questions from the admin panel, and users can fill out forms with a clean and interactive user interface.

![image](https://github.com/user-attachments/assets/a4401b3b-dbfa-4f90-8977-2341c44680e8)
![image](https://github.com/user-attachments/assets/153d9088-1962-4853-a346-dd4641cb7494)
![image](https://github.com/user-attachments/assets/6554e008-377f-47a8-a632-f044699dc949)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Prakhar2706/User-Feedback-Form.git
   ```
2. Navigate to the project directory:

   ```bash
   cd User-Feedback-Form
   ```
3. Create a virtual environment:
   ```bash
   python -m venv env
   ```
4. Activate the virtual environment:
   - On Windows:
     
   ```bash
   .\env\Scripts\activate
   ```
   - On macOS/Linux:
     
   ```bash
   source env/bin/activate
   ```
5. Install the dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```
6. Create migrations for your models:

   ```bash
   python manage.py makemigrations
   ```

7. Apply migrations:

   ```bash
   python manage.py migrate
   ```

8. Create a superuser (optional, for admin access):

   ```bash
   python manage.py createsuperuser
   ```

9. Run the development server:

   ```bash
   python manage.py runserver
   ```

10. Open your web browser and go to http://127.0.0.1:8000/ to access the Madni Inter College website.

11. For admin access:

    ```bash
    http://127.0.0.1:8000/admin
    ```

## Requirements

- asgiref==3.8.1
- Django==5.1
- sqlparse==0.5.1
- tzdata==2024.1

## Features

- **Multiple Forms**: Easily create and manage multiple feedback forms.
- **Admin Panel Questions**: Admins can add, edit, and manage questions from the Django admin interface.
- **Get Responses**: Collect and view responses from users filling out the feedback forms.
- **Interactive UI**: A user-friendly, engaging interface for a smooth user experience.
- **Simple to Use**: Designed to be intuitive, requiring minimal setup to get started.
- **Responsive Design**: Fully responsive, ensuring an optimal experience on all devices.

## Usage

Once the server is running:

- Create multiple feedback forms through the admin interface.
- Add and manage questions for each form from the admin panel.
- Collect user responses and analyze the feedback.
- The app features an interactive and responsive UI, making it easy to navigate on any device.
