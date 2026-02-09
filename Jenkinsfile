pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'echo "data" > file.txt'
        sh 'ls -la'
      }
    }
    stage('Test') {
      steps {
        sh 'cat file.txt'
      }
    }
  }
}
