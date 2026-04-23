.. _advanced:

{{ header }}

******************************
MultiIndex / advanced indexing
******************************

This section covers :ref:`indexing with a MultiIndex <advanced.hierarchical>`
and :ref:`other advanced indexing features <advanced.index_types>`.

See the :ref:`Indexing and Selecting Data <indexing>` for general indexing documentation.

   Whether a copy or a reference is returned for a setting operation may
   depend on the context.  This is sometimes called ``chained assignment`` and
   should be avoided.  See :ref:`Returning a View versus Copy
   <indexing.view_versus_copy>`.

See the :ref:`cookbook<cookbook.selection>` for some advanced strategies.

.. _advanced.hierarchical:

Hierarchical indexing (MultiIndex)
----------------------------------

Hierarchical / Multi-level indexing is very exciting as it opens the door to some
quite sophisticated data analysis and manipulation, especially for working with
higher dimensional data. In essence, it enables you to store and manipulate
data with an arbitrary number of dimensions in lower dimensional data
structures like ``Series`` (1d) and ``DataFrame`` (2d).

In this section, we will show what exactly we mean by "hierarchical" indexing
and how it integrates with all of the pandas indexing functionality
described above and in prior sections. Later, when discussing :ref:`group by
<groupby>` and :ref:`pivoting and reshaping data <reshaping>`, we'll show
non-trivial applications to illustrate how it aids in structuring data for
analysis.

See the :ref:`cookbook<cookbook.multi_index>` for some advanced strategies.

Creating a MultiIndex (hierarchical index) object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :class:`MultiIndex` object is the hierarchical analogue of the standard

