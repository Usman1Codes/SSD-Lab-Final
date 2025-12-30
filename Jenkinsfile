pipeline {
    agent any

    // Define a global variable for our "Production" folder
    environment {
        DEPLOY_DIR = '/tmp/management_app_prod'
    }

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
                sh 'tar -czf management_app_v1.tar.gz app.py templates static requirements.txt'
                archiveArtifacts artifacts: 'management_app_v1.tar.gz', fingerprint: true
            }
        }

        // Step 5: Deploy Application
        stage('Step 5: Deploy Application') {
            steps {
                echo 'Initiating Step 5: Simulating Deployment...'
                
                // 1. Create the deployment directory (Simulates a server folder)
                // -p ensures no error if it already exists
                sh "mkdir -p ${DEPLOY_DIR}"
                
                // 2. Clean the directory (optional, simulates fresh deploy)
                sh "rm -rf ${DEPLOY_DIR}/*"
                
                // 3. Copy the artifact to the deployment folder
                sh "cp management_app_v1.tar.gz ${DEPLOY_DIR}"
                
                // 4. Extract the files (Unzip)
                sh "cd ${DEPLOY_DIR} && tar -xzf management_app_v1.tar.gz"
                
                // 5. Verify deployment
                echo "Deployment finished. Listing files in ${DEPLOY_DIR}:"
                sh "ls -la ${DEPLOY_DIR}"
            }
        }
    }
    
    // Post-build actions (Status Notifications)
    post {
        success {
            echo '✅ Pipeline succeeded! The app is deployed to /tmp/management_app_prod'
        }
        failure {
            echo '❌ Pipeline failed. Please check the console output for errors.'
        }
    }
}