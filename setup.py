from setuptools import setup, version

setup(
    name='pm',
    version='0.1',
    py_modules=['pv'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pm=pm:cli
    ''',
)