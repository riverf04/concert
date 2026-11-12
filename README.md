# Personal Concert Tracker API

A RESTful API built with Flask and SQLAlchemy for logging, managing, and tracking personal live music experiences. Designed as a single-user backend service with JWT authentication, modular configuration, and strict resource isolation.

## Getting Started

Follow these steps to set up and run the personal concert tracker API on your local machine.

### 1. Clone the repository
```bash
git clone <repository-url>
cd concert

```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate

```

### 3. Install dependencies

```bash
pip install -r requirements.txt

```

### 4. Configure environment variables

Copy the template file to create your local environment file:

```bash
cp .env.example .env

```

Open the new `.env` file and verify your local settings and secrets.

### 5. Run the application

Start the development server using Flask:

```bash
flask run

```

The application will be accessible at `http://127.0.0.1:5000/api`.

```

```

```markdown
## Environment Variables

This project uses environment variables to manage configuration and secrets safely without hardcoding them into the source code. An `.env.example` file is provided in the repository as a template listing all required variables.

To set up your local environment, copy the template to a new file named `.env` and populate your local values:

```bash
cp .env.example .env

```

### Required Variables

* **`FLASK_APP`**: Specifies the entry point package for the Flask CLI to run.
* **`FLASK_DEBUG`**: Controls whether Flask runs in debug mode, enabling automatic reloads and error diagnostics during development.
* **`SECRET_KEY`**: Used by Flask for cryptographic security and session management.
* **`JWT_SECRET`**: Dedicated secret key used by the authentication layer to sign and verify JSON Web Tokens.
* **`DATABASE_URL`**: Specifies the connection string or file path for SQLAlchemy to target your database (such as your local development SQLite file).

```

```

```markdown
## Database Migrations

Right now, there are no database models or migration scripts created yet. The application is set up with Flask-SQLAlchemy and Flask-Migrate to handle schema version control, but the migration repository has not yet been initialized.

Once database models are defined, you will use Flask-Migrate commands to manage schema evolution safely:

* **Initialize the migration repository (first time only):**
  ```bash
  flask db init

```

* **Generate a new migration script after updating your models:**
```bash
flask db migrate -m "Description of schema changes"

```


* **Apply pending migrations to the database:**
```bash
flask db upgrade

```



```

```