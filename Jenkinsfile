pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Build') {
          steps {
            echo 'building...'
          }
        }
      }
    }

    stage('Test') {
      steps {
        echo 'testing...'
        sh 'pip3 install -r simple_webserver/requirements.txt'
        sh '''
        PYTHONPATH=. python -m pytest --junitxml results.xml simple_webserver/tests
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
        echo 'deploying...'
      }
    }

  }
}