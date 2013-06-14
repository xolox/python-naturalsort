Simple natural order sorting API for Python that just works
===========================================================

The ``natsort.natsort()`` function in the ``naturalsort`` package is a very
simple alternative to Python's ``sorted()`` function that implements `natural
order sorting`_ in Python.

Usage
-----

Here's an example of regular sorting vs. natural order sorting::

   >>> # Import the sorted() alternative.
   >>> from natsort import natsort
   >>> 
   >>> # This is plain old sorting (what we DON'T want).
   >>> sorted(['1', '5', '10', '50'])
   ['1', '10', '5', '50']
   >>> 
   >>> # This is version sorting (what we DO want).
   >>> natsort(['1', '5', '10', '50'])
   ['1', '5', '10', '50']
   >>>
   >>> # This covers a previously fixed bug.
   >>> natsort(['1.0', '1.5'])
   ['1.0', '1.5']

Why another natsort module?!
----------------------------

There is already a ``natsort`` package available on PyPI, however this package
does not implement natural order sorting as I would expect it to work. Given
the following example it works correctly::

   >>> available_versions = ['1.8.1-r26', '1.8.1-r30', '2.0-r2', '2.0-r7', '2.0-r11']
   >>> natsort.natsorted(available_versions)
   ['1.8.1-r26', '1.8.1-r30', '2.0-r2', '2.0-r7', '2.0-r11']

However look what happens when we add a common prefix; it suddenly changes its
mind about what natural order sorting means::

   >>> natsort.natsorted(['my-package-%s' % v for v in available_versions])
   ['my-package-2.0-r2',
    'my-package-2.0-r7',
    'my-package-2.0-r11',
    'my-package-1.8.1-r26',
    'my-package-1.8.1-r30']

This last result is clearly incorrect according to reasonable expectations. The
implementation of GNU ``sort -V`` agrees with us.

Contact
-------

The latest version of ``naturalsort`` is available on PyPI_ and GitHub_. For
bug reports please create an issue on GitHub_. If you have questions,
suggestions, etc. feel free to send me an e-mail at `peter@peterodding.com`_.

License
-------

This software is licensed under the `MIT license`_.

© 2013 Peter Odding.

.. External references:
.. _GitHub: https://github.com/xolox/python-naturalsort
.. _MIT license: http://en.wikipedia.org/wiki/MIT_License
.. _natural order sorting: http://www.codinghorror.com/blog/2007/12/sorting-for-humans-natural-sort-order.htm
.. _peter@peterodding.com: peter@peterodding.com
.. _PyPI: https://pypi.python.org/pypi/naturalsort
