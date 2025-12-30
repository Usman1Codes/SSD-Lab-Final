pipeline {
    agent any

    stages {
        // Step 1: Clone the repository
        stage('Step 1: Clone Repository') {
            steps {
                echo 'Initiating Step 1: Cloning repository...'
                
                // While Jenkins Multibranch pipelines check out code automatically,
                // this step explicitly pulls from your specific link as requested.
                git branch: 'main', url: 'https://github.com/Usman1Codes/SSD-Lab-Final.git'
                
                // List files to confirm the clone was successful
                echo 'Verifying file contents:'
                // Use 'dir' (Windows) or 'ls -la' (Linux/Mac). 
                // Using 'sh' assumes a Linux/Mac environment or Git Bash on Windows.
                sh 'ls -la' 
            }
        }
    }
}