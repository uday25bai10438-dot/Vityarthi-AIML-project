# Video Game Predictor AI

### Project Overview
* **The Application:** A web-based Machine Learning tool built with Django that predicts and recommends video games based on user preferences (Platform, Publisher, Genre, and Release Year).
* **The AI Model:** Powered by a Scikit-Learn Decision Tree Classifier, trained on historical video game sales data and pruned to a `max_depth` of 7 to optimize deployment size and prevent overfitting.
* **Dual-Response System:** To ensure high accuracy, the app first queries the original dataset for exact game matches. If none are found, it falls back to the AI model's closest predictive guess.
* **Typo-Correction:** Utilizes Python's `difflib` to run an automated algorithm that gracefully handles and corrects misspelled user inputs (e.g., publisher names) before they crash the model.

### Prerequisites
* **Python 3.8 or higher** installed on your system.
* **pip** (Python package installer).

### Setup and Installation
* **1. Clone the repository:** Open your terminal and run the following command to download the project, then navigate into the folder:
  `git clone https://github.com/Harshit1337Verma/Vityarthi-AIML-project.git`
  `cd Vityarthi-AIML-project`
* **2. Create a virtual environment:** Isolate your packages by running `python -m venv .venv`. 
* **3. Activate the environment:** * On Windows: `.venv\Scripts\activate`
  * On macOS/Linux: `source .venv/bin/activate`
* **4. Install Dependencies:** With your environment active, install all required packages by running:
  `pip install -r requirements.txt`

### Execution
* **Start the server:** This application is fully executable via the command line. Run the following command:
  `python manage.py runserver`
* **Access the app:** Open your web browser and navigate to **http://127.0.0.1:8000/**

### Usage Instructions
* **Step 1:** Enter a gaming platform (e.g., pc, ps4, x360).
* **Step 2:** Enter a publisher (e.g., valve, nintendo, ea). *Minor spelling mistakes will be auto-corrected.*
* **Step 3:** Enter a genre (e.g., shooter, action, sports).
* **Step 4:** Enter a target release year (e.g., 2004).
* **Step 5:** Click **Predict Game** to see the exact database matches or the AI's closest recommendation.# Vityarthi-AIML-project
