from setuptools import setup
from setuptools.command.install import install
n='gits'
class cic(install):
    def before(self):
        pass
    def after(self):
        pass
    def run(self):
        self.before()
        install.run(self)
        self.after()
setup(
    name=n,
    version='1.3',
    packages=[n],
    cmdclass={
        'install': cic,
    },
)