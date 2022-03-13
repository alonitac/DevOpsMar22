pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'building...'
            }
        }
        stage('Test') {
            when { changeRequest target: 'dev' }
            steps {
                sh 'printenv'
                sh '''
                pip3 install -r simple_webserver/requirements.txt
                PYTHONPATH=. python3 -m pytest --junitxml results.xml simple_webserver/tests
                '''
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'results.xml'
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'deploying....'
            }
        }
    }
}