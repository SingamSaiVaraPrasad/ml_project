from setuptools import find_packages,setup
from typing import List

hyphenE='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function returns the list of packages to install for the project
     '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if hyphenE in requirements:
            requirements.remove(hyphenE)
    return requirements
setup(
    name='mlproject',
    author='Sai Vara Prasad',
    author_email='saivaraprasad5090@gmail.com',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)