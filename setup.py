from setuptools import setup


def readme():
    with open("README.md", "r") as fh:
        long_description = fh.read()
        return long_description


setup(
    name='gemini-pro-cli',
    version='1.1',
    packages=['gemini-pro-cli'],
    url='https://github.com/GlobalCreativeApkDev/gemini-pro-cli',
    license='MIT',
    author='GlobalCreativeApkDev',
    author_email='globalcreativeapkdev2022@gmail.com',
    description='This package contains implementation of the application enabling Gemini Pro usage '
                'on command-line interface (CLI).',
    long_description=readme(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ],
    entry_points={
        "console_scripts": [
            "gemini-pro-cli=main:main",
        ]
    }
)