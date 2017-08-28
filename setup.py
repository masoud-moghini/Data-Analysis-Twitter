from setuptools import setup,find_packages
setup( 
    name='data-analysis',
    version='0.0.1',
    url='https://github.com/masoud-moghini/Data-Analysis',
    license='BSD',
    author='masoud moghini',
    packages=find_packages(),
    install_requires=['PyQt5',
        'pandas',
        'sqlalchemy',
        'nltk',
        'numpy',
        'jupyter',
        'python-twitter'],
    entry_points={},
    extras_requrie={'dev':['flake8',]}

)