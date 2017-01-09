cpe_utils
=========
 
Getting Started
^^^^^^^^^^^^^^^
 
**Common Platform Enumeration** (CPE) is considered to be an industry standard that is used to provide a uniform way to show information on operating systems, hardward and software.
This tool is a collection of CPE-related utilities.

cpe_utils handles both CPE 1.0 and CPE 2.3 formats, provides functions for comparing cpes, determining if they match, and expanding a CPE that contains wildcards.

Installation
^^^^^^^^^^^^

cpe_utils can be installed from the command line as follows:

```python

    pip install cpe_utils
```

Once installed users can use the tool using the following methods.

Human Readable Representation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Human Readable method translates a Common Platform Enumeration (CPE) string to readable text.
One arguement is required as shown in the example below:

```python

    import cpe_utils

    cpe_str = "cpe:/o:microsoft:windows_8:::x64"
    cpe = cpe_utils.CPE(cpe_str)
    cpe.human()
```

Once a CPE is created the get_human method returns a single string containing the readable value.
The following translation is performed:

* Underscore character is replaced with a space
* The first letter of each section is capitalized

Returns

```python

    Microsoft Windows 8 x64
```

CPE Matching
^^^^^^^^^^^^

CPE matching can be used as follows:

* matches(self, cpe) - Compare if a CPE object exactly matches the provided cpe_obj
* has_wildcards(self) - Compare if a CPE with wildcards matches another cpe(using a provided list of reference CPEs)
* expand_cpe(cpe_str, cpe_list) - Test a cpe against a list of CPEs


**matches()**

```python

    import cpe_utils

    cpe_str1 = "cpe:/windows:microsoft:version:edition"
    cpe1 = cpe_utils.CPE(cpe_str1)
    cpe_str2 = "cpe:/linux:ubuntu:version:edition"
    cpe2 = cpe_utils.CPE(cpe_str2)
    cpe1.matches(cpe2)
```

Returns

``` python

    False
```

**has_wildcards()**

```python

    import cpe_utils

    cpe_str1 = "cpe:/*:vendor:product:version:update:edition"
    cpe1 = cpe_utils.CPE(cpe_str1)
    cpe1.has_wildcards()
```

Results

```python

    True
```
**expand_cpe(cpe_str, cpe_list)**

 
``` python

    import cpe_utils

    cpe_list = ["cpe:/o:microsoft:windows_7:::x64", "cpe:/a:mozilla:firefox:38.1.0", "cpe:/a:mozilla:firefox:38.3.0", "cpe:/a:adobe:shockwave_player:11.6.5.635", "cpe:/a:adobe:reader:11.0.10"]
    cpe_utils.expand_cpe("cpe:/a:adobe", cpe_list)
```
Results

``` python

    ['cpe:/a:adobe:shockwave_player:11.6.5.635', 'cpe:/a:adobe:reader:11.0.10']
```

to_json() and to_dict()
^^^^^^^^^^^^^^^^^^^^^^^

**JavaScript Object Notation** (JSON), is a lightweight data interchange format inspired by JavaScript object literal syntax.
The to_json() method takes a cpe string which is then translated into json syntax by using the following:
 
 * Data is represented in name/value pairs
 * Curly braces hold objects and each name is followed by ':'(colon), the name/value paris are sperated by , (commma)
 * Square brackets hold arrays and values are separted by , (comma)
 
 ```
 
    import cpe_utils

    cpe_str = "cpe:/a:something:something:"
    cpe = cpe_utils.CPE(cpe_str)
    cpe.json()
```
Returns

```python

    {"product": "something", "vendor": "something", "version": " ", "update": "", "edition": "", "part": "a"}
```

The ``to_dict()`` method creates a dictionary from a cpe string.

```python
   
    cpe_str = "cpe:/a:something:something"
    cpe = cpe_utils.CPE(cpe_str)
    cpe.to_dict()
```
Returns

```python

    {'product': 'something', 'vendor': 'something', 'version': '', 'update': '', 'edition': '', 'part': 'a'}
```