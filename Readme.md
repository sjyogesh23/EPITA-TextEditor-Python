# Streamlit Text Editor

A lightweight, line-based text editor built using Python and Streamlit. This application allows users to create, view, edit, and manage text files directly through a web interface. It is fully containerized and includes a CI/CD pipeline for automated testing.

[Link for the Application](https://sjy-text-editor.streamlit.app/)

## 🌟 Features

* **Line-by-Line Editing:** View and manipulate text files based on line numbers.
* **CRUD Operations:**
    * **Add Line:** Insert text at specific indices or append to the end.
    * **Modify Line:** Select and edit existing lines.
    * **Delete Line:** Remove specific lines from the document.
* **File Management:**
    * **Save:** Persist your changes to the local file system.
    * **Load:** Open existing text files from the local directory.
* **Session State:** Keeps your unsaved edits active while you navigate the app.

## 🛠️ Prerequisites

* Python 3.9 or higher
* pip (Python package installer)
* Docker (Optional, for containerization)

## 📦 Installation (Local)

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/sjyogesh23/EPITA-TextEditor-Python
    cd EPITA-TextEditor-Python
    ```

2.  **Install dependencies:**
    It is recommended to use a virtual environment.
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

1.  **Run the application:**
    ```bash
    streamlit run main.py
    ```

2.  **Navigate the Interface:**
    * Open your browser to the URL shown in the terminal (usually `http://localhost:8501`).
    * Use the **Sidebar** on the left to select an action (View, Add, Modify, Delete, Save, Load).

## 🐳 Docker Support

This application is fully containerized. You can run it without installing Python locally.

1.  **Build the Docker Image:**
    ```bash
    docker build -t text-editor-app .
    ```

2.  **Run the Container:**
    ```bash
    docker run -p 8501:8501 text-editor-app
    ```
    Access the app at `http://localhost:8501`.

## ⚙️ CI/CD Pipeline

This project uses **GitHub Actions** for Continuous Integration.
* **Workflow File:** `.github/workflows/ci-cd.yml`
* **Triggers:** Pushes and Pull Requests to the `main` branch.
* **Actions:**
    * Lints code with `flake8` to ensure quality.
    * Builds the Docker image to ensure deployability.

## 📂 Project Structure

```text
.
├── .github/workflows
│   └── ci-cd.yml        # GitHub Actions configuration
├── .dockerignore        # Files excluded from Docker builds
├── .gitignore           # Files excluded from Git
├── Dockerfile           # Docker image definition
├── main.py              # Main application script
├── README.md            # Documentation
├── requirements.txt     # Python dependencies
└── setup.py             # Package installation script
