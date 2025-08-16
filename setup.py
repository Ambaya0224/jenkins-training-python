from setuptools import setup, find_packages
import os

# Read long description from README.md
current_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(current_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='my_simple_app',
    version='0.1.0',
    author='Ganbayar Ganbaatar',
    author_email='your.email@example.com',
    description='A simple application for DevOps assessment',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Ambaya0224/jenkins-training-python',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        # List your project dependencies here
        # e.g., 'flask>=1.0.0',
    ],
    extras_require={
        'dev': [
            'pytest>=6.0.0',
            'wheel',
            'pyinstaller',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'myapp=my_simple_app.main:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
    options={
        'bdist_wheel': {
            'universal': True
        }
    },
)
