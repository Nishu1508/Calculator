pipeline {
    agent any

    environment {
        IMAGE_REPO = "navish1508/imt2023060"
        DOCKER = "/usr/local/bin/docker"
        DOCKER_HOST = "unix:///Users/navishmalik/.docker/run/docker.sock"
    }

    stages {

        stage('Checkout from GitHub') {
            steps {
                git url: 'https://github.com/Nishu1508/Calculator.git', branch: 'main'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest -q
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    IMAGE_TAG = "${IMAGE_REPO}:${BUILD_NUMBER}"
                    sh """
                        export DOCKER_HOST=unix:///Users/navishmalik/.docker/run/docker.sock
                        ${DOCKER} build -t ${IMAGE_TAG} .
                    """
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                                                 usernameVariable: 'DOCKER_USER',
                                                 passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                        export DOCKER_HOST=unix:///Users/navishmalik/.docker/run/docker.sock
                        echo "$DOCKER_PASS" | ${DOCKER} login -u "$DOCKER_USER" --password-stdin
                        ${DOCKER} push ${IMAGE_REPO}:${BUILD_NUMBER}
                    """
                }
            }
        }
    }

    post {
        always {
            sh """
                export DOCKER_HOST=unix:///Users/navishmalik/.docker/run/docker.sock
                ${DOCKER} images | head -20
            """
        }
    }
}
