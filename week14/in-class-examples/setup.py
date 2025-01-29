from setuptools import setup, find_packages

setup(
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy>=1.19.5',
        'matplotlib>=3.4.3',
        'requests>=2.26.0',
        'scikit-learn>=0.24.2',
    ],

    # Script
    entry_points={
          "numpy.distutils.commands": [
            "config = numpy.distutils.command.config:config",
            "build_src = numpy.distutils.command.build_src:build_src",
            ...
        ],
    }

)
