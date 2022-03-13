pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'building...'
            }
        }
        stage('Test') {
            when { changeRequest() }
            steps {
                sh '''
                pip3 install -r simple_webserver/requirements.txt
                PYTHONPATH=. python3 -m pytest --junitxml results.xml simple_webserver/tests
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo 'deploying....'
            }
        }
    }
}