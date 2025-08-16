pipeline {
    agent any

    stages {
        stage('Set up Python environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip setuptools wheel  # Added wheel and setuptools
                if [ -f requirements.txt ]; then 
                    pip install -r requirements.txt
                fi
                pip install pytest
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest --junitxml=results.xml
                '''
            }
            post {
                always {
                    junit 'results.xml'
                }
            }
        }

        stage('Build package') {
            steps {
                sh '''
                . venv/bin/activate
                python setup.py sdist  # Removed bdist_wheel if not needed
                # OR use this if you want wheels:
                # pip install wheel && python setup.py sdist bdist_wheel
                '''
            }
        }

        stage('Optional: Build standalone executable') {
            when {
                expression { return fileExists('main.py') }
            }
            steps {
                sh '''
                . venv/bin/activate
                pip install pyinstaller
                pyinstaller --onefile main.py
                '''
            }
        }

        stage('Archive build outputs') {
            steps {
                archiveArtifacts artifacts: 'dist/*,build/*', fingerprint: true  # More specific pattern
                stash name: 'build-artifacts', includes: 'dist/*,build/*'  # Optional: for sharing between stages
            }
        }
    }

    post {
        always {
            cleanWs()  # Clean up workspace after build
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
