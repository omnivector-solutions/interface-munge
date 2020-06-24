from setuptools import setuptools, find_packages

with  open('README.md') as fh:
    long_description = fh.read()


setuptools.setup(
    name='interface-munge-jesseleo',
    packages=find_packages(include=['interface_munge']),
    version='0.0.1',
    license='MIT',
    long_description= long_description,
    url='https://github.com/omnivector-solutions/interface-munge',
    python_requires='>=3.6',
)
