pipeline {
    agent any
    environment {
        PATH = "./venv/bin:$PATH" // Add pip virtual-environment's path to PATH
    }
    stages {
        stage ('Create venv') {
            steps {
                sh '''
                # mkdir ./venv
                python3 -m venv ./venv
                source ./venv/bin/activate
                '''
            }
        }

        stage ('Artifactory Configurations') {
            steps {
                rtServer (
                    id: 'Artifactory-1',
                    url: 'http://my-artifactory-domain/artifactory',
                    // If you're using username and password:
                    username: 'user',
                    password: 'password',
                    // If you're using Credentials ID:
                    credentialsId: 'ccrreeddeennttiiaall',
                    // If Jenkins is configured to use an http proxy, you can bypass the proxy when using this Artifactory server:
                    bypassProxy: true,
                    // Configure the connection timeout (in seconds).
                    // The default value (if not configured) is 300 seconds:
                    timeout: 300
                )
            }
        }

        stage('Build') {
            steps {
                echo 'building...'
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