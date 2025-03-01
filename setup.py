from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    '''
    This function returns list of requirements.
    '''

    with open(file_path) as file:
        requirements = [req.replace('\n', '') for req in file.readlines()]

    if '-e .'  in requirements:
        requirements.remove('-e .')

    return requirements 

setup(
    name='student_performance_indicator',
    version='0.0.1',
    author='Himank',
    author_email='k.himank.14@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
