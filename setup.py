from setuptools import setup, find_packages
from luscious_dl import __author__, __version__, __email__


with open('requirements.txt') as r:
  requirements = r.readlines()

with open('README.md') as ld:
  long_description = ld.read()

setup(
  name='luscious-downloader',
  version=__version__,
  packages=find_packages(),
  keywords='luscious, album, donwloader',
  url='https://github.com/Lucas8x/luscious-downloader',
  license='MIT',
  author=__author__,
  author_email=__email__,
  description='Download Luscious Albums',
  long_description=long_description,
  long_description_content_type="text/markdown",
  install_requires=requirements,
  include_package_data=True,
  zip_safe=False,
  entry_points={
    'console_scripts': [
      'lsd = luscious_dl.start:start'
    ]
  },
  classifiers=(
    'Programming Language :: Python :: 3',
    'Environment :: Console'
  ),
)