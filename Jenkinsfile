pipeline {
    agent any
    environment {
        PATH = "/Users/myUser/venv-example/bin:$PATH" // Add pip virtual-environment's path to PATH
    }
    stages {

        stage ('Artifactory Configuration') {
            steps {
                rtServer (
                    id: "artifactory-project",
                    url: "https://devopsmar22.jfrog.io",
                    credentialsId: "jfrog-jenkins"
                )

                rtPipResolver (
                    id: "pip-resolver",
                    serverId: "artifactory-project",
                    repo: "pypi-virtual"
                )
            }
        }

        stage ('Pip install') {
            steps {
                rtPipInstall (
                    resolverId: "pip-resolver"
                    args: "-r python-example/requirements.txt"
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