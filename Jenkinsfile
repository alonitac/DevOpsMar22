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
                    resolverId: "PIP_RESOLVER"
                    args: "-r python-example/requirements.txt"
                )
            }
        }

        stage ('Package and create distribution archives') {
            steps {
                sh '''
                    cd python-example
                    python setup.py sdist bdist_wheel
                '''
            }
        }

        stage ('Upload packages') {
            steps {
                rtUpload (
                    serverId: "ARTIFACTORY_SERVER",
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
                    serverId: "ARTIFACTORY_SERVER"
                )
            }
        }
    }
}