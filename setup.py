from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in fund_request/__init__.py
from fund_request import __version__ as version

setup(
	name="fund_request",
	version=version,
	description="fund request app",
	author="sydney",
	author_email="sydneykb38@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
