pipeline {
  agent any
  environment {
    IMAGE_NAME = "navish1508/IMT2023060" // replace 'yourdockerhubusername'
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Prepare Python') {
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
          // use BUILD_NUMBER to tag image
          IMAGE_TAG = "${env.IMAGE_NAME}:${env.BUILD_NUMBER}"
          sh "docker build -t ${IMAGE_TAG} ."
        }
      }
    }
    stage('Push to Docker Hub') {
      steps {
        // dockerhub-creds must be created in Jenkins (username/password)
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh '''
            echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
            docker push ${IMAGE_TAG}
          '''
        }
      }
    }
  }
  post {
    always {
      sh 'docker images | sed -n "1,200p"'
    }
  }
}
