from setuptools import setup, find_packages

setup(
    name='transcoder',
    version='0.1',
    packages=find_packages(),
    install_requires=['ffmpeg-python'],
    description='An advanced Python package for video transcoding',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/transcoder',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
