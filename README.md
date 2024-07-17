# Groq Project

This project integrates a FastAPI backend with a React frontend to provide a Q&A interface using the Groq API.

**Make sure to use two diffrent terminals for frontend and backend running simultanously**


## Setup

## Backend (FastAPI)

1. **Navigate to the backend directory:**
    ```bash
    cd Groq_ChatBot-master/grog_Project
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirement.txt
    ```

4. **Set up the environment variables:**
    Create a `.env` file in the `grog_Project` directory and add your Groq API key:
    ```
    GROQ_API_KEY=your-api-key-here
    ```

5. **Run the FastAPI server:**
    ```bash
    uvicorn main:app --reload
    ```

### Frontend (React)

1. **Navigate to the frontend directory:**
    ```bash
    cd Groq_ChatBot-master/frontend
    ```

2. **Install Node.js version 16** (You can use [nvm](https://github.com/nvm-sh/nvm) to manage Node.js versions):
    ```bash
    nvm install 16
    nvm use 16
    ```

3. **Install the required packages:**
    ```bash
    npm install
    ```

4. **Run the React development server:**
    ```bash
    npm start
    ```

## Usage

1. **Start the backend server** as described in the backend setup section.
2. **Start the frontend server** as described in the frontend setup section.
3. Open your browser and navigate to `http://localhost:3000`.
4. Use the Q&A interface to ask questions and see responses from the Groq API.





