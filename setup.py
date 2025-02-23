from setuptools import setup, find_packages

setup(
    name="fastapi_flex",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A template for FastAPI projects with state management, performance optimization, flexibility, and integration.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/fastapi_flex",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
],
)