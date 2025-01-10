import os
from setuptools import setup, find_packages
from setuptools.command.install import install

# Custom commands for pre- and post-install
class CustomInstallCommand(install):
    def run_before_install(self):
        print("Running before installation...")
        # Example: Create a file before installation
        with open("before_install.txt", "w") as f:
            f.write("This file was created before installation.")

    def run_after_install(self):
        print("Running after installation...")
        # Example: Create a file after installation
        with open("after_install.txt", "w") as f:
            f.write("This file was created after installation.")

    def run(self):
        self.run_before_install()
        install.run(self)
        self.run_after_install()

# Define the package
setup(
    name='gits',
    version='0.1',
    packages=find_packages(),
    cmdclass={
        'install': CustomInstallCommand,
    },
)