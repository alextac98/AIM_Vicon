import setuptools
from setuptools import setup, find_packages

setuptools.setup(
    name="Vicon",
    version="1.0",
    install_requires=["GaitCore @ git+https://github.com/WPI-AIM/AIM_GaitCore.git"],
    package_dir = {'': 'Vicon'},
    packages=find_packages()
    #py_modules=["Vicon", "ModelOutput", "Markers", "IMU", "ForcePlate", "EMG", "Devices", "Accel"]
)
