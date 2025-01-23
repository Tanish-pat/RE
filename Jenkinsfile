pipeline {
    agent any

    environment {
        VENV_DIR = 'venv' // Define a reusable variable for the virtual environment
        PYTHON = 'python' // Python executable (update if a specific Python version is required)
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
                git branch: 'main', url: 'https://github.com/tanish-pat/RE'
            }
        }
        stage('Setup Virtual Environment') {
            steps {
                echo 'Setting up virtual environment...'
                bat "${PYTHON} -m venv ${VENV_DIR}" // Create virtual environment
            }
        }
        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                bat """
                call ${VENV_DIR}\\Scripts\\activate
                ${PYTHON} -m pip install --upgrade pip // Ensure pip is updated
                pip install -r requirements.txt
                """
            }
        }
        stage('Initialize Artifacts') {
            steps {
                echo 'Initializing artifacts...'
                bat """
                call ${VENV_DIR}\\Scripts\\activate
                ${PYTHON} main.py // Replace with the correct script for initialization
                """
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                bat """
                call ${VENV_DIR}\\Scripts\\activate
                pytest tests.py --disable-warnings // Add --disable-warnings for cleaner logs
                """
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                bat """
                call ${VENV_DIR}\\Scripts\\activate
                uvicorn app:app --host 0.0.0.0 --port 8000 // Customize host/port as needed
                """
            }
        }
    }

    post {
        always {
            echo 'Cleaning up virtual environment and workspace...'
            bat "rmdir /S /Q ${VENV_DIR}" // Delete the virtual environment folder
            cleanWs() // Clean up the workspace
        }
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed! Investigate the logs for issues.'
        }
    }
}
