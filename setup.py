import setuptools

setuptools.setup(
    name='JustgoodAPI',
    version='V2.2.7',
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
        'aiohttp'
    ],
    url='https://github.com/herbertendrian/justgoodapi',
    license='MIT',
    author='Bert.',
    author_email='',
    description='Implementation of ImJustGood API'
)