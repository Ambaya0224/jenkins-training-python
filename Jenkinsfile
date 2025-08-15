pipeline {
  agent any
  options { timestamps(); ansiColor('xterm') }

  environment {
    VENV = '.venv'
    REPORT_DIR = 'reports/junit'
  }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Set up Python (venv)') {
      steps {
        sh '''
          python3 -V
          python3 -m venv ${VENV}
          . ${VENV}/bin/activate
          python -m pip install --upgrade pip setuptools wheel
          if [ -f requirements.txt ]; then
            pip install -r requirements.txt
          fi
          # Ensure tests will run even without extra deps
          pip install -U pytest pytest-cov
        '''
      }
    }

    stage('Test') {
      steps {
        sh '''
          . ${VENV}/bin/activate
          mkdir -p ${REPORT_DIR}
          # Produce JUnit XML so Jenkins shows "Test Result"
          pytest -q --junitxml=${REPORT_DIR}/junit.xml || true
        '''
      }
      post {
        always {
          junit allowEmptyResults: true, testResults: 'reports/junit/*.xml'
        }
      }
    }

    stage('Build Package') {
      steps {
        sh '''
          . ${VENV}/bin/activate
          if [ -f setup.py ]; then
            python setup.py sdist bdist_wheel
          elif [ -x build.sh ]; then
            chmod +x build.sh
            ./build.sh
          else
            echo "No setup.py or build.sh found; skipping packaging."
          fi
        '''
      }
    }

    stage('(Optional) Create Executable') {
      when { expression { return fileExists('app.py') } }
      steps {
        sh '''
          . ${VENV}/bin/activate
          pip install -U pyinstaller
          # Produces dist/app (Mac binary). Keep optional to avoid breaking builds.
          pyinstaller --onefile app.py || true
        '''
      }
    }

    stage('Archive Artifacts') {
      steps {
        archiveArtifacts artifacts: 'dist/**/*,build/**/*,**/*.spec', allowEmptyArchive: true, fingerprint: true
      }
    }
  }

  post {
    success { echo '✅ Build, tests, and packaging completed.' }
    unstable { echo '⚠️ Build unstable—review test results.' }
    failure { echo '❌ Build failed—check console output.' }
  }
}
