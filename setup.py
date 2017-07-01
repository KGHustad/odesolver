from setuptools import setup

setup(name='odesolver',
      version='1.0',
      description='A small class hierarchy for solving ordinary differential equations (ODEs)',
      url='http://github.com/KGHustad/odesolver',
      author='Hans Petter Langtangen',
      #author_email='hpl@simula.no',
      maintainer='Kristian Gregorius Hustad',
      maintainer_email='krihus@ifi.uio.no',
      license='MIT',
      packages=['odesolver'],
      install_requires=[
        'numpy',
      ],
      zip_safe=False)
