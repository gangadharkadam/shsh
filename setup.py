from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='shipping_management',
    version=version,
    description='App to handle transprotation of containers ',
    author='New Indictranstech Pvt Ltd',
    author_email='saurabh.p@indictranstech.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
