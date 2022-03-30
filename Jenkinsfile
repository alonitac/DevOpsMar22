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
                # source ./venv/bin/activate
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
            environment {
                JFROG_AR_TOKEN = credentials('jfrog-artifactory')
            }
            steps {
                sh '''
                cd simple_webserver
                echo "[global]
                index-url = https://jenkins:$JFROG_AR_TOKEN@devopsmar22.jfrog.io/artifactory/api/pypi/dependecies-pypi/simple" > pip.conf
                '''
                echo 'building...'
                rtPipInstall (
                    resolverId: "pip-default",
                    args: "-r simple_webserver/requirements.txt"
                )
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
         stage ('Package and create distribution archives') {
            steps {
                sh '''
                    cd package_demo
                    pip3 install wheel
                    python3 setup.py sdist bdist_wheel
                '''
            }
        }
         stage ('Package publish') {
            steps {
                rtUpload (
                    serverId: 'artifactory-default',
                    spec: '''{
                      "files": [
                        {
                          "pattern": "package_demo/dist/",
                          "target": "fantastic-ascii-2-pypi/"
                        }
                     ]
                    }'''
                )
            }
        }
    }
}