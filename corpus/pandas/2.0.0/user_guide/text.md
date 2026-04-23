.. _text:

{{ header }}

======================
Working with text data
======================

.. _text.types:

Text data types
---------------

There are two ways to store text data in pandas:

1. ``object`` -dtype NumPy array.
2. :class:`StringDtype` extension type.

We recommend using :class:`StringDtype` to store text data.

Prior to pandas 1.0, ``object`` dtype was the only option. This was unfortunate
for many reasons:

1. You can accidentally store a *mixture* of strings and non-strings in an
   ``object`` dtype array. It's better to have a dedicated dtype.
2. ``object`` dtype breaks dtype-specific operations like :meth:`DataFrame.select_dtypes`.
   There isn't a clear way to select *just* text while excluding non-text
   but still object-dtype columns.
3. When reading code, the contents of an ``object`` dtype array is less clear
   than ``'string'``.

Currently, the performance of ``object`` dtype arrays of strings and

to significantly increase the performance and lower the memory overhead of

   ``StringArray`` is currently considered experimental. The implementation
   and parts of the API may change without warning.

For backwards-compatibility, ``object`` dtype remains the default type we
infer a list of strings to

   pd.Series(["a", "b", "c"])

To explicitly request ``string`` dtype, specify the ``dtype``

   pd.Series(["a", "b", "c"], dtype="string")
   pd.Series(["a", "b", "c"], dtype=pd.StringDtype())

Or ``astype`` after the ``Series`` or ``DataFrame`` is created

   s = pd.Series(["a", "b", "c"])
   s
   s.astype("string")

You can also use :class:`StringDtype`/``"string"`` as the dtype on non-string data and
it will be converted to ``string`` dtype:

   s = pd.Series(["a", 2, np.nan], dtype="string")
   s
   type(s[1])

or convert from existing pandas data:

   s1 = pd.Series([1, 2, np.nan], dtype="Int64")
   s1
   s2 = s1.astype("string")
   s2
   type(s2[0])

.. _text.differences:

Behavior differences
^^^^^^^^^^^^^^^^^^^^

These are places where the behavior of ``StringDtype`` objects differ from
``object`` dtype

l. For ``StringDtype``, :ref:`string accessor methods<api.series.str>`
   that return **numeric** output will always return a nullable integer dtype,
   rather than either int or float dtype, depending on the presence of NA values.
   Methods returning **boolean** output will return a nullable boolean dtype.

      s = pd.Series(["a", None, "b"], dtype="string")
      s
      s.str.count("a")
      s.dropna().str.count("a")

   Both outputs are ``Int64`` dtype. Compare that with object-dtype

      s2 = pd.Series(["a", None, "b"], dtype="object")
      s2.str.count("a")
      s2.dropna().str.count("a")

   When NA values are present, the output dtype is float64. Similarly for
   methods returning boolean values.

      s.str.isdigit()
      s.str.match("a")

2. Some string methods, like :meth:`Series.str.decode` are not available
   on ``StringArray`` because ``StringArray`` only holds strings, not
   bytes.
3. In comparison operations, :class:`arrays.StringArray` and ``Series`` backed
   by a ``StringArray`` will return an object with :class:`BooleanDtype`,
   rather than a ``bool`` dtype object. Missing values in a ``StringArray``
   will propagate in comparison operations, rather than always comparing
   unequal like :attr:`numpy.nan`.

Everything else that follows in the rest of this document applies equally to
``string`` and ``object`` dtype.

.. _text.string_methods:

String methods
--------------

Series and Index are equipped with a set of string processing methods
that make it easy to operate on each element of the array. Perhaps most
importantly, these methods exclude missing/NA values automatically. These are
accessed via the ``str`` attribute and generally have names matching
the equivalent (scalar) built-in string methods:

   s = pd.Series(
       ["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"], dtype="string"
   )
   s.str.lower()
   s.str.upper()
   s.str.len()

   idx = pd.Index([" jack", "jill ", " jesse ", "frank"])
   idx.str.strip()
   idx.str.lstrip()
   idx.str.rstrip()

