from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Comicru',
  version='0.0.1',
  description='A package to download comics from ReadComicsOnline.ru',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
  url='https://github.com/cyb3r-g0d/Comicru',  
  author='Cyb3rG0d',
  author_email='cyb3r-g0d@tuta.io',
  license='MIT', 
  classifiers=classifiers,
  keywords='comics', 
  packages=find_packages(),
  install_requires=[
  'requests',
    'bs4'
  ] 
)