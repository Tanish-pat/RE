pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        PYTHON = 'python' 
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
                bat "${PYTHON} -m venv ${VENV_DIR}" 
            }
        }
        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                bat """
                call ${VENV_DIR}\\Scripts\\activate
                ${PYTHON} -m pip install --upgrade pip 
                pip install -r requirements.txt
                """
            }
        }
        stage('Initialize Artifacts') {
            steps {
                echo 'Initializing artifacts...'
                bat """
                call ${VENV_DIR}\\Scripts\\activate
                ${PYTHON} main.py
                """
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                bat """
                call ${VENV_DIR}\\Scripts\\activate
                pytest tests.py
                """
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                bat """
                call ${VENV_DIR}\\Scripts\\activate
                uvicorn app:app --host 0.0.0.0 --port 8000 
                """
            }
        }
    }

    post {
        always {
            echo 'Cleaning up virtual environment and workspace...'
            bat "rmdir /S /Q ${VENV_DIR}" 
            cleanWs() 
        }
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed! Investigate the logs for issues.'
        }
    }
}
