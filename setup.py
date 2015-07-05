from setuptools import find_packages, setup

version = '0.0.1a0'

setup(
    name='punct',
    version=version,
    url='https://github.com/WLPhoenix/punct',
    author='Cory Hughes',
    author_email='w.cory.hughes@gmail.com',
    description=('A tool to convert fancy unicode punctuation into standard '
                 'ascii punctuation.'),
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
