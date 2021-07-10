#!/usr/bin/env python
import os
import re
from pprint import pprint

from setuptools import setup


def get_long_description():
    content = ""
    with open("README.md", encoding='utf-8') as FH:
        content = FH.read()
    return content


def get_version():
    version = None
    notes_filepath = "RELEASES_NOTES.md"
    if os.path.exists(notes_filepath):
        with open(notes_filepath) as FH:
            first_line = FH.readline()
            version = re.search("^\#\s+.+\s+(.+)\s+\[", first_line).groups()[0]  # Example: "# v2.5.0 [DEV]"
    return version


def load_requirements(path):
    requirements = []
    with open(path) as FH:
        requirements = [elt.strip().replace(" ", "") for elt in FH]
    return requirements


def get_package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))

    pprint(paths)
    return paths



"""
Generate module : 
python setup.py bdist_wheel

Install module
pip install dist/variant_project-0.2.0-py3-none-any.whl
pip install --force-reinstall dist/variant_project-0.2.0-py3-none-any.whl

Uninstall module
pip uninstall variant_project


With the same python environment and therefore on the same system :
pip install .
pip install -e .
"""

setup(
    name='variant_project',
    version=get_version(),
    description='Parse annotated VCF files, manage variant database and requests, provide web services.',
    author='Noël MAURICE - IUCT Oncopole Toulouse',
    author_email='maurice.noel@iuct-oncopole.fr',
    license='CeCILL v2.1',
    packages=['variant',
              'sample',
              'variant_project_api'],
    package_data={'variant': get_package_files('variant'),
                  'sample': get_package_files('sample'),
                  'variant_project_api': get_package_files('variant_project_api')},
    include_package_data=True,
    install_requires=load_requirements("requirements.txt"),
    url='https://github.com/noelmaurice-iuct-oncopole/variant_project_server',
    python_requires='>=3.8',
    keywords='biology VCF variant sample filter annotation genome',
    long_description_content_type='text/markdown',
    long_description=get_long_description(),
)
