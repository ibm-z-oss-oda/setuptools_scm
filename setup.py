from setuptools import setup
import hgdistver
setup(
    name='hgdistver',
    version=hgdistver.get_version(),
    author_mail='Ronny Pfannschmidt <Ronny.Pfannschmidt@gmx.de>',
    description='utility lib to generate python package version infos from mercurial tags',
    long_description=open('README.txt').read(),
    license='MIT',
    py_modules=[
        'hgdistver',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Version Control',
        'Topic :: System :: Software Distribution',
        'Topic :: Utilities',
    ],
)

