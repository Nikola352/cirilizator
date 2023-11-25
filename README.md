# Serbian Transliteration App

This application consists of a Python Flask backend and a JavaScript React Vite frontend. The backend provides transliteration services from Serbian Latin to Serbian Cyrillic using the GPT-3 API. The frontend allows users to input text and choose between AI-based transliteration and local transliteration.

## Running the Backend

1. Navigate to the `backend` directory:
```bash
  cd backend
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


## Running the Frontend

1. Navigate to the frontend directory:
```bash
  cd frontend
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

### Transliteration
Choose between AI-based or local transliteration.

Enter text in the input area.

Click the "Submit" button to see the transliterated text in the output area.

## Notes
Ensure both the backend and frontend servers are running simultaneously for the full functionality of the application.

Make sure to install the required dependencies using pip install -r requirements.txt and npm install for the backend and frontend, respectively.
