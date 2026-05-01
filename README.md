# SecureSSO: GitHub OAuth Dashboard

![SecureSSO Banner](https://img.shields.io/badge/Status-Active-success) ![Python](https://img.shields.io/badge/Python-3.x-blue) ![Flask](https://img.shields.io/badge/Flask-3.0.0-lightgrey) ![OAuth](https://img.shields.io/badge/Authlib-OAuth2.0-orange)

## 📖 Overview
**SecureSSO** is a lightweight, secure web application that allows users to seamlessly authenticate via their GitHub accounts using OAuth 2.0. Once authenticated, users are granted access to a personalized dashboard that retrieves and displays their live GitHub profile data and repository statistics.

This project demonstrates secure session management, external API integration, and standard OAuth authorization flows.

## 🚀 Live Demo
You can view the running application here:
*https://securesso-demo.herokuapp.com*

---

## 🛠️ Tech Stack & Technologies Used

### Backend & Core Framework
*   **Python 3.x**: The core programming language powering the logic.
*   **Flask 3.0.0**: A lightweight WSGI web application framework used for routing and handling HTTP requests.
*   **Authlib 1.2.1**: A comprehensive OAuth library used to securely integrate GitHub's OAuth 2.0 authentication flow.
*   **Requests 2.31.0**: Used under the hood to perform HTTP requests to the GitHub REST API.
*   **python-dotenv**: securely manages environment variables and secret credentials off the source code.

### Frontend
*   **HTML5 & CSS3**: Structured and styled using pure HTML and CSS.
*   **Jinja2** (via Flask): Dynamic HTML templating engine to securely render user context and repository lists directly into the frontend views.

---

## 🔑 Key Features
1.  **Single Sign-On (SSO)**: One-click secure login through GitHub. No local passwords stored.
2.  **Session Security**: Stateless, secure HTTP-only cookies managed via Flask's session framework.
3.  **Real-time GitHub Data Fetching**: Communicates with the GitHub API securely using user-scoped access tokens to fetch repository lists and profile stats.
4.  **Graceful Logout**: Securely wipes session tokens to ensure data privacy.

---

## ⚙️ Local Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/securesso.git
cd securesso
```

### 2. Set Up a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add the following keys. You will need to create an OAuth App in your GitHub Developer Settings to get the Client ID and Secret.
```env
SECRET_KEY=your_super_secret_flask_key
GITHUB_CLIENT_ID=your_github_oauth_client_id
GITHUB_CLIENT_SECRET=your_github_oauth_client_secret
```

### 5. Run the Application
```bash
flask run
# OR
python app.py
```
The app will be available at `http://localhost:5000`.

---
*Created to demonstrate robust OAuth pipelines and API integrations.*
