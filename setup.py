try:
    from setuptools import setup
    from setuptools import find_packages
except ImportError:
    from distutils.core import setup

setup(
    name='rt_primer_design',
    version='0.0.3',
    description='Primer Design for real time PCR',
    url='https://github.com/tomharrop/rtPrimerDesign',
    author='Tom Harrop',
    author_email='twharrop@gmail.com',
    license='GPL-3',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4>=4.5.1',
        'joblib>=0.9.4',
        'lxml>=3.7.1',
        'requests>=2.12.4',
        'tompytools>=0.0.3'],
    zip_safe=False
)
