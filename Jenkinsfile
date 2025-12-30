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
                sh '''
                    . venv/bin/activate
                    pytest
                '''
            }
        }

        // Step 4: Build & Package
        stage('Step 4: Build & Package') {
            steps {
                echo 'Initiating Step 4: Packaging Application...'
                
                // 1. Create a compressed .tar.gz file containing all app files
                // We include app.py, the templates folder, static folder, and requirements
                sh 'tar -czf management_app_v1.tar.gz app.py templates static requirements.txt'
                
                // 2. Archive the artifact so it is accessible in the Jenkins Dashboard
                archiveArtifacts artifacts: 'management_app_v1.tar.gz', fingerprint: true
                
                echo 'Build successful! Artifact archived.'
            }
        }
    }
}