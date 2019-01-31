from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pygreynoisev1',
    version='0.1',
    description='Python wrapper around the GreyNoise APO',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Te-k/pygreynoisev1',
    author='Tek',
    author_email='tek@randhome.io',
    keywords='security',
    install_requires=['requests'],
    license='MIT',
    packages=['pygreynoisev1'],
    entry_points= {
        'console_scripts': [ 'greynoisev1=pygreynoisev1.cli:main' ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]

)
