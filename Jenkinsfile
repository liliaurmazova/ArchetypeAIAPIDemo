// Определение декларативного пайплайна
pipeline {
    
    agent any


    triggers {
        githubPush()
    }

   
    environment {
   
        API_BASE_URL = "http://api-server:80"
    }



    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Run API Tests') {
            steps {
                script {
                    docker.image('python:3.9-slim').inside('--network=container:httpbin_api') {
                        sh 'pip install --no-cache-dir -r requirements.txt'
                        sh 'pytest --verbose'
                    }
                }
            }
        }
    }

    post {
        always {
            // Выполняется всегда, независимо от результата
            echo "Pipeline finished. Status: ${currentBuild.result}"
        }
    }
}
