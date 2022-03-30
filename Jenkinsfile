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
                    id: 'artifactory-default',
                    url: 'https://devopsmar22.jfrog.io/artifactory',
                    credentialsId: 'jfrog-artifactory'
                )

                rtPipResolver (
                    id: "pip-default",
                    serverId: "artifactory-default",
                    repo: "dependecies-pypi"
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