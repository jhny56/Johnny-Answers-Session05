import os
from setuptools import find_packages, setup
from glob import glob

package_name = 'temperature_monitor'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='robot',
    # maintainer_email='no',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'temperature_publisher = temperature_monitor.temperature_publisher:main',
            'threshold_subscriber = temperature_monitor.threshold_subscriber:main',
            'alert_publisher = temperature_monitor.alert_publisher:main',
            'temperature_logger = temperature_monitor.temperature_logger:main',
        ],
    },
)
