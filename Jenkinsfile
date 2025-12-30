pipeline {
    agent any

    stages {
        // Step 1: Clone the repository
        stage('Step 1: Clone Repository') {
            steps {
                echo 'Initiating Step 1: Cloning repository...'
                git branch: 'main', url: 'https://github.com/Usman1Codes/SSD-Lab-Final.git'
            }
        }

        // Step 2: Install Dependencies
        stage('Step 2: Install Dependencies') {
            steps {
                echo 'Initiating Step 2: Installing dependencies...'
                
                // We use a virtual environment to avoid permission errors on the server
                // The '&&' ensures commands run in the same shell session
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pip list
                '''
            }
        }
    }
}