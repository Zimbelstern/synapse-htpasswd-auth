from setuptools import setup

setup(
    name="synapse_htpasswd_auth",
    version="1.0.0",
    author="Zimbelstern",
    url="https://github.com/Zimbelstern/synapse-htpasswd-auth",
    py_modules=['synapse_htpasswd_auth'],
    description="Htpasswd auth provider module for Matrix Synapse",
    install_requires=['matrix-synapse', 'bcrypt', 'typing']
)