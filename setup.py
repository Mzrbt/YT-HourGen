from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='yt-hourgen',
    version='1.0.0',
    author='Mzrbt',
    description='Generate 1-hour looped videos from YouTube',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Mzrbt/YT-HourGen',
    packages=find_packages(),
    install_requires=[
        'yt-dlp',
        'moviepy',
    ],
    entry_points={
        'console_scripts': [
            'yt-hourgen=main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)