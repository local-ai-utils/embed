from setuptools import setup, find_packages

setup(
    name="local-ai-utils-embed",
    version="0.0.1",
    packages=['embed'],
    package_dir={"embed": "embed"},
    entry_points={
        'console_scripts': [
            'embed=embed.cli:main',
        ],
    },
    install_requires=[
        'fire',
    ],
)