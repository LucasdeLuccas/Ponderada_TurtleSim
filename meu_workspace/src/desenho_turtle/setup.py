from setuptools import find_packages, setup

package_name = 'desenho_turtle'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lucasdeluccas',
    maintainer_email='lucas.luccas@sou.inteli.edu.br',
    description='Um pacote para desenhar com a tartaruga no turtlesim',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'draw = desenho_turtle.draw:main',
        ],
    },
)
