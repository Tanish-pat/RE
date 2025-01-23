pipeline {
    agent any

    environment {
        VENV_DIR = 'venv' // Define a reusable variable for the virtual environment
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository
                git branch: 'main', url: 'https://github.com/tanish-pat/jktut'
            }
        }
        stage('Setup Virtual Environment') {
            steps {
                // Create and activate a Python virtual environment
                bat "python -m venv ${VENV_DIR}"
            }
        }
        stage('Install Dependencies') {
            steps {
                // Activate the venv and install dependencies
                bat """
                call ${VENV_DIR}\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }
        stage('Test') {
            steps {
                // Activate venv and run tests
                bat """
                call ${VENV_DIR}\\Scripts\\activate
                pytest tests.py
                """
            }
        }
        stage('Initialize Artifacts') {
            steps {
                // Activate venv and run tests
                bat """
                call ${VENV_DIR}\\Scripts\\activate
                python main.py
                """
            }
        }
        stage('Deploy') {
            steps {
                // Activate venv and deploy Flask app
                bat """
                call ${VENV_DIR}\\Scripts\\activate
                uvicorn app:app --reload
                """
            }
        }
    }

    post {
        always {
            // Cleanup the virtual environment and workspace
            echo 'Cleaning up virtual environment and workspace...'
            bat "rmdir /S /Q ${VENV_DIR}" // Delete the virtual environment
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