pipeline {
    agent any 
    environment{
        APP_ENV = "staging"
    }
    options{
        timeout(time: 20, unit: 'MINUTES')
    }
    stages {
        stage('connect to github'){
           steps{
            withCredentials([
    		  usernamePassword(credentialsId: 'GitHubUser', usernameVariable: 'USER', passwordVariable: 'PASS'),
    		]) {
    		  bat '''
    			echo  Deploying as %USER% %PASS%
    		  '''
    		}
        }
        }
        stage('Hello') {
            steps {
                echo "build number: ${env.BUILD_NUMBER}"
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
