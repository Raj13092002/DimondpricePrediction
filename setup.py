from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'

def get_requirements(file_path:str) ->List[str]: #we make the function and pass the file path in string format
    requirements=[] #we make the empty list so that the all the requirment keywords come here
    with open(file_path) as file_obj:# we first use the open to topen the file and make the file path in file object
        requirements=file_obj.readlines()#after that we read the lines and append at the requirment list
        requirements=[req.replace("\n","")for req in requirements]#after that we see that the \n -->next line is alo come so it is used to remove the \n

        if HYPEN_E_DOT in requirements:
            requirements.remove((HYPEN_E_DOT))
        return requirements

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='raj aryan',
    author_email='rajaryan13092002@gmail.com',
    install_requires=get_requirements('requirements.txt'),#in this we have to install the libraries that is required in this projects
    #requirement .txt is the functions that allocated the requirment file
    packages=find_packages()   #in this it see that the sub module of the pakages
)