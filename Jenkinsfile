pipeline {
    agent any
    
    environment {
        DATABASE_URL = 'postgresql://myuser:mypassword@localhost:5432/mydatabase'
        SECRET_KEY = 'mysecretkey'
        ENVIRONMENT = 'local'
        DOCKER_IMAGE = "user-management-service"
        DOCKER_REGISTRY = "myregistry"  // Replace with your Docker registry
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/your-repo/microservice-template.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:latest")
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    docker.image("${DOCKER_IMAGE}:latest").inside {
                        sh 'pytest'
                    }
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Push Docker image to registry
                    sh "docker tag ${DOCKER_IMAGE}:latest ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:latest"
                    sh "docker push ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:latest"
                }
            }
        }

        stage('Deploy to Production') {
            steps {
                script {
                    // Example deployment step, e.g. using Docker Compose
                    sh "docker-compose -f docker-compose.prod.yml up -d"
                }
            }
        }
    }

    post {
        always {
            script {
                sh "docker system prune -f"
            }
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs for details.'
        }
    }
}
