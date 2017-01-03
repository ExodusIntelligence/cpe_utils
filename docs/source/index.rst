.. cpe_utils documentation master file, created by
   sphinx-quickstart on Wed Dec 14 11:42:49 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

cpe_utils
=========

Getting Started
^^^^^^^^^^^^^^^

This is a paragraph.

Here is some code, and this is ``inline mono-space text``

.. code-block:: python


    import cpe_utils
   
    cpe_str = "cpe:/a:something"
    cpe = cpe_utils.CPE(cpe_str)
    

Self.vendor is parsed from the cpe_str:

* list item
* list item
* list item

Human Readable Representation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Human Readable method translates a ''Common Platform Enumeration'' (CPE) string to readable text.
One arguement is required as shown in the example below:

.. code-block:: python

    import cpe_utils

    cpe_str = "cpe:/o:microsoft:windows_8:::x64"
    cpe = cpe_utils.CPE(cpe_str)   
    >>> cpe.human()

Once a CPE is created the ''get_human'' method returns a single string containing the readable value.
The following translation is performed:

* Underscore character is replaced with a space
* The first letter of each section is capitalized

Returns

.. code-block:: python 
    
    >>> Microsoft Windows 8 x64



^^^^^^^^^^^^

This is a paragraph.

Here is some code, and this is ``inline mono-space text``

.. code-block:: python

    import cpe_utils

    cpe_str = "cpe:/a:something"
    cpe = cpe_utils.CPE(cpe_str)

Blah blah blah

* list item
* list item
* list item

to_json() and to_dict()
^^^^^^^^^^^^^^^^^^^^^^^

``JavaScript Object Notation`` (JSON), is a lightweight data interchange format inspired by JavaScript object literal syntax.
The ``to_json()`` method takes a cpe string which is then translated into json syntax by using the following:

 * Data is represented in name/value pairs
 * Curly braces hold objects and each name is followed by ':'(colon), the name/value paris are sperated by , (commma)
 * Square brackets hold arrays and values are separted by , (comma)

.. code-block:: python

    import cpe_utils

    cpe_str = "cpe:/a:something:something:"
    cpe = cpe_utils.CPE(cpe_str)
    cpe.json()

Returns

.. code-block:: python

    {"product": "something", "vendor": "something", "version": " ", "update": "", "edition": "", "part": "a"}


The ``to_dict()`` method creates a dictionary from a cpe string.

.. code-block:: python
    
    cpe_str = "cpe:/a:something:something"
    cpe = cpe_utils.CPE(cpe_str)
    cpe.to_dict()

Returns

.. code-block:: python

    {'product': 'something', 'vendor': 'something', 'version': '', 'update': '', 'edition': '', 'part': 'a'}





Contents
#########

.. toctree::
   :maxdepth: 2

.. automodule:: cpe_utils
   :members:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

