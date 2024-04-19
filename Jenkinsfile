pipeline{
    agent any
    environment {
        SCANNER_HOME=tool 'sonar-scanner'
    }
    stages {
        stage('clean workspace'){
            steps{
                cleanWs()
            }
        }
        stage('Checkout from Git'){
            steps{
                git branch: 'main', url: 'https://github.com/Veeresh2708/microservices-python.git'
            }
        }
        stage("Sonarqube Analysis "){
            steps{
                withSonarQubeEnv('sonarserver') {
                    sh ''' $SCANNER_HOME/bin/sonar-scanner -Dsonar.projectName=Webapp \
                    -Dsonar.projectKey=Webapp '''
                }
            }
        }
        stage("quality gate"){
           steps {
                script {
                    waitForQualityGate abortPipeline: false, credentialsId: 'sonar' 
                }
            } 
        }
                stage('TRIVY FS SCAN') {
            steps {
                sh "trivy fs --scanners vuln,secret,misconfig . > trivyfs.txt"
            }
        }
        stage("Docker Build & Push"){
            steps{
                script{
                   withDockerRegistry(credentialsId: 'docker-hub', toolName: 'docker'){
                   sh 'printenv'
                   sh 'docker build -t python-webapp:""$GIT_COMMIT"" .'
                   sh 'docker tag netflix:""$GIT_COMMIT"" veereshvanga/ott:$BUILD_NUMBER'
                   sh 'docker push veereshvanga/python-webapp:""$BUILD_NUMBER""'
                   }
                }
            }
        }
        stage("TRIVY"){
            steps{
                sh 'trivy image veereshvanga/python-webapp:""$BUILD_NUMBER"" > trivyimage.txt' 
            }
        }
        //stage('Deploy to container'){
        //    steps{
        //        sh 'docker run -d -p 8081:80 veereshvanga/ott:""$BUILD_NUMBER""'
        //    }
        //}
        //stage('Deploy to kubernets'){
        //    steps{
        //        script{
        //            dir('Kubernetes') {
        //                withKubeConfig(caCertificate: '', clusterName: '', contextName: '', credentialsId: 'k8s', namespace: '', restrictKubeConfigAccess: false, serverUrl: '') {
        //                        sh 'kubectl apply -f deployment.yml'
        //                       sh 'kubectl apply -f service.yml'
        //               }   
        //           }
        //       }
        //   }
        //}
    }
}
