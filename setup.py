from setuptools import setup, find_packages

with open('README.md') as f:
    readme  = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='perukey',
    version='0.0.1',
    description='Generador de claves seguras',
    long_description=readme,
    author='Moises Alvarado',
    url='https://github.com/moisespe',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)