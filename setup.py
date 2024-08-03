import setuptools

setuptools.setup(
    name="extension_bark_legacy",
    packages=setuptools.find_namespace_packages(),
    version="0.0.1",
    author="rsxdalv",
    description="This is the legacy UI of Bark from TTS-Generation-WebUI",
    url="https://github.com/rsxdalv/extension_bark_legacy",
    project_urls={},
    scripts=[],
    install_requires=[
        "audiocraft_apple_silicon @ git+https://github.com/rsxdalv/audiocraft@audiocraft_apple_silicon_ext",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
