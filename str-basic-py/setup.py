'''
setup.py: El archivo de configuración para empaquetar el proyecto, necesario si piensas distribuirlo
o instalarlo como un paquete Python. Define las dependencias y metadatos del paquete.
'''


from setuptools import setup, find_packages

setup(
    name='mi_proyecto',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # Aquí van las dependencias de tu proyecto
    ],
)