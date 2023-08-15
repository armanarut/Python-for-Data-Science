My first package

Package name: ft_package


To build the source distribution (tarball):
    python setup.py sdist

To build the wheel distribution:
    python setup.py bdist_wheel


To install from the source distribution (tarball):
    pip install ./dist/ft_package-0.0.1.tar.gz

To install from the wheel distribution:
    pip install ./dist/ft_package-0.0.1-py3-none-any.whl

To delete a Python package installed with pip:
    pip uninstall ft_package