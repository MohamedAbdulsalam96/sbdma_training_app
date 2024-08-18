from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sbdma_training_app/__init__.py
from sbdma_training_app import __version__ as version

setup(
	name="sbdma_training_app",
	version=version,
	description="This application is directed to the training course of the internal team of the  SBDMA",
	author="Mohamed Abdulsalam Alqadasi",
	author_email="moha2016it@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
