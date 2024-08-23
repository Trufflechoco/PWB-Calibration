from setuptools import setup, find_packages

requirements = ['setuptools>=70.2.0', 'numpy>=1.26.4', 'matplotlib>=3.8.3', 'pandas>=2.1.3',
                'PyYAML>=6.0.1', 'pyPDF2>=3.0.1', 'reportlab>=4.0.7', 'requests>=2.31.0']

setup(
    name='PwbCalib',
    version='1.0',
    description='Package to graph the raw results from PWB calibration chips, and the insertion loss at select wavelength.',
    author='Tenna Yuan',
    author_email='tenna@student.ubc.ca',
    packages=find_packages(),
    install_requires=requirements
)