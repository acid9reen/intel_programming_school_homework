from setuptools import setup

setup(
    name="get_time_package",
    version="0.1",
    description="Show current time",
    url="",
    author="Ruslan Smirnov",
    author_email="smirnov_ruslan@outlook.com",
    license="MIT",
    packages=[
        "get_time_package",
        "pretty_print_package",
    ],
    install_requires=[
        "requests==2.26.0",
    ],
    entry_points={
        "console_scripts": [
            "get_time=get_time_package.get_time_module:main",
            "get_pretty_time=pretty_print_package.pretty_print_module:main",
        ]
    },
)
