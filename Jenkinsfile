#!groovy
// Run docker build
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
                    // Сборка Docker-образа с зависимостями
                    sh 'docker build -t bot_delo-ci-image -f ./cicd/python-lintings/Dockerfile .'
                }
            }
        }
        stage('Run Black') {
            steps {
                script {
                    // Запуск проверки Black в контейнере
                    sh 'docker run --rm -v $(pwd):/app bot_delo-ci-image black --check /app'
                }
            }
        }
        stage('Run Isort') {
            steps {
                script {
                    // Запуск проверки Isort в контейнере
                    sh 'docker run --rm -v $(pwd):/app bot_delo-ci-image isort --check-only /app'
                }
            }
        }
        stage('Run Flake8') {
            steps {
                script {
                    // Запуск проверки Flake8 в контейнере
                    sh 'docker run --rm -v $(pwd):/app bot_delo-ci-image flake8 /app'
                }
            }
        }
    }
}
