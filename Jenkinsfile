pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'building...'
            }
            post {
                 always {
                     jiraSendBuildInfo site: 'exit-zero.atlassian.net'
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
        }
    }
}