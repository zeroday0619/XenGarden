from ensurepip import version
from gettext import install
from xml.etree.ElementInclude import include
from requests import packages
from setuptools import setup, find_packages

setup(
    name='XenGarden',
    version='1.0.0',
    description='XenGarden, A Python XenAPI Wrapper for Citrix Hypervisor and XCP-ng Servers',
    author='Stella IT',
    author_email='contact@stella-it.com',
    url='https://github.com/Stella-IT/XenGarden',
    packages=find_packages(exclude=['.vscode']),
    keywords=[
        'XenGarden', 'XenAPI', 'XenAPI Wrapper', 'Citrix Hypervisor', 'XCP-ng'
    ],
    python_requires='>=3',
    install_requires=[
        "xenapi", 
        "deprecated"
        ],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ]
)