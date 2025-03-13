# Election Polling System  -    Using Django Framework

A web-based election polling system built with Django, allowing users to vote for political parties and view election results.

Website Link  :  https://subbu199921.pythonanywhere.com/

## Features

- User-friendly UI with animations and a responsive layout
- Users can view available political parties
- Secure voting system with unique voter IDs
- Live vote counting and results display
- Admin panel for managing parties and votes

## Technologies Used

- **Django**: Web framework
- **SQLite**: Database
- **Tailwind CSS**: Styling and responsiveness
- **Font Awesome**: Icons
- **Animate.css**: Animations

## Installation

### Prerequisites

Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/election_polling.git
   cd election_polling
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser for the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to set up an admin account.

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Open your browser and visit:

   - `http://127.0.0.1:8000/` for the election polling system
   - `http://127.0.0.1:8000/admin/` to access the admin panel

## Project Structure

```
 election_polling/
 ├── polling/
 │   ├── migrations/
 │   ├── static/
 │   ├── templates/
 │   │   ├── polling/
 │   │   │   ├── base.html
 │   │   │   ├── home.html
 │   │   │   ├── vote.html
 │   │   │   ├── results.html
 │   │   │   ├── party_detail.html
 │   ├── __init__.py
 │   ├── admin.py
 │   ├── apps.py
 │   ├── forms.py
 │   ├── models.py
 │   ├── tests.py
 │   ├── urls.py
 │   ├── views.py
 ├── election_polling/
 │   ├── __init__.py
 │   ├── settings.py
 │   ├── urls.py
 │   ├── wsgi.py
 │   ├── asgi.py
 ├── db.sqlite3
 ├── manage.py
 ├── README.md
 ├── requirements.txt
```

## Usage

- Visit the home page to see all registered parties.
- Click on a party to see details.
- Navigate to the voting page to cast a vote.
- View live election results on the results page.



