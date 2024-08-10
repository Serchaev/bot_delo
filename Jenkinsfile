#!groovy
// Run docker build
def FAILED_STAGE
properties([disableConcurrentBuilds()])

pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '3', artifactNumToKeepStr: '3'))
        timestamps()
    }
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    FAILED_STAGE=env.STAGE_NAME
                    // Сборка Docker-образа с зависимостями
                    sh 'docker build -t bot_delo-ci-image -f ./cicd/python-lintings/Dockerfile .'
                }
            }
        }
        stage('Black') {
            steps {
                script {
                    FAILED_STAGE=env.STAGE_NAME
                    // Запуск проверки Black в контейнере
                    sh 'docker run --rm -v $(pwd):/app bot_delo-ci-image black --check /app/app'
                }
            }
        }
        stage('Isort') {
            steps {
                script {
                    FAILED_STAGE=env.STAGE_NAME
                    // Запуск проверки Isort в контейнере
                    sh 'docker run --rm -v $(pwd):/app bot_delo-ci-image isort --check-only /app/app'
                }
            }
        }
        stage('Flake8') {
            steps {
                script {
                    FAILED_STAGE=env.STAGE_NAME
                    // Запуск проверки Flake8 в контейнере
                    sh 'docker run --rm -v $(pwd):/app bot_delo-ci-image flake8 /app/app'
                }
            }
        }
    }
    post {
        failure {
            echo "Failed stage name: ${FAILED_STAGE}"
        }
    }
}
