import re

from setuptools import setup, find_packages


def __get_version():
    with open("image_processor/__init__.py") as package_init_file:
        return re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', package_init_file.read(), re.MULTILINE).group(1)


requirements = [requirement for requirement in open("requirements.txt").read().splitlines()]

setup(
    name="image_processor",
    version=__get_version(),
    url="https://github.com/thec0sm0s/image-processor-client",
    author="□ | The Cosmos",
    description="Asynchronous python client for image-processor server (https://github.com/thec0sm0s/image-processor).",
    long_description=open("README.md").read(),
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
            'Development Status :: 2 - Beta',
            'License :: OSI Approved :: MIT License',
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Topic :: Image',
            'Topic :: Tools',
    ]
)
