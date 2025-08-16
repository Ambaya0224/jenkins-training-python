from setuptools import setup, find_packages
import os

# Try to read README.md, fall back to empty string if not found
current_dir = os.path.abspath(os.path.dirname(__file__))
long_description = ''
try:
    with open(os.path.join(current_dir, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    pass

setup(
    name='my_simple_app',
    version='0.1.0',
    author='Ganbayar Ganbaatar',
    author_email='your.email@example.com',
    description='A simple application for DevOps assessment',
    long_description=long_description,
    long_description_content_type='text/markdown' if long_description else None,
    url='https://github.com/Ambaya0224/jenkins-training-python',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        # List your project dependencies here
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
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    include_package_data=True,
    zip_safe=False,
)
