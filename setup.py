from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in lims_samples_management/__init__.py
from lims_samples_management import __version__ as version

setup(
	name="lims_samples_management",
	version=version,
	description="LIMS CLIA Sample Management Application",
	author="Hephzibah Technologies Inc",
	author_email="david.alexander@hephzibahtech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
