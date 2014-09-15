import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

version = __import__('fabulous').__version__

setup(
    name                 = 'fabulous',
    version              = version,
    url                  = 'http://lobstertech.com/fabulous.html',
    author               = 'Justine Tunney',
    author_email         = 'jtunney@lobstertech.com',
    description          = 'Makes your terminal output totally fabulous',
    download_url         = ('http://lobstertech.com/media/file/fabulous/'
                            'fabulous-' + version + '.tar.gz'),
    long_description     = read('README.rst'),
    license              = 'MIT',
    install_requires     = [
        'grapefruit',
        'Image',
    ],
    packages             = find_packages(),
    zip_safe             = False,
    include_package_data = True,
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: C",
        "Programming Language :: Python",
        "Topic :: Utilities",
        "Topic :: Artistic Software",
        "Topic :: System :: Logging",
        "Topic :: Multimedia :: Graphics"
    ],

    dependency_links = [
        'git+https://github.com/christian-oudard/Grapefruit.git#grapefruit',
    ],
)
