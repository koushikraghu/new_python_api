def label = "mypod-fortest"
def serviceaccount = "jenkins"
podTemplate(label: label, serviceAccount: serviceaccount,
            containers: [containerTemplate(name: 'docker', image: 'docker:1.11', ttyEnabled: true, command: 'cat')],
            volumes: [hostPathVolume(hostPath: '/var/run/docker.sock', mountPath: '/var/run/docker.sock')])
{
node (label) {
	
    stage('docker') {
    container('docker') {
    docker.image('hello-world').run()
    }
    }

    stage('Clone repository') {
        /* Cloning the Repository to our Workspace */

        git url :'https://github.com/koushikraghu/new_python_api.git', branch : 'master'
    }
    stage('SonarQube Analysis') {
		withCredentials([usernamePassword(credentialsId: 'SONAR', passwordVariable: 'PASSWORD', usernameVariable: 'USERNAME')]){
			scannerHome = tool 'SonarQubeScanner'
	withSonarQubeEnv('SonarQube') {
		println('Sonar Method enter');
		//sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=hello-world-python -Dsonar.projectName=hello-world-python -Dsonar.projectVersion=1.0 -Dsonar.sourceEncoding=UTF-8 -Dsonar.sources=. -Dsonar.language=py -Dsonar.scm.disabled=True -Dsonar.login=$USERNAME -Dsonar.password=$PASSWORD"
		//sonar-scanner -Dsonar.projectKey=myproject -Dsonar.sources=src1

		//def scannerHome = tool 'Sonarqube';
		sh "${scannerHome}/bin/sonar-scanner -Dsonar.login=$USERNAME -Dsonar.password=$PASSWORD";
			println('Sonar Method exit');                        
	}
     }				
    } 

    stage('Build image') {
        container('docker'){
        
            sh ("docker build -t registry.gitlab.com/koushikraghu/python_api:${env.BUILD_NUMBER} .")
                }
        /* This builds the actual image */
    }

    stage('Push image') {
		container('docker'){
		    docker.withRegistry('https://registry.gitlab.com/koushikraghu/python_api', 'gitlabauth') {
		    sh "docker push registry.gitlab.com/koushikraghu/python_api:${env.BUILD_NUMBER}"
            echo "Trying to Push Docker Image to GitLab Registry"
            }
            }
    }
}
}
