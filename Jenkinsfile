#!groovy
// Run docker build
def FAILED_STAGE
def FAILED_STEP
properties([disableConcurrentBuilds()])

pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '3', artifactNumToKeepStr: '3'))
        timestamps()
    }
    stages {
        stage('Linters') {
            steps {
                script {
                    FAILED_STAGE=env.STAGE_NAME
                    FAILED_STEP="Build Docker Image Linters"
                    // Сборка Docker-образа с зависимостями
                    sh 'docker build -t bot_delo-ci-image -f ./cicd/python-lintings/Dockerfile .'
                    FAILED_STEP="Black"
                    sh 'docker run --rm -v $(pwd):/app bot_delo-ci-image black --check /app/app'
                    FAILED_STEP="Isort"
                    sh 'docker run --rm -v $(pwd):/app bot_delo-ci-image isort --check-only /app/app'
                    FAILED_STEP="Flake8"
                    sh 'docker run --rm -v $(pwd):/app bot_delo-ci-image flake8 /app/app'
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    FAILED_STAGE=env.STAGE_NAME
                    FAILED_STEP="Image build"
                    sh 'docker build -t localhost:5050/my-app:latest .'
                    FAILED_STEP="Image push"
                    sh 'docker push localhost:5050/my-app:latest'
                }
            }
        }
    }
    post {
        failure {
            echo "Failed stage name: ${FAILED_STAGE}, step name: ${FAILED_STEP}"
        }
    }
}
