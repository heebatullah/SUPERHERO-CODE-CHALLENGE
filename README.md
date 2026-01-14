# Superhero API

## Description
A simple Flask REST API for managing superheroes, their powers, and the strength of each hero-power combination.  
Users can view heroes, powers, and create hero-power relationships. Also includes optional email notifications via Flask-Mail.

## Author
Heeba Ahmed

---

## Table of Contents

- [Features](#features)  
- [Models](#models)  
- [Routes](#routes)  
- [Example Requests & Responses](#example-requests--responses)  
- [Setup](#setup)  
- [Testing](#testing)  

---

## Features

- Manage heroes and their superpowers.
- Assign powers to heroes with strength levels: `Strong`, `Weak`, or `Average`.
- Validations:
  - `Power.description` must be present and at least 20 characters.
  - `HeroPower.strength` must be one of `Strong`, `Weak`, or `Average`.
- Full CRUD for powers (GET, PATCH) and creation of hero-power associations (POST).

---

## Models

### Hero

| Field       | Type   |
|------------|--------|
| `id`      | Integer (Primary Key) |
| `name`    | String |
| `super_name` | String |

- Relationship: `hero_powers` (one-to-many)
- Association proxy: `powers` (many-to-many through HeroPower)

---

### Power

| Field       | Type   |
|------------|--------|
| `id`      | Integer (Primary Key) |
| `name`    | String |
| `description` | String (min 20 characters) |

- Relationship: `hero_powers` (one-to-many)
- Association proxy: `heroes` (many-to-many through HeroPower)

---

### HeroPower

| Field       | Type   |
|------------|--------|
| `id`      | Integer (Primary Key) |
| `strength`| String (`Strong`, `Weak`, `Average`) |
| `hero_id` | Foreign Key (Hero) |
| `power_id`| Foreign Key (Power) |

- Relationships: belongs to `Hero` and `Power`.

---

## Routes

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/heroes` | List all heroes |
| GET    | `/heroes/<id>` | Get hero by ID with powers |
| GET    | `/powers` | List all powers |
| GET    | `/powers/<id>` | Get power by ID |
| PATCH  | `/powers/<id>` | Update a power’s description |
| POST   | `/hero_powers` | Create a HeroPower association |

---

## Setup

1. Clone the repository:
bash
```
Copy code
git clone <repo-url>
cd <repo-folder>
```

2. Create a virtual environment:
bash
```
python3 -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:
bash
```
pip install -r requirements.txt
```

4. Initialize the database:
bash
```
flask db init
flask db migrate
flask db upgrade
```

5. Seed the database :
bash
```
python seed.py
```

6. Run the Flask server:
```
python app.py
```
#### API available at: After running flask run, visit http://127.0.0.1:5000/ and use the following endpoints.

## Author

This project was created by Heeba Ahmed

## License

This project is open source and is available for educational purposes