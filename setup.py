# setup.py
from setuptools import setup, find_packages

setup(
    name='my_simple_app', # The name of your package
    version='0.1.0',      # The current version of your package
    packages=find_packages(), # Automatically finds all Python packages (folders with __init__.py)
    # You can add more metadata here if needed, like:
    # author='Your Name',
    # description='A simple application for DevOps assessment',
    # long_description=open('README.md').read(),
    # long_description_content_type='text/markdown',
    # url='https://github.com/YourGitHubUsername/my-simple-app',
    # classifiers=[
    #     'Programming Language :: Python :: 3',
    #     'License :: OSI Approved :: MIT License',
    #     'Operating System :: OS Independent',
    # ],
    # python_requires='>=3.6', # Specify minimum Python version
)
