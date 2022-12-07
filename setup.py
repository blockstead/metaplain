from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.0.1',
    extras_require=dict(tests=['pytest']),
    packages=find_packages(where='src'),
    package_dir={"": "src"}
)
