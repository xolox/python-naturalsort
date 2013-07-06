Simple natural order sorting API for Python that just works
===========================================================

The ``natsort.natsort()`` function in the ``naturalsort`` package is a very
simple alternative to Python's ``sorted()`` function that implements `natural
order sorting`_ in Python. The package is available on PyPI, so getting started
is very simple::

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

The main use case that this package was originally created for is sorting of
pathnames with versions numbers embedded in them. This is why the sorting key
defined by the ``naturalsort`` package ignores filename extensions (not doing
so can give unexpected results).

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

Why another natsort module?!
----------------------------

There was already a natsort_ package available on PyPI before I uploaded the
first release of my naturalsort_ package, so why did I upload another package
with a very similar name? Because the two packages implement different forms of
natural order sorting!

My main use case for natural order sorting has always been for sorting
filenames and pathnames, specifically those containing software version
numbers. I wrote my naturalsort_ module years ago because I couldn't find any
for Python, but never published it.

At some point I got sick of manually copying versions of my natural order
sorting module back and forth between projects so I decided to either find an
alternative available on PyPI or publish my own module. That's when I found the
natsort_ package and started using it in several projects.

At some point I got bitten in the ass because I didn't properly test the
natsort_ package for my use case. Here's a simple scenario which works as I
expect it to::

   > from natsort import natsorted
   > natsorted(['1.8.1-r26', '1.8.1-r30', '2.0-r2', '2.0-r7', '2.0-r11'])
   ['1.8.1-r26', '1.8.1-r30', '2.0-r2', '2.0-r7', '2.0-r11']

However as I said my actual use case was for sorting filenames with version
numbers embedded in them, for example::

   > from natsort import natsorted
   > versions = ['1.8.1-r26', '1.8.1-r30', '2.0-r2', '2.0-r7', '2.0-r11']
   > natsorted(['my-package-%s' % v for v in versions])
   ['my-package-2.0-r2',
    'my-package-2.0-r7',
    'my-package-2.0-r11',
    'my-package-1.8.1-r26',
    'my-package-1.8.1-r30']

This result really surprised me when I saw it for the first time, although it
is the intended result of the natsort_ package: The hyphen before the version
number is interpreted as a negative sign, which explains why 2.0 now comes
before 1.8.1.

So there's a long answer to a simple question: *the two packages do different
things*. Use the naturalsort_ package if you need to reliably sort version
numbers regardless of separators and use the natsort_ package if you need to
sort strings containing more complex numbers like floating point numbers with
negative signs and exponentials.

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
.. _ASCII: http://en.wikipedia.org/wiki/ASCII
.. _GitHub: https://github.com/xolox/python-naturalsort
.. _MIT license: http://en.wikipedia.org/wiki/MIT_License
.. _natsort: https://pypi.python.org/pypi/natsort
.. _natural order sorting: http://www.codinghorror.com/blog/2007/12/sorting-for-humans-natural-sort-order.htm
.. _naturalsort: https://pypi.python.org/pypi/naturalsort
.. _peter@peterodding.com: peter@peterodding.com
.. _PyPI: https://pypi.python.org/pypi/naturalsort