The string methods on Index are especially useful for cleaning up or
transforming DataFrame columns. For instance, you may have columns with
leading or trailing whitespace:

   df = pd.DataFrame(
       np.random.randn(3, 2), columns=[" Column A ", " Column B "], index=range(3)
   )
   df

Since ``df.columns`` is an Index object, we can use the ``.str`` accessor

   df.columns.str.strip()
   df.columns.str.lower()

These string methods can then be used to clean up the columns as needed.
Here we are removing leading and trailing whitespaces, lower casing all names,
and replacing any remaining whitespaces with underscores:

   df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
   df

    If you have a ``Series`` where lots of elements are repeated
    (i.e. the number of unique elements in the ``Series`` is a lot smaller than the length of the
    ``Series``), it can be faster to convert the original ``Series`` to one of type
    ``category`` and then use ``.str.<method>`` or ``.dt.<property>`` on that.
    The performance difference comes from the fact that, for ``Series`` of type ``category``, the
    string operations are done on the ``.categories`` and not on each element of the
    ``Series``.

    Please note that a ``Series`` of type ``category`` with string ``.categories`` has
    some limitations in comparison to ``Series`` of type string (e.g. you can't add strings to
    each other: ``s + " " + s`` won't work if ``s`` is a ``Series`` of type ``category``). Also,
    ``.str`` methods which operate on elements of type ``list`` are not available on such a
    ``Series``.

.. _text.warn_types:

    Before v.0.25.0, the ``.str``-accessor did only the most rudimentary type checks. Starting with
    v.0.25.0, the type of the Series is inferred and the allowed types (i.e. strings) are enforced more rigorously.

    Generally speaking, the ``.str`` accessor is intended to work only on strings. With very few
    exceptions, other uses are not supported, and may be disabled at a later point.

.. _text.split:

Splitting and replacing strings
-------------------------------

Methods like ``split`` return a Series of lists:

   s2 = pd.Series(["a_b_c", "c_d_e", np.nan, "f_g_h"], dtype="string")
   s2.str.split("_")

Elements in the split lists can be accessed using ``get`` or ``[]`` notation:

   s2.str.split("_").str.get(1)
   s2.str.split("_").str[1]

It is easy to expand this to return a DataFrame using ``expand``.

   s2.str.split("_", expand=True)

When original ``Series`` has :class:`StringDtype`, the output columns will all
be :class:`StringDtype` as well.

It is also possible to limit the number of splits:

   s2.str.split("_", expand=True, n=1)

``rsplit`` is similar to ``split`` except it works in the reverse direction,
i.e., from the end of the string to the beginning of the string:

   s2.str.rsplit("_", expand=True, n=1)

``replace`` optionally uses `regular expressions
<https://docs.python.org/3/library/re.html>`__:

   s3 = pd.Series(
       ["A", "B", "C", "Aaba", "Baca", "", np.nan, "CABA", "dog", "cat"],
       dtype="string",
   )
   s3
   s3.str.replace("^.a|dog", "XX-XX ", case=False, regex=True)

Single character pattern with ``regex=True`` will also be treated as regular expressions:

   s4 = pd.Series(["a.b", ".", "b", np.nan, ""], dtype="string")
   s4
   s4.str.replace(".", "a", regex=True)

If you want literal replacement of a string (equivalent to :meth:`str.replace`), you
can set the optional ``regex`` parameter to ``False``, rather than escaping each
character. In this case both ``pat`` and ``repl`` must be strings:

    dollars = pd.Series(["12", "-$10", "$10,000"], dtype="string")

    # These lines are equivalent
    dollars.str.replace(r"-\$", "-", regex=True)
    dollars.str.replace("-$", "-", regex=False)

The ``replace`` method can also take a callable as replacement. It is called
on every ``pat`` using :func:`re.sub`. The callable should expect one
positional argument (a regex object) and return a string.

   # Reverse every lowercase alphabetic word
   pat = r"[a-z]+"

   def repl(m):
       return m.group(0)[::-1]

   pd.Series(["foo 123", "bar baz", np.nan], dtype="string").str.replace(
       pat, repl, regex=True
   )

   # Using regex groups
   pat = r"(?P<one>\w+) (?P<two>\w+) (?P<three>\w+)"

   def repl(m):
       return m.group("two").swapcase()

   pd.Series(["Foo Bar Baz", np.nan], dtype="string").str.replace(
       pat, repl, regex=True
   )

The ``replace`` method also accepts a compiled regular expression object
from :func:`re.compile` as a pattern. All flags should be included in the
compiled regular expression object.

   import re

   regex_pat = re.compile(r"^.a|dog", flags=re.IGNORECASE)
   s3.str.replace(regex_pat, "XX-XX ", regex=True)

Including a ``flags`` argument when calling ``replace`` with a compiled
regular expression object will raise a ``ValueError``.

    @verbatim
    In [1]: s3.str.replace(regex_pat, 'XX-XX ', flags=re.IGNORECASE)
    ---------------------------------------------------------------------------
    ValueError: case and flags cannot be set when pat is a compiled regex

``removeprefix`` and ``removesuffix`` have the same effect as ``str.removeprefix`` and ``str.removesuffix`` added in Python 3.9
<https://docs.python.org/3/library/stdtypes.html#str.removeprefix>`__:

   s = pd.Series(["str_foo", "str_bar", "no_prefix"])
   s.str.removeprefix("str_")

   s = pd.Series(["foo_str", "bar_str", "no_suffix"])
   s.str.removesuffix("_str")

.. _text.concatenate:

Concatenation
-------------

There are several ways to concatenate a ``Series`` or ``Index``, either with itself or others, all based on :meth:`~Series.str.cat`,
resp. ``Index.str.cat``.

Concatenating a single Series into a string
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The content of a ``Series`` (or ``Index``) can be concatenated:

    s = pd.Series(["a", "b", "c", "d"], dtype="string")
    s.str.cat(sep=",")

If not specified, the keyword ``sep`` for the separator defaults to the empty string, ``sep=''``:

    s.str.cat()

By default, missing values are ignored. Using ``na_rep``, they can be given a representation:

    t = pd.Series(["a", "b", np.nan, "d"], dtype="string")
    t.str.cat(sep=",")
    t.str.cat(sep=",", na_rep="-")

Concatenating a Series and something list-like into a Series
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first argument to :meth:`~Series.str.cat` can be a list-like object, provided that it matches the length of the calling ``Series`` (or ``Index``).

    s.str.cat(["A", "B", "C", "D"])

Missing values on either side will result in missing values in the result as well, *unless* ``na_rep`` is specified:

    s.str.cat(t)
    s.str.cat(t, na_rep="-")

Concatenating a Series and something array-like into a Series
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The parameter ``others`` can also be two-dimensional. In this case, the number or rows must match the lengths of the calling ``Series`` (or ``Index``).

    d = pd.concat([t, s], axis=1)
    s
    d
    s.str.cat(d, na_rep="-")

Concatenating a Series and an indexed object into a Series, with alignment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For concatenation with a ``Series`` or ``DataFrame``, it is possible to align the indexes before concatenation by setting
the ``join``-keyword.

   u = pd.Series(["b", "d", "a", "c"], index=[1, 3, 0, 2], dtype="string")
   s
   u
   s.str.cat(u)
   s.str.cat(u, join="left")

    If the ``join`` keyword is not passed, the method :meth:`~Series.str.cat` will currently fall back to the behavior before version 0.23.0 (i.e. no alignment),
    but a ``FutureWarning`` will be raised if any of the involved indexes differ, since this default will change to ``join='left'`` in a future version.

The usual options are available for ``join`` (one of ``'left', 'outer', 'inner', 'right'``).
In particular, alignment also means that the different lengths do not need to coincide anymore.

    v = pd.Series(["z", "a", "b", "d", "e"], index=[-1, 0, 1, 3, 4], dtype="string")
    s
    v
    s.str.cat(v, join="left", na_rep="-")
    s.str.cat(v, join="outer", na_rep="-")

The same alignment can be used when ``others`` is a ``DataFrame``:

    f = d.loc[[3, 2, 1, 0], :]
    s
    f
    s.str.cat(f, join="left", na_rep="-")

Concatenating a Series and many objects into a Series
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Several array-like items (specifically: ``Series``, ``Index``, and 1-dimensional variants of ``np.ndarray``)
can be combined in a list-like container (including iterators, ``dict``-views, etc.).

    s
    u
    s.str.cat([u, u.to_numpy()], join="left")

All elements without an index (e.g. ``np.ndarray``) within the passed list-like must match in length to the calling ``Series`` (or ``Index``),
but ``Series`` and ``Index`` may have arbitrary length (as long as alignment is not disabled with ``join=None``):

    v
    s.str.cat([v, u, u.to_numpy()], join="outer", na_rep="-")

If using ``join='right'`` on a list-like of ``others`` that contains different indexes,
the union of these indexes will be used as the basis for the final concatenation:

    u.loc[[3]]
    v.loc[[-1, 0]]
    s.str.cat([u.loc[[3]], v.loc[[-1, 0]]], join="right", na_rep="-")

Indexing with ``.str``
----------------------

.. _text.indexing:

You can use ``[]`` notation to directly index by position locations. If you index past the end
of the string, the result will be a ``NaN``.

   s = pd.Series(
       ["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"], dtype="string"
   )

   s.str[0]
   s.str[1]

Extracting substrings
---------------------

.. _text.extract:

Extract first match in each subject (extract)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Before version 0.23, argument ``expand`` of the ``extract`` method defaulted to
   ``False``. When ``expand=False``, ``expand`` returns a ``Series``, ``Index``, or
   ``DataFrame``, depending on the subject and regular expression
   pattern. When ``expand=True``, it always returns a ``DataFrame``,
   which is more consistent and less confusing from the perspective of a user.
   ``expand=True`` has been the default since version 0.23.0.

The ``extract`` method accepts a `regular expression
<https://docs.python.org/3/library/re.html>`__ with at least one
capture group.

Extracting a regular expression with more than one group returns a
DataFrame with one column per group.

   pd.Series(
       ["a1", "b2", "c3"],
       dtype="string",
   ).str.extract(r"([ab])(\d)", expand=False)

Elements that do not match return a row filled with ``NaN``. Thus, a
Series of messy strings can be "converted" into a like-indexed Series
or DataFrame of cleaned-up or more useful strings, without
necessitating ``get()`` to access tuples or ``re.match`` objects. The
dtype of the result is always object, even if no match is found and
the result only contains ``NaN``.

Named groups like

   pd.Series(["a1", "b2", "c3"], dtype="string").str.extract(
       r"(?P<letter>[ab])(?P<digit>\d)", expand=False
   )

and optional groups like

   pd.Series(
       ["a1", "b2", "3"],
       dtype="string",
   ).str.extract(r"([ab])?(\d)", expand=False)

can also be used. Note that any capture group names in the regular
expression will be used for column names; otherwise capture group
numbers will be used.

Extracting a regular expression with one group returns a ``DataFrame``
with one column if ``expand=True``.

   pd.Series(["a1", "b2", "c3"], dtype="string").str.extract(r"[ab](\d)", expand=True)

It returns a Series if ``expand=False``.

   pd.Series(["a1", "b2", "c3"], dtype="string").str.extract(r"[ab](\d)", expand=False)

Calling on an ``Index`` with a regex with exactly one capture group
returns a ``DataFrame`` with one column if ``expand=True``.

   s = pd.Series(["a1", "b2", "c3"], ["A11", "B22", "C33"], dtype="string")
   s
   s.index.str.extract("(?P<letter>[a-zA-Z])", expand=True)

It returns an ``Index`` if ``expand=False``.

   s.index.str.extract("(?P<letter>[a-zA-Z])", expand=False)

Calling on an ``Index`` with a regex with more than one capture group
returns a ``DataFrame`` if ``expand=True``.

   s.index.str.extract("(?P<letter>[a-zA-Z])([0-9]+)", expand=True)

It raises ``ValueError`` if ``expand=False``.

.. code-block:: python

    >>> s.index.str.extract("(?P<letter>[a-zA-Z])([0-9]+)", expand=False)
    ValueError: only one regex group is supported with Index

The table below summarizes the behavior of ``extract(expand=False)``
(input subject in first column, number of groups in regex in
first row)

+--------+---------+------------+
|        | 1 group | >1 group   |
+--------+---------+------------+
| Index  | Index   | ValueError |
+--------+---------+------------+
| Series | Series  | DataFrame  |
+--------+---------+------------+

Extract all matches in each subject (extractall)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _text.extractall:

Unlike ``extract`` (which returns only the first match),

   s = pd.Series(["a1a2", "b1", "c1"], index=["A", "B", "C"], dtype="string")
   s
   two_groups = "(?P<letter>[a-z])(?P<digit>[0-9])"
   s.str.extract(two_groups, expand=True)

the ``extractall`` method returns every match. The result of
``extractall`` is always a ``DataFrame`` with a ``MultiIndex`` on its
rows. The last level of the ``MultiIndex`` is named ``match`` and
indicates the order in the subject.

   s.str.extractall(two_groups)

When each subject string in the Series has exactly one match,

   s = pd.Series(["a3", "b3", "c2"], dtype="string")
   s

then ``extractall(pat).xs(0, level='match')`` gives the same result as
``extract(pat)``.

   extract_result = s.str.extract(two_groups, expand=True)
   extract_result
   extractall_result = s.str.extractall(two_groups)
   extractall_result
   extractall_result.xs(0, level="match")

``Index`` also supports ``.str.extractall``. It returns a ``DataFrame`` which has the
same result as a ``Series.str.extractall`` with a default index (starts from 0).

   pd.Index(["a1a2", "b1", "c1"]).str.extractall(two_groups)

   pd.Series(["a1a2", "b1", "c1"], dtype="string").str.extractall(two_groups)

Testing for strings that match or contain a pattern
---------------------------------------------------

You can check whether elements contain a pattern:

   pattern = r"[0-9][a-z]"
   pd.Series(
       ["1", "2", "3a", "3b", "03c", "4dx"],
       dtype="string",
   ).str.contains(pattern)

Or whether elements match a pattern:

   pd.Series(
       ["1", "2", "3a", "3b", "03c", "4dx"],
       dtype="string",
   ).str.match(pattern)

   pd.Series(
       ["1", "2", "3a", "3b", "03c", "4dx"],
       dtype="string",
   ).str.fullmatch(pattern)

    The distinction between ``match``, ``fullmatch``, and ``contains`` is strictness:
    ``fullmatch`` tests whether the entire string matches the regular expression;
    ``match`` tests whether there is a match of the regular expression that begins
    at the first character of the string; and ``contains`` tests whether there is
    a match of the regular expression at any position within the string.

    The corresponding functions in the ``re`` package for these three match modes are
    `re.fullmatch <https://docs.python.org/3/library/re.html#re.fullmatch>`_,
    `re.match <https://docs.python.org/3/library/re.html#re.match>`_, and
    `re.search <https://docs.python.org/3/library/re.html#re.search>`_,
    respectively.

Methods like ``match``, ``fullmatch``, ``contains``, ``startswith``, and
``endswith`` take an extra ``na`` argument so missing values can be considered
True or False:

   s4 = pd.Series(
       ["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"], dtype="string"
   )
   s4.str.contains("A", na=False)

.. _text.indicator:

Creating indicator variables
----------------------------

You can extract dummy variables from string columns.
For example if they are separated by a ``'|'``:

    s = pd.Series(["a", "a|b", np.nan, "a|c"], dtype="string")
    s.str.get_dummies(sep="|")

String ``Index`` also supports ``get_dummies`` which returns a ``MultiIndex``.

    idx = pd.Index(["a", "a|b", np.nan, "a|c"])
    idx.str.get_dummies(sep="|")

See also :func:`~pandas.get_dummies`.

Method summary
--------------

.. _text.summary:

.. csv-table::
