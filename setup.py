import os
from setuptools import setup, find_packages
import multiprocessing

def readme():
  with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    return f.read()

setup(name='jsontoemail',
      version='0.0.1',
      description='Takes a jinja2 template and some json and sends an email',
      long_description=readme(),
      url='https://github.com/sanger-pathogens/jsontoemail',
      author='Ben Taylor',
      author_email='ben.taylor@sanger.ac.uk',
      scripts=['scripts/json-to-email'],
      install_requires=[
        'email'
      ],
      test_suite='nose.collector',
      tests_require=[
        'nose',
        'mock'
      ],
      license='GPLv3',
      packages=find_packages(),
      classifiers=[
        "License :: OSI Approved :: GNU General Public License (GPLv3)",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Topic :: Communications :: Email",
        "Topic :: System :: Monitoring",
        "Topic :: Utilities"
      ]
)