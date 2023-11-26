# Serbian Transliteration App

This application consists of a Python Flask backend and a JavaScript React Vite frontend. The backend provides transliteration services from Serbian Latin to Serbian Cyrillic using the GPT-3 API. The frontend allows users to input text and choose between AI-based transliteration and local transliteration.

## Running the Backend

1. Navigate to the `server` directory:
```bash
  cd server
```
   
2. Install the required Python packages using pip:

```bash
  pip install -r requirements.txt
```

3. Run the Flask development server:
```bash
  flask run
```
The backend will start on http://localhost:5000.
View the docs: http://localhost:5000/apidocs/#/


## Running the Frontend

1. Navigate to the `client` directory:
```bash
  cd client
```

2. Install the required Node.js packages using npm:
```bash
  npm install
```

3. Run the Vite development server:
```bash
  npm run dev
```
The frontend will be accessible at http://localhost:5173.

## Usage
Access the frontend in your web browser at http://localhost:5173.

Access the login page at http://localhost:5173/login

Create a blog post at http://localhost:5173/admin

## Notes
Ensure both the backend and frontend servers are running simultaneously for the full functionality of the application.

Make sure to install the required dependencies using pip install -r requirements.txt and npm install for the backend and frontend, respectively.

## TODO
Add backend tests

Add more backend docs

Refactor some frontend code

Make buttons for /login and /admin
