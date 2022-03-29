pipeline {
    agent any
    environment {
        PATH = "./venv/bin:$PATH" // Add pip virtual-environment's path to PATH
    }
    stages {
        stage ('Create venv') {
            steps {
                sh '''
                mkdir ./venv
                python3 -m venv ./venv
                source ./venv/bin/activate
                '''
            }
        }

        stage ('Artifactory Configuration') {
            steps {
                rtServer (
                    id: "artifactory-project",
                    url: "https://devopsmar22.jfrog.io/artifactory",
                    credentialsId: "jfrog-jenkins"
                )

                rtPipResolver (
                    id: "pip-resolver",
                    serverId: "artifactory-project",
                    repo: "default-pypi-remote-cache/"
                )
            }
        }

        stage ('Pip install') {
            steps {
                rtPipInstall (
                    resolverId: "pip-resolver",
                    args: "-r simple_webserver/requirements.txt"
                )
            }
        }

        stage ('Package and create distribution archives') {
            steps {
                sh '''
                    cd package_demo
                    python setup.py sdist bdist_wheel
                '''
            }
        }

        stage ('Upload packages') {
            steps {
                rtUpload (
                    serverId: "artifactory-project",
                    spec: '''{
                        "files": [
                            {
                                "pattern": "python-example/dist/",
                                "target": "pypi-virtual/"
                            }
                        ]
                    }'''
                )
            }
        }

        stage ('Publish build info') {
            steps {
                rtPublishBuildInfo (
                    serverId: "artifactory-project"
                )
            }
        }
    }
}