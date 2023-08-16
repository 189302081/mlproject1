from setuptools import find_packages,setup
HYPEN_E_DOT='-e .'

def get_requirements(file_path: str):
    '''
    This function returns a list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        for req in file_obj:
            req = req.strip()
            if req != HYPEN_E_DOT:
                requirements.append(req)
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Sanjil',
author_email='sanjilmahajani@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)