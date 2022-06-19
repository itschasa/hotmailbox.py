from setuptools import setup

setup(
    name='hotmailbox.py',
    version='1.0.2',    
    description='An API wrapper for hotmailbox.me written in Python.',
    url='https://github.com/itschasa/hotmailbox.py',
    author='itschasa',
    license='',
    packages=['hotmailbox'],
    install_requires=[
        'httpx'                     
    ]
)