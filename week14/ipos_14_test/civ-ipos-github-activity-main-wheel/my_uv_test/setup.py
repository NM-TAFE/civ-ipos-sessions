from setuptools import setup, find_packages

setup(
    name="flask_tic_tac_toe_uv",
    version="0.1.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
