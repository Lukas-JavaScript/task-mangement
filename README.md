# TaskMangemen

--

TaskMangement is a Django project designed for managing tasks. It consists of two main apps:

##### manegement – Handles adding, editing, and deleting tasks.

##### comments – Allows adding comments to tasks.
---
### Installation

#### Clone the repository:

```bash
git clone https://github.com/Lukas-JavaScript/task-mangement.git
cd taskMangement
```

#### Install Python

If you haven’t installed Python yet, you need to do so.

#### Set up a virtual environment:

Create and activate a virtual environment:

```bash
python -m venv .env
.\.env\Scripts\activate
```

#### Install dependencies:

```bash
pip install datetime whitenoise Django
```

#### Migrate the database:

```bash
python TaskMangement\manage.py migrate
```
---
#### Run the project

Windows:

```bash
start.bat
```

#### Linux:

```bash
sudo python TaskMangement\manage.py runserver 0.0.0.0:8000
```

#### macOS:

```bash
sudo python TaskMangement\manage.py runserver 0.0.0.0:8000
```
---
### Configuration

#### DEBUG
In production, DEBUG must be set to False in the settings.py file.
---
#### ALLOWED_HOSTS
Make sure all necessary hosts are included in ALLOWED_HOSTS. Example:
---
ALLOWED_HOSTS = [
'localhost',
'127.0.0.1',
get_ip_address(),
]
---
Directory structure
TaskMangement/ # Django project directory
###### TaskMangement/ # Project configuration (settings, urls, wsgi, etc.)
###### comments/ # Django app for comments
###### manegement/ # Django app for task management
###### static/ # Static files (CSS, JavaScript, images)
###### staticfiles/ # Target folder for `collectstatic`
###### db.sqlite3 # SQLite database file
###### manage.py # Django management script