can think of ``MultiIndex`` as an array of tuples where each tuple is unique. A
``MultiIndex`` can be created from a list of arrays (using

a ``MultiIndex`` when it is passed a list of tuples.  The following examples
demonstrate different ways to initialize MultiIndexes.

   arrays = [
       ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
       ["one", "two", "one", "two", "one", "two", "one", "two"],
   ]
   tuples = list(zip(*arrays))
   tuples

   index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
   index

   s = pd.Series(np.random.randn(8), index=index)
   s

When you want every pairing of the elements in two iterables, it can be easier
to use the :meth:`MultiIndex.from_product` method:

   iterables = [["bar", "baz", "foo", "qux"], ["one", "two"]]
   pd.MultiIndex.from_product(iterables, names=["first", "second"])

You can also construct a ``MultiIndex`` from a ``DataFrame`` directly, using
the method :meth:`MultiIndex.from_frame`. This is a complementary method to

   df = pd.DataFrame(
       [["bar", "one"], ["bar", "two"], ["foo", "one"], ["foo", "two"]],
       columns=["first", "second"],
   )
   pd.MultiIndex.from_frame(df)

As a convenience, you can pass a list of arrays directly into ``Series`` or
``DataFrame`` to construct a ``MultiIndex`` automatically:

   arrays = [
       np.array(["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"]),
       np.array(["one", "two", "one", "two", "one", "two", "one", "two"]),
   ]
   s = pd.Series(np.random.randn(8), index=arrays)
   s
   df = pd.DataFrame(np.random.randn(8, 4), index=arrays)
   df

All of the ``MultiIndex`` constructors accept a ``names`` argument which stores
string names for the levels themselves. If no names are provided, ``None`` will
be assigned:

   df.index.names

This index can back any axis of a pandas object, and the number of **levels**
of the index is up to you:

   df = pd.DataFrame(np.random.randn(3, 8), index=["A", "B", "C"], columns=index)
   df
   pd.DataFrame(np.random.randn(6, 6), index=index[:6], columns=index[:6])

We've "sparsified" the higher levels of the indexes to make the console output a
bit easier on the eyes. Note that how the index is displayed can be controlled using the
``multi_sparse`` option in ``pandas.set_options()``:

   with pd.option_context("display.multi_sparse", False):
       df

It's worth keeping in mind that there's nothing preventing you from using
tuples as atomic labels on an axis:

   pd.Series(np.random.randn(8), index=tuples)

The reason that the ``MultiIndex`` matters is that it can allow you to do
grouping, selection, and reshaping operations as we will describe below and in
subsequent areas of the documentation. As you will see in later sections, you
can find yourself working with hierarchically-indexed data without creating a
``MultiIndex`` explicitly yourself. However, when loading data from a file, you
may wish to generate your own ``MultiIndex`` when preparing the data set.

.. _advanced.get_level_values:

Reconstructing the level labels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The method :meth:`~MultiIndex.get_level_values` will return a vector of the labels for each
location at a particular level:

   index.get_level_values(0)
   index.get_level_values("second")

Basic indexing on axis with MultiIndex
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One of the important features of hierarchical indexing is that you can select
data by a "partial" label identifying a subgroup in the data. **Partial**
selection "drops" levels of the hierarchical index in the result in a
completely analogous way to selecting a column in a regular DataFrame:

   df["bar"]
   df["bar", "one"]
   df["bar"]["one"]
   s["qux"]

See :ref:`Cross-section with hierarchical index <advanced.xs>` for how to select
on a deeper level.

.. _advanced.shown_levels:

Defined levels
~~~~~~~~~~~~~~

The :class:`MultiIndex` keeps all the defined levels of an index, even
if they are not actually used. When slicing an index, you may notice this.
For example:

   df.columns.levels  # original MultiIndex

   df[["foo","qux"]].columns.levels  # sliced

This is done to avoid a recomputation of the levels in order to make slicing
highly performant. If you want to see only the used levels, you can use the

   df[["foo", "qux"]].columns.to_numpy()

   # for a specific level
   df[["foo", "qux"]].columns.get_level_values(0)

To reconstruct the ``MultiIndex`` with only the used levels, the

   new_mi = df[["foo", "qux"]].columns.remove_unused_levels()
   new_mi.levels

Data alignment and using ``reindex``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Operations between differently-indexed objects having ``MultiIndex`` on the
axes will work as you expect; data alignment will work the same as an Index of
tuples:

   s + s[:-2]
   s + s[::2]

The :meth:`~DataFrame.reindex` method of ``Series``/``DataFrames`` can be
called with another ``MultiIndex``, or even a list or array of tuples:

   s.reindex(index[:3])
   s.reindex([("foo", "two"), ("bar", "one"), ("qux", "one"), ("baz", "one")])

.. _advanced.advanced_hierarchical:

Advanced indexing with hierarchical index
-----------------------------------------

Syntactically integrating ``MultiIndex`` in advanced indexing with ``.loc`` is a
bit challenging, but we've made every effort to do so. In general, MultiIndex
keys take the form of tuples. For example, the following works as you would expect:

   df = df.T
   df
   df.loc[("bar", "two")]

Note that ``df.loc['bar', 'two']`` would also work in this example, but this shorthand
notation can lead to ambiguity in general.

If you also want to index a specific column with ``.loc``, you must use a tuple
like this:

   df.loc[("bar", "two"), "A"]

You don't have to specify all levels of the ``MultiIndex`` by passing only the
first elements of the tuple. For example, you can use "partial" indexing to
get all elements with ``bar`` in the first level as follows:

   df.loc["bar"]

This is a shortcut for the slightly more verbose notation ``df.loc[('bar',),]`` (equivalent
to ``df.loc['bar',]`` in this example).

"Partial" slicing also works quite nicely.

   df.loc["baz":"foo"]

You can slice with a 'range' of values, by providing a slice of tuples.

   df.loc[("baz", "two"):("qux", "one")]
   df.loc[("baz", "two"):"foo"]

Passing a list of labels or tuples works similar to reindexing:

   df.loc[[("bar", "two"), ("qux", "one")]]

   It is important to note that tuples and lists are not treated identically
   in pandas when it comes to indexing. Whereas a tuple is interpreted as one
   multi-level key, a list is used to specify several keys. Or in other words,
   tuples go horizontally (traversing levels), lists go vertically (scanning levels).

Importantly, a list of tuples indexes several complete ``MultiIndex`` keys,
whereas a tuple of lists refer to several values within a level:

   s = pd.Series(
       [1, 2, 3, 4, 5, 6],
       index=pd.MultiIndex.from_product([["A", "B"], ["c", "d", "e"]]),
   )
   s.loc[[("A", "c"), ("B", "d")]]  # list of tuples
   s.loc[(["A", "B"], ["c", "d"])]  # tuple of lists

.. _advanced.mi_slicers:

Using slicers
~~~~~~~~~~~~~

You can slice a ``MultiIndex`` by providing multiple indexers.

You can provide any of the selectors as if you are indexing by label, see :ref:`Selection by Label <indexing.label>`,
including slices, lists of labels, labels, and boolean indexers.

You can use ``slice(None)`` to select all the contents of *that* level. You do not need to specify all the
*deeper* levels, they will be implied as ``slice(None)``.

As usual, **both sides** of the slicers are included as this is label indexing.

   You should specify all axes in the ``.loc`` specifier, meaning the indexer for the **index** and
   for the **columns**. There are some ambiguous cases where the passed indexer could be mis-interpreted
   as indexing *both* axes, rather than into say the ``MultiIndex`` for the rows.

   You should do this:

   .. code-block:: python

      df.loc[(slice("A1", "A3"), ...), :]  # noqa: E999

   You should **not** do this:
 
   .. code-block:: python

      df.loc[(slice("A1", "A3"), ...)]  # noqa: E999

   def mklbl(prefix, n):
       return ["%s%s" % (prefix, i) for i in range(n)]

   miindex = pd.MultiIndex.from_product(
       [mklbl("A", 4), mklbl("B", 2), mklbl("C", 4), mklbl("D", 2)]
   )
   micolumns = pd.MultiIndex.from_tuples(
       [("a", "foo"), ("a", "bar"), ("b", "foo"), ("b", "bah")], names=["lvl0", "lvl1"]
   )
   dfmi = (
       pd.DataFrame(
           np.arange(len(miindex) * len(micolumns)).reshape(
               (len(miindex), len(micolumns))
           ),
           index=miindex,
           columns=micolumns,
       )
       .sort_index()
       .sort_index(axis=1)
   )
   dfmi

Basic MultiIndex slicing using slices, lists, and labels.

   dfmi.loc[(slice("A1", "A3"), slice(None), ["C1", "C3"]), :]

You can use :class:`pandas.IndexSlice` to facilitate a more natural syntax
using ``:``, rather than using ``slice(None)``.

   idx = pd.IndexSlice
   dfmi.loc[idx[:, :, ["C1", "C3"]], idx[:, "foo"]]

It is possible to perform quite complicated selections using this method on multiple
axes at the same time.

   dfmi.loc["A1", (slice(None), "foo")]
   dfmi.loc[idx[:, :, ["C1", "C3"]], idx[:, "foo"]]

Using a boolean indexer you can provide selection related to the *values*.

   mask = dfmi[("a", "foo")] > 200
   dfmi.loc[idx[mask, :, ["C1", "C3"]], idx[:, "foo"]]

You can also specify the ``axis`` argument to ``.loc`` to interpret the passed
slicers on a single axis.

   dfmi.loc(axis=0)[:, :, ["C1", "C3"]]

Furthermore, you can *set* the values using the following methods.

   df2 = dfmi.copy()
   df2.loc(axis=0)[:, :, ["C1", "C3"]] = -10
   df2

You can use a right-hand-side of an alignable object as well.

   df2 = dfmi.copy()
   df2.loc[idx[:, :, ["C1", "C3"]], :] = df2 * 1000
   df2

.. _advanced.xs:

Cross-section
~~~~~~~~~~~~~

The :meth:`~DataFrame.xs` method of ``DataFrame`` additionally takes a level argument to make
selecting data at a particular level of a ``MultiIndex`` easier.

   df
   df.xs("one", level="second")

   # using the slicers
   df.loc[(slice(None), "one"), :]

You can also select on the columns with ``xs``, by
providing the axis argument.

   df = df.T
   df.xs("one", level="second", axis=1)

   # using the slicers
   df.loc[:, (slice(None), "one")]

``xs`` also allows selection with multiple keys.

   df.xs(("one", "bar"), level=("second", "first"), axis=1)

   # using the slicers
   df.loc[:, ("bar", "one")]

You can pass ``drop_level=False`` to ``xs`` to retain
the level that was selected.

   df.xs("one", level="second", axis=1, drop_level=False)

Compare the above with the result using ``drop_level=True`` (the default value).

   df.xs("one", level="second", axis=1, drop_level=True)

   df = df.T

.. _advanced.advanced_reindex:

Advanced reindexing and alignment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using the parameter ``level`` in the :meth:`~DataFrame.reindex` and

values across a level. For instance:

   midx = pd.MultiIndex(
       levels=[["zero", "one"], ["x", "y"]], codes=[[1, 1, 0, 0], [1, 0, 1, 0]]
   )
   df = pd.DataFrame(np.random.randn(4, 2), index=midx)
   df
   df2 = df.groupby(level=0).mean()
   df2
   df2.reindex(df.index, level=0)

   # aligning
   df_aligned, df2_aligned = df.align(df2, level=0)
   df_aligned
   df2_aligned

Swapping levels with ``swaplevel``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :meth:`~MultiIndex.swaplevel` method can switch the order of two levels:

   df[:5]
   df[:5].swaplevel(0, 1, axis=0)

.. _advanced.reorderlevels:

Reordering levels with ``reorder_levels``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :meth:`~MultiIndex.reorder_levels` method generalizes the ``swaplevel``
method, allowing you to permute the hierarchical index levels in one step:

   df[:5].reorder_levels([1, 0], axis=0)

.. _advanced.index_names:

Renaming names of an ``Index`` or ``MultiIndex``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :meth:`~DataFrame.rename` method is used to rename the labels of a
``MultiIndex``, and is typically used to rename the columns of a ``DataFrame``.
The ``columns`` argument of ``rename`` allows a dictionary to be specified
that includes only the columns you wish to rename.

   df.rename(columns={0: "col0", 1: "col1"})

This method can also be used to rename specific labels of the main index
of the ``DataFrame``.

   df.rename(index={"one": "two", "y": "z"})

The :meth:`~DataFrame.rename_axis` method is used to rename the name of a
``Index`` or ``MultiIndex``. In particular, the names of the levels of a
``MultiIndex`` can be specified, which is useful if ``reset_index()`` is later
used to move the values from the ``MultiIndex`` to a column.

   df.rename_axis(index=["abc", "def"])

Note that the columns of a ``DataFrame`` are an index, so that using
``rename_axis`` with the ``columns`` argument will change the name of that
index.

   df.rename_axis(columns="Cols").columns

Both ``rename`` and ``rename_axis`` support specifying a dictionary,
``Series`` or a mapping function to map labels/names to new values.

When working with an ``Index`` object directly, rather than via a ``DataFrame``,

   mi = pd.MultiIndex.from_product([[1, 2], ["a", "b"]], names=["x", "y"])
   mi.names

   mi2 = mi.rename("new name", level=0)
   mi2

You cannot set the names of the MultiIndex via a level.

   mi.levels[0].name = "name via level"

Use :meth:`Index.set_names` instead.

Sorting a ``MultiIndex``
------------------------

For :class:`MultiIndex`-ed objects to be indexed and sliced effectively,
they need to be sorted. As with any index, you can use :meth:`~DataFrame.sort_index`.

   import random

   random.shuffle(tuples)
   s = pd.Series(np.random.randn(8), index=pd.MultiIndex.from_tuples(tuples))
   s
   s.sort_index()
   s.sort_index(level=0)
   s.sort_index(level=1)

.. _advanced.sortlevel_byname:

You may also pass a level name to ``sort_index`` if the ``MultiIndex`` levels
are named.

   s.index = s.index.set_names(["L1", "L2"])
   s.sort_index(level="L1")
   s.sort_index(level="L2")

On higher dimensional objects, you can sort any of the other axes by level if
they have a ``MultiIndex``:

   df.T.sort_index(level=1, axis=1)

Indexing will work even if the data are not sorted, but will be rather
inefficient (and show a ``PerformanceWarning``). It will also
return a copy of the data rather than a view:

   dfm = pd.DataFrame(
       {"jim": [0, 0, 1, 1], "joe": ["x", "x", "z", "y"], "jolie": np.random.rand(4)}
   )
   dfm = dfm.set_index(["jim", "joe"])
   dfm

.. code-block:: ipython

   In [4]: dfm.loc[(1, 'z')]
   PerformanceWarning: indexing past lexsort depth may impact performance.

   Out[4]:
              jolie
   jim joe
   1   z    0.64094

.. _advanced.unsorted:

Furthermore, if you try to index something that is not fully lexsorted, this can raise:

.. code-block:: ipython

    In [5]: dfm.loc[(0, 'y'):(1, 'z')]
    UnsortedIndexError: 'Key length (2) was greater than MultiIndex lexsort depth (1)'

The :meth:`~MultiIndex.is_monotonic_increasing` method on a ``MultiIndex`` shows if the
index is sorted:

   dfm.index.is_monotonic_increasing

   dfm = dfm.sort_index()
   dfm
   dfm.index.is_monotonic_increasing

And now selection works as expected.

   dfm.loc[(0, "y"):(1, "z")]

Take methods
------------

.. _advanced.take:

Similar to NumPy ndarrays, pandas ``Index``, ``Series``, and ``DataFrame`` also provides
the :meth:`~DataFrame.take` method that retrieves elements along a given axis at the given
indices. The given indices must be either a list or an ndarray of integer
index positions. ``take`` will also accept negative integers as relative positions to the end of the object.

   index = pd.Index(np.random.randint(0, 1000, 10))
   index

   positions = [0, 9, 3]

   index[positions]
   index.take(positions)

   ser = pd.Series(np.random.randn(10))

   ser.iloc[positions]
   ser.take(positions)

For DataFrames, the given indices should be a 1d list or ndarray that specifies
row or column positions.

   frm = pd.DataFrame(np.random.randn(5, 3))

   frm.take([1, 4, 3])

   frm.take([0, 2], axis=1)

It is important to note that the ``take`` method on pandas objects are not
intended to work on boolean indices and may return unexpected results.

   arr = np.random.randn(10)
   arr.take([False, False, True, True])
   arr[[0, 1]]

   ser = pd.Series(np.random.randn(10))
   ser.take([False, False, True, True])
   ser.iloc[[0, 1]]

Finally, as a small note on performance, because the ``take`` method handles
a narrower range of inputs, it can offer performance that is a good deal
faster than fancy indexing.

   arr = np.random.randn(10000, 5)
   indexer = np.arange(10000)
   random.shuffle(indexer)

   %timeit arr[indexer]
   %timeit arr.take(indexer, axis=0)

   ser = pd.Series(arr[:, 0])
   %timeit ser.iloc[indexer]
   %timeit ser.take(indexer)

.. _advanced.index_types:

Index types
-----------

We have discussed ``MultiIndex`` in the previous sections pretty extensively.
Documentation about ``DatetimeIndex`` and ``PeriodIndex`` are shown :ref:`here <timeseries.overview>`,
and documentation about ``TimedeltaIndex`` is found :ref:`here <timedeltas.index>`.

In the following sub-sections we will highlight some other index types.

.. _advanced.categoricalindex:

CategoricalIndex
~~~~~~~~~~~~~~~~

indexing with duplicates. This is a container around a :class:`Categorical`
and allows efficient indexing and storage of an index with a large number of duplicated elements.

   from pandas.api.types import CategoricalDtype

   df = pd.DataFrame({"A": np.arange(6), "B": list("aabbca")})
   df["B"] = df["B"].astype(CategoricalDtype(list("cab")))
   df
   df.dtypes
   df["B"].cat.categories

Setting the index will create a ``CategoricalIndex``.

   df2 = df.set_index("B")
   df2.index

Indexing with ``__getitem__/.iloc/.loc`` works similarly to an ``Index`` with duplicates.
The indexers **must** be in the category or the operation will raise a ``KeyError``.

   df2.loc["a"]

The ``CategoricalIndex`` is **preserved** after indexing:

   df2.loc["a"].index

Sorting the index will sort by the order of the categories (recall that we
created the index with ``CategoricalDtype(list('cab'))``, so the sorted
order is ``cab``).

   df2.sort_index()

Groupby operations on the index will preserve the index nature as well.

   df2.groupby(level=0).sum()
   df2.groupby(level=0).sum().index

Reindexing operations will return a resulting index based on the type of the passed
indexer. Passing a list will return a plain-old ``Index``; indexing with
a ``Categorical`` will return a ``CategoricalIndex``, indexed according to the categories
of the **passed** ``Categorical`` dtype. This allows one to arbitrarily index these even with
values **not** in the categories, similarly to how you can reindex **any** pandas index.

   df3 = pd.DataFrame(
       {"A": np.arange(3), "B": pd.Series(list("abc")).astype("category")}
   )
   df3 = df3.set_index("B")
   df3

   df3.reindex(["a", "e"])
   df3.reindex(["a", "e"]).index
   df3.reindex(pd.Categorical(["a", "e"], categories=list("abe")))
   df3.reindex(pd.Categorical(["a", "e"], categories=list("abe"))).index

   Reshaping and Comparison operations on a ``CategoricalIndex`` must have the same categories
   or a ``TypeError`` will be raised.

      df4 = pd.DataFrame({"A": np.arange(2), "B": list("ba")})
      df4["B"] = df4["B"].astype(CategoricalDtype(list("ab")))
      df4 = df4.set_index("B")
      df4.index

      df5 = pd.DataFrame({"A": np.arange(2), "B": list("bc")})
      df5["B"] = df5["B"].astype(CategoricalDtype(list("bc")))
      df5 = df5.set_index("B")
      df5.index

   .. code-block:: ipython

      In [1]: pd.concat([df4, df5])
      TypeError: categories must match existing categories when appending

.. _advanced.rangeindex:

RangeIndex
~~~~~~~~~~

``RangeIndex`` is an optimized version of ``Index`` that can represent a monotonic ordered set. These are analogous to Python `range types <https://docs.python.org/3/library/stdtypes.html#typesseq-range>`__.
A ``RangeIndex`` will always have an ``int64`` dtype.

   idx = pd.RangeIndex(5)
   idx

``RangeIndex`` is the default index for all :class:`DataFrame` and :class:`Series` objects:

   ser = pd.Series([1, 2, 3])
   ser.index
   df = pd.DataFrame([[1, 2], [3, 4]])
   df.index
   df.columns

A ``RangeIndex`` will behave similarly to a :class:`Index` with an ``int64`` dtype and operations on a ``RangeIndex``,
whose result cannot be represented by a ``RangeIndex``, but should have an integer dtype, will be converted to an ``Index`` with ``int64``.
For example:

   idx[[0, 2]]

.. _advanced.intervalindex:

IntervalIndex
~~~~~~~~~~~~~

as well as the :class:`Interval` scalar type,  allow first-class support in pandas
for interval notation.

The ``IntervalIndex`` allows some unique indexing and is also used as a
return type for the categories in :func:`cut` and :func:`qcut`.

Indexing with an ``IntervalIndex``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An ``IntervalIndex`` can be used in ``Series`` and in ``DataFrame`` as the index.

   df = pd.DataFrame(
       {"A": [1, 2, 3, 4]}, index=pd.IntervalIndex.from_breaks([0, 1, 2, 3, 4])
   )
   df

Label based indexing via ``.loc`` along the edges of an interval works as you would expect,
selecting that particular interval.

   df.loc[2]
   df.loc[[2, 3]]

If you select a label *contained* within an interval, this will also select the interval.

   df.loc[2.5]
   df.loc[[2.5, 3.5]]

Selecting using an ``Interval`` will only return exact matches (starting from pandas 0.25.0).

   df.loc[pd.Interval(1, 2)]

Trying to select an ``Interval`` that is not exactly contained in the ``IntervalIndex`` will raise a ``KeyError``.

.. code-block:: python

   In [7]: df.loc[pd.Interval(0.5, 2.5)]
   ---------------------------------------------------------------------------
   KeyError: Interval(0.5, 2.5, closed='right')

Selecting all ``Intervals`` that overlap a given ``Interval`` can be performed using the

   idxr = df.index.overlaps(pd.Interval(0.5, 2.5))
   idxr
   df[idxr]

Binning data with ``cut`` and ``qcut``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

create are stored as an ``IntervalIndex`` in its ``.categories`` attribute.

   c = pd.cut(range(4), bins=2)
   c
   c.categories

a useful pandas idiom. First, We call :func:`cut` with some data and ``bins`` set to a
fixed number, to generate the bins. Then, we pass the values of ``.categories`` as the
``bins`` argument in subsequent calls to :func:`cut`, supplying new data which will be
binned into the same bins.

   pd.cut([0, 3, 5, 1], bins=c.categories)

Any value which falls outside all bins will be assigned a ``NaN`` value.

Generating ranges of intervals
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If we need intervals on a regular frequency, we can use the :func:`interval_range` function
to create an ``IntervalIndex`` using various combinations of ``start``, ``end``, and ``periods``.
The default frequency for ``interval_range`` is a 1 for numeric intervals, and calendar day for
datetime-like intervals:

   pd.interval_range(start=0, end=5)

   pd.interval_range(start=pd.Timestamp("2017-01-01"), periods=4)

   pd.interval_range(end=pd.Timedelta("3 days"), periods=3)

The ``freq`` parameter can used to specify non-default frequencies, and can utilize a variety
of :ref:`frequency aliases <timeseries.offset_aliases>` with datetime-like intervals:

   pd.interval_range(start=0, periods=5, freq=1.5)

   pd.interval_range(start=pd.Timestamp("2017-01-01"), periods=4, freq="W")

   pd.interval_range(start=pd.Timedelta("0 days"), periods=3, freq="9H")

Additionally, the ``closed`` parameter can be used to specify which side(s) the intervals
are closed on.  Intervals are closed on the right side by default.

   pd.interval_range(start=0, end=4, closed="both")

   pd.interval_range(start=0, end=4, closed="neither")

Specifying ``start``, ``end``, and ``periods`` will generate a range of evenly spaced
intervals from ``start`` to ``end`` inclusively, with ``periods`` number of elements
in the resulting ``IntervalIndex``:

   pd.interval_range(start=0, end=6, periods=4)

   pd.interval_range(pd.Timestamp("2018-01-01"), pd.Timestamp("2018-02-28"), periods=3)

Miscellaneous indexing FAQ
--------------------------

Integer indexing
~~~~~~~~~~~~~~~~

Label-based indexing with integer axis labels is a thorny topic. It has been
discussed heavily on mailing lists and among various members of the scientific
Python community. In pandas, our general viewpoint is that labels matter more
than integer locations. Therefore, with an integer axis index *only*
label-based indexing is possible with the standard tools like ``.loc``. The
following code will generate exceptions:

   s = pd.Series(range(5))
   s[-1]
   df = pd.DataFrame(np.random.randn(5, 4))
   df
   df.loc[-2:]

This deliberate decision was made to prevent ambiguities and subtle bugs (many
users reported finding bugs when the API change was made to stop "falling back"
on position-based indexing).

Non-monotonic indexes require exact matches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the index of a ``Series`` or ``DataFrame`` is monotonically increasing or decreasing, then the bounds
of a label-based slice can be outside the range of the index, much like slice indexing a
normal Python ``list``. Monotonicity of an index can be tested with the :meth:`~Index.is_monotonic_increasing` and

    df = pd.DataFrame(index=[2, 3, 3, 4, 5], columns=["data"], data=list(range(5)))
    df.index.is_monotonic_increasing

    # no rows 0 or 1, but still returns rows 2, 3 (both of them), and 4:
    df.loc[0:4, :]

    # slice is are outside the index, so empty DataFrame is returned
    df.loc[13:15, :]

On the other hand, if the index is not monotonic, then both slice bounds must be
*unique* members of the index.

    df = pd.DataFrame(index=[2, 3, 1, 4, 3, 5], columns=["data"], data=list(range(6)))
    df.index.is_monotonic_increasing

    # OK because 2 and 4 are in the index
    df.loc[2:4, :]

.. code-block:: ipython

    # 0 is not in the index
    In [9]: df.loc[0:4, :]
    KeyError: 0

    # 3 is not a unique label
    In [11]: df.loc[2:3, :]
    KeyError: 'Cannot get right slice bound for non-unique label: 3'

``Index.is_monotonic_increasing`` and ``Index.is_monotonic_decreasing`` only check that
an index is weakly monotonic. To check for strict monotonicity, you can combine one of those with
the :meth:`~Index.is_unique` attribute.

   weakly_monotonic = pd.Index(["a", "b", "c", "c"])
   weakly_monotonic
   weakly_monotonic.is_monotonic_increasing
   weakly_monotonic.is_monotonic_increasing & weakly_monotonic.is_unique

.. _advanced.endpoints_are_inclusive:

Endpoints are inclusive
~~~~~~~~~~~~~~~~~~~~~~~

Compared with standard Python sequence slicing in which the slice endpoint is
not inclusive, label-based slicing in pandas **is inclusive**. The primary
reason for this is that it is often not possible to easily determine the
"successor" or next element after a particular label in an index. For example,
consider the following ``Series``:

   s = pd.Series(np.random.randn(6), index=list("abcdef"))
   s

Suppose we wished to slice from ``c`` to ``e``, using integers this would be
accomplished as such:

   s[2:5]

However, if you only had ``c`` and ``e``, determining the next element in the
index can be somewhat complicated. For example, the following does not work:

::

    s.loc['c':'e' + 1]

A very common use case is to limit a time series to start and end at two
specific dates. To enable this, we made the design choice to make label-based
slicing include both endpoints:

    s.loc["c":"e"]

This is most definitely a "practicality beats purity" sort of thing, but it is
something to watch out for if you expect label-based slicing to behave exactly
in the way that standard Python integer slicing works.

Indexing potentially changes underlying Series dtype
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The different indexing operation can potentially change the dtype of a ``Series``.

   series1 = pd.Series([1, 2, 3])
   series1.dtype
   res = series1.reindex([0, 4])
   res.dtype
   res

   series2 = pd.Series([True])
   series2.dtype
   res = series2.reindex_like(series1)
   res.dtype
   res

This is because the (re)indexing operations above silently inserts ``NaNs`` and the ``dtype``
changes accordingly.  This can cause some issues when using ``numpy`` ``ufuncs``
such as ``numpy.logical_and``.

See the :issue:`2388` for a more
detailed discussion.
