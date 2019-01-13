from setuptools import setup, find_packages

requirements = [requirement for requirement in open("requirements.txt").read().splitlines()]

setup(
    name="image_processor",
    version="0.0.0.4",
    url="https://github.com/thec0sm0s/image-processor-client",
    author="□ | The Cosmos",
    description="Asynchronous python client for image-processor server (https://github.com/thec0sm0s/image-processor).",
    long_description=open("README.md").read(),
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
            'Development Status :: 2 - Alpha',
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
