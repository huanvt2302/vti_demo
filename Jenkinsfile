pipeline {
  agent any
  stages {
        stage('Static Code Checking') {
            steps {
                script {
                    sh 'find . -name \\*.py | xargs pylint -f parseable | tee pylint.log'
                        recordIssues(
                            tool: pyLint(pattern: 'pylint.log'),
                            failTotalHigh: 10,
                        )
                    }
                }
            }
        stage('Test') {
            steps {
                echo 'Test'
            }
        }
        stage('Build image') {
            steps {
                sh 'docker build -t vti_demo:2.0 .'
            }
        }
        stage('Push Image') {
            steps {
                withDockerRegistry([credentialsId: 'huan-dockerhub', url: 'https://index.docker.io/v1/']) {
                    sh 'docker tag vti_demo:2.0 huanvt2302/vti_demo:2.0'
                    sh 'docker push huanvt2302/vti_demo:2.0'
                 }
            }
        }
        stage('Deploy K8s') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
            }
        }
    }
}  
