from setuptools import find_packages, setup
# -*- coding: utf-8 -*-

with open('requirements.txt', 'rt') as requirements:
    requires = requirements.readlines()

setup(name='app',
      version='1.0.0',
      description='evolvecyber',
      long_description=open('README.md').read(),
      author='Bekzot Azimov',
      author_email='ilmnuri@ilmnuri.com',
      packages=find_packages(where='app'),
      package_dir={'': 'app'},
      install_requires=requires,
      keywords='evolvecyber app',
      url='https://github.com/bazimov/sample_webapp.git',
      download_url='https://github.com/bazimov/sample_webapp.git',
      platforms=['OS Independent'],
      classifiers=[
          'Development Status :: 1 - Beta',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 2.7',
          'Operating System :: OS Independent',
      ],
      entry_points={
          'console_scripts': 'app = app.__main__:main',
      }, )
