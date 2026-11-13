# will be responsible for creating my machine learning project as a package and that can be used later 
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    This function will be returning the list of requirements mentioned in requirements.txt
    '''
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        [req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)


setup(
    name = 'MachineLearningProject',
    version = '0.0.1',
    author= 'Rupali',
    author_email='rupalibhatnagar1997@gmail.com',
    packages= find_packages(),
    install_requires=get_requirements('requirements.txt')
)