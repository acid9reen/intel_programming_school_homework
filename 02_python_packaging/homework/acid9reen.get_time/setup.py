from setuptools import setup

setup(
    name="get_time_package",
    version="0.1",
    description="Show current time",
    author="Ruslan Smirnov",
    author_email="smirnov_ruslan@outlook.com",
    packages=[
        "acid9reen.get_time_package",
    ],
    install_requires=[
        "requests==2.26.0",
    ],
    entry_points={
        "console_scripts": [
            "get_time=acid9reen.get_time_package.get_time_module:main",
        ]
    },
)
