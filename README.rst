Simple natural order sorting API for Python that just works
===========================================================

The ``natsort`` class in the ``naturalsort`` module is a very simple
alternative to Python's ``sorted()`` function that implements natural order
sorting in Python.

Usage
-----

Here's an example of regular sorting vs. natural order sorting::

   >>> # Import the sorted() alternative.
   >>> from natsort import natsort
   >>> 
   >>> # This is plain old sorting (what we don't want).
   >>> sorted(['1', '5', '10', '50'])
   ['1', '10', '5', '50']
   >>> 
   >>> # This is version sorting (what we're after).
   >>> natsort(['1', '5', '10', '50'])
   ['1', '5', '10', '50']
   >>>
   >>> # This covers a previously fixed bug.
   >>> natsort(['1.0', '1.5'])
   ['1.0', '1.5']

Contact
-------

The latest version of ``naturalsort`` is available on PyPi_ and GitHub_. For
bug reports please create an issue on GitHub_. If you have questions,
suggestions, etc. feel free to send me an e-mail at `peter@peterodding.com`_.

License
-------

This software is licensed under the `MIT license`_.

© 2013 Peter Odding.

.. External references:
.. _GitHub: https://github.com/xolox/python-naturalsort
.. _MIT license: http://en.wikipedia.org/wiki/MIT_License
.. _peter@peterodding.com: peter@peterodding.com
.. _PyPi: https://pypi.python.org/pypi/naturalsort
