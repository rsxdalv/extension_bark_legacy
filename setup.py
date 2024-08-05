import setuptools

setuptools.setup(
    name="extension_bark_legacy",
    packages=setuptools.find_namespace_packages(),
    version="0.0.2",
    author="rsxdalv",
    description="This is the legacy UI of Bark from TTS-Generation-WebUI",
    url="https://github.com/rsxdalv/extension_bark_legacy",
    project_urls={},
    scripts=[],
    install_requires=[
        # "suno-bark @ git+https://github.com/rsxdalv/bark@0d91823ead3d87c317f12d01d325fca9408c669e",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
