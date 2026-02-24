pipeline {
    agent any 
    environment{
        APP_ENV = "staging"
    }
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
                echo "${APP_ENV}"
            }
        }
        stage('build') {
            steps {
                echo 'build'
                echo 'The second step'
                echo "${APP_ENV}"
            }
        }
        stage('test') {
            steps {
                echo 'Running tests...'
            }
        }
        stage('deploy') {
            steps {
                echo 'Deploying application...'
            }
        }
    }
}
