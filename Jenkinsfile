pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'building...'
            }
            post {
                 always {
                     jiraSendBuildInfo()
                 }
             }
        }
        stage('Test') {
            when { changeRequest() }
            steps {
                sh '''
                pip install -r simple_webserver/requirements.txt
                PYTHONPATH=. python3 -m pytest --junitxml results.xml simple_webserver/tests
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo 'deploying...'
            }
            post {
                 always {
                     jiraSendDeploymentInfo environmentId: 'east-us-1', environmentName: 'eastus', environmentType: 'production'
                 }
             }
        }
    }
}