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
                // We install requirements.txt which now includes pytest
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        // Step 3: Run Unit Tests
        stage('Step 3: Run Unit Tests') {
            steps {
                echo 'Initiating Step 3: Running Unit Tests...'
                
                // We must reactivate the venv to access pytest
                sh '''
                    . venv/bin/activate
                    echo "Running tests against app.py..."
                    pytest
                '''
            }
        }
    }
}