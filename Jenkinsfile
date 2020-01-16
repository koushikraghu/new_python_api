def label = "mypod-${UUID.randomUUID().toString()}"
def serviceaccount = "my-new-jenkins"
podTemplate(label: label, serviceAccount: serviceaccount,
            containers: [containerTemplate(name: 'docker', image: 'docker:1.11', ttyEnabled: true, command: 'cat')],
            volumes: [hostPathVolume(hostPath: '/var/run/docker.sock', mountPath: '/var/run/docker.sock')])
{
node (label) {
    def app
    stage('docker') {
    container('docker') {
    docker.image('hello-world').run()
    }
    }

    stage('Clone repository') {
        /* Cloning the Repository to our Workspace */

        git url :'https://gitlab.com/koushikraghu/Python_APi.git', branch : 'master', credentialsId : 'gitlabauth'
    }

    stage('Build image') {
        container('docker'){
        
            sh ("docker build -t registry.gitlab.com/koushikraghu/python_api:${env.BUILD_NUMBER} .")
                }
        /* This builds the actual image */
    }

    stage('Push image') {
        /* 
			You would need to first register with DockerHub before you can push images to your account
		*/
		container('docker'){
		    docker.withRegistry('https://registry.gitlab.com/koushikraghu/python_api', 'gitlabauth') {
		    sh "docker push registry.gitlab.com/koushikraghu/python_api:${env.BUILD_NUMBER}"
            echo "Trying to Push Docker Image to GitLab Registry"
            }
            }
    }
}
}
