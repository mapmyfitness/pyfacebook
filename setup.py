#!/usr/bin/env python

from distutils.core import setup
import sys

if 'sdist' in sys.argv:
    import mmf_release_tools
    version = mmf_release_tools.generate_release_version("0.1", __file__)
    mmf_release_tools.write_release_version(version)
else:
    with open("RELEASE-VERSION", "r") as f:
        version = f.readlines()[0].strip()


setup(name='pyfacebook',
      version=version,
      description='Python Client Library for the Facebook API',
      author='Samuel Cormier-Iijima',
      author_email='sciyoshi@gmail.com',
      url='http://code.google.com/p/pyfacebook',
      packages=['facebook', 'facebook.djangofb',
          'facebook.djangofb.default_app'])
