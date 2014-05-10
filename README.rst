Simple natural order sorting API for Python
===========================================

The ``natsort.natsort()`` function in the ``naturalsort`` package is a very
simple alternative to Python's ``sorted()`` function that implements `natural
order sorting`_ in Python. The package is available on PyPI_, so getting
started is very simple::

   $ pip install naturalsort
   $ python
   > from natsort import natsort
   > versions = ['1.8.1-r26', '1.8.1-r30', '2.0-r2', '2.0-r7', '2.0-r11']
   > natsort(['my-package-%s' % v for v in versions])
   ['my-package-1.8.1-r26',
    'my-package-1.8.1-r30',
    'my-package-2.0-r2',
    'my-package-2.0-r7',
    'my-package-2.0-r11']

Usage
-----

Here's an example of regular sorting (based on the ASCII_ order of individual
characters) compared to `natural order sorting`_::

   > # Import the sorted() alternative.
   > from natsort import natsort
   >
   > # This is plain old sorting (what we DON'T want).
   > sorted(['1', '5', '10', '50'])
   ['1', '10', '5', '50']
   >
   > # This is natural order sorting (what we DO want).
   > natsort(['1', '5', '10', '50'])
   ['1', '5', '10', '50']

Custom comparison keys
^^^^^^^^^^^^^^^^^^^^^^

The main use case that the naturalsort_ package was originally created for is
sorting of filenames with versions numbers embedded in them. Unfortunately this
won't always work out of the box; you may need to define a custom comparison
key. Here's an example where a custom comparison key is required to get the
proper results::

   > from natsort import natsort
   > from pprint import pprint
   > versions = ['package-name_1_all.deb',
   ...           'package-name_1.5_all.deb',
   ...           'package-name_2_all.deb']

This is what happens by default::

   > pprint(natsort(versions))
   ['package-name_1.5_all.deb',
    'package-name_1_all.deb',
    'package-name_2_all.deb']

Here's how to get the right results::

   > from os.path import basename, splitext
   > def version_from_fname(filename):
   ...   filename, extension = splitext(basename(filename))
   ..    name, version, architecture = filename.split('_')
   ...   return version
   ...
   > pprint(natsort(versions, key=version_from_fname))
   ['package-name_1_all.deb',
    'package-name_1.5_all.deb',
    'package-name_2_all.deb']

Why another natsort module?!
----------------------------

The natsort_ package on PyPI is more advanced and configurable than my
naturalsort_ package, so depending on your use case you may prefer to use that
package instead. Here are the differences:

1. My naturalsort_ package implements only a small subset of the functionality
   of the natsort_ package, specifically the following calls result in the same
   sorting order:

   naturalsort package:
     ``natsort.natsort(['1-1', '1-2'])``

   natsort package:
     ``natsort.natsorted(['1-1', '1-2'], number_type=None)``

   This example shows the different goals of the two packages: The naturalsort_
   package is intended to sort version numbers while the natsort_ package by
   default interprets dashes as a negative sign and requires the keyword
   argument ``number_type=None`` to disable this behavior.

2. The naturalsort_ package works on Python 2.4 and 2.5 while the natsort_
   package requires at least Python 2.6.

Contact
-------

The latest version of naturalsort_ is available on PyPI_ and GitHub_. For
bug reports please create an issue on GitHub_. If you have questions,
suggestions, etc. feel free to send me an e-mail at `peter@peterodding.com`_.

License
-------

This software is licensed under the `MIT license`_.

© 2014 Peter Odding.

.. External references:
.. _ASCII: http://en.wikipedia.org/wiki/ASCII
.. _GitHub: https://github.com/xolox/python-naturalsort
.. _MIT license: http://en.wikipedia.org/wiki/MIT_License
.. _natsort: https://pypi.python.org/pypi/natsort
.. _natural order sorting: http://www.codinghorror.com/blog/2007/12/sorting-for-humans-natural-sort-order.htm
.. _naturalsort: https://pypi.python.org/pypi/naturalsort
.. _peter@peterodding.com: peter@peterodding.com
.. _PyPI: https://pypi.python.org/pypi/naturalsort
