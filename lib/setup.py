from setuptools import setup

setup(
    name='phonebook_cli',
    version='1.0',
    py_modules=['cli', 'helpers', 'db.models'],
    install_requires=[
        'Click',
        'SQLAlchemy',
        'Faker',
    ],
    entry_points='''
        [console_scripts]
        phonebook=cli:cli
    ''',
)
