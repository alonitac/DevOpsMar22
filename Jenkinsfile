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

        stage('Build 2') {
          steps {
            error 'ff'
          }
        }

      }
    }

    stage('Test') {
      steps {
        echo 'testing...'
        sh 'pip3 install -r simple_webserver/requirements.txt'
        sh '''
        PYTHONPATH=. py.test --junitxml results.xml simple_webserver/tests
        '''
      }
      post {
          always {
              // Archive unit tests for the future
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