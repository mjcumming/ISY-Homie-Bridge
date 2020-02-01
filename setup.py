import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='ISY994-Homie4-Bridge',
    version='0.3.2',
    description='Homie 4 for Universal Devices ISY994',
    author='Michael Cumming',
    author_email='mike@4831.com',
    long_description=long_description,
    long_description_content_type="text/markdown",      
    url='https://github.com/mjcumming/ISY-Homie-Bridge',
    keywords = ['HOMIE','MQTT','ISY994','ISY','Universal Devices','zWave','Insteon'],  
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],      
    install_requires=[
        'Homie4>=0.2.0',
        'ISY994v5>=0.6.9',
        'pyyaml',
    ],
    scripts=['isy_homie_start.py'],
    python_requires='>=3',
)
