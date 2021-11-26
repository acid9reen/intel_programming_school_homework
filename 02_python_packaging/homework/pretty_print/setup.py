from setuptools import setup

setup(
    name="pretty_print_package",
    version="0.1",
    description="Show current time",
    author="Ruslan Smirnov",
    author_email="smirnov_ruslan@outlook.com",
    namespace_packages=["pretty_print_namespace"],
    packages=[
        "pretty_print_namespace.pretty_print_package",
    ],
    install_requires=[
        "requests==2.26.0",
    ],
    entry_points={
        "console_scripts": [
            "get_time_pp="
            "pretty_print_namespace"
            ".pretty_print_package"
            ".pretty_print_module:main",
            "get_time="
            "pretty_print_namespace"
            ".pretty_print_package"
            ".pretty_print_module:main",
        ]
    },
)
