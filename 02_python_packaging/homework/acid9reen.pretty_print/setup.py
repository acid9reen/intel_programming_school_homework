from setuptools import setup

setup(
    name="pretty_print_package",
    version="0.1",
    description="Show current time",
    author="Ruslan Smirnov",
    author_email="smirnov_ruslan@outlook.com",
    packages=[
        "acid9reen.pretty_print_package",
    ],
    install_requires=[
        "requests==2.26.0",
    ],
    entry_points={
        "console_scripts": [
            "get_time_pp=acid9reen.pretty_print_package.__main__:main",
        ]
    },
)
