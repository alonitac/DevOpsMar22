pipeline {
    agent any

    stages {

        stage ('Artifactory Configuration') {
            steps {
                rtServer (
                    id: "artifactory-project",
                    url: 'https://devopsmar22.jfrog.io',
                    credentialsId: 'jfrog-jenkins'
                )

//                 rtPipResolver (
//                     id: "PIP_RESOLVER",
//                     serverId: "ARTIFACTORY_SERVER",
//                     repo: "pypi-virtual"
//                 )
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