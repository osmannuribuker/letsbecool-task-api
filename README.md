# Letsbecool Task API

Letsbecool Task API for Todo App

## Installation

**First,** install `python3-venv` to create virtual environment.

```bash
sudo apt-get install python3-venv
```

### Installation Via `setup.py`

**Second,** start `setup.py` for create the necessary environment and run the project

```bash
bash setup.py
```

### Installation Normally

**Second,** activate virtual environment

```bash
source venv/bin/activate
```

**Third,** use the package manager [pip3](https://pip.pypa.io/en/stable/) to install `requirements.txt`.

```bash
pip3 install -r requirements.txt
```

**Fourth,** `migrate` after making all `migrations`

```bash
python manage.py makemigrations authentication
python manage.py makemigrations app
python manage.py migrate
```

**Fifth,** create user for use `API`

```bash
python manage.py createsuperuser --username='admin' --email='admin@admin.com'
```

**Finally,** run the application

```bash
python manage.py runserver
```

## Usage

```bash
python manage.py runserver
```

## Running the tests

```bash
python manage.py test core/apps/services/tests
```

## Endpoints

**SERVER_URL =** `http://localhost:8000`

**API_URL =** `<SERVER_URL>/api/v1`

**SWAGGER =** ` <API_URL>/swagger`

**DOCUMENTATION =** ` <API_URL>/redoc`

## License

[MIT](https://choosealicense.com/licenses/mit/)
