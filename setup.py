from setuptools import setup, find_packages

import onlineuser
version = onlineuser.__version__

LONG_DESCRIPTION = """
"""

setup(
    name='django-onlineuser',
    version=version,
    description="A django app to count online users.",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='onlineusers,django',
    author='vicalloy',
    author_email='zbirder@gmail.com',
    url='https://github.com/vicalloy/onlineuser/',
    license='BSD',
    packages=find_packages(),
    package_data = {
        'onlineuser': [
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
