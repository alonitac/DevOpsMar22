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
      }
    }

    stage('Deploy') {
      steps {
        echo 'deploying...'
      }
    }

  }
}