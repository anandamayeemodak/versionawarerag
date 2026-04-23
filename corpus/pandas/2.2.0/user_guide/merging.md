.. _merging:

{{ header }}

   from matplotlib import pyplot as plt
   import pandas.util._doctools as doctools

   p = doctools.TablePlotter()

************************************
Merge, join, concatenate and compare
************************************

pandas provides various methods for combining and comparing :class:`Series` or

* :func:`~pandas.concat`: Merge multiple :class:`Series` or :class:`DataFrame` objects along a shared index or column
* :meth:`DataFrame.join`: Merge multiple :class:`DataFrame` objects along the columns
* :meth:`DataFrame.combine_first`: Update missing values with non-missing values in the same location
* :func:`~pandas.merge`: Combine two :class:`Series` or :class:`DataFrame` objects with SQL-style joining
* :func:`~pandas.merge_ordered`: Combine two :class:`Series` or :class:`DataFrame` objects along an ordered axis
* :func:`~pandas.merge_asof`: Combine two :class:`Series` or :class:`DataFrame` objects by near instead of exact matching keys
* :meth:`Series.compare` and :meth:`DataFrame.compare`: Show differences in values between two :class:`Series` or :class:`DataFrame` objects

.. _merging.concat:

----------------------

The :func:`~pandas.concat` function concatenates an arbitrary amount of

performing optional set logic (union or intersection) of the indexes on
the other axes. Like ``numpy.concatenate``, :func:`~pandas.concat`
takes a list or dict of homogeneously-typed objects and concatenates them.

   df1 = pd.DataFrame(
       {
           "A": ["A0", "A1", "A2", "A3"],
           "B": ["B0", "B1", "B2", "B3"],
           "C": ["C0", "C1", "C2", "C3"],
           "D": ["D0", "D1", "D2", "D3"],
       },
       index=[0, 1, 2, 3],
   )

   df2 = pd.DataFrame(
       {
           "A": ["A4", "A5", "A6", "A7"],
           "B": ["B4", "B5", "B6", "B7"],
           "C": ["C4", "C5", "C6", "C7"],
           "D": ["D4", "D5", "D6", "D7"],
       },
       index=[4, 5, 6, 7],
   )

   df3 = pd.DataFrame(
       {
           "A": ["A8", "A9", "A10", "A11"],
           "B": ["B8", "B9", "B10", "B11"],
           "C": ["C8", "C9", "C10", "C11"],
           "D": ["D8", "D9", "D10", "D11"],
       },
       index=[8, 9, 10, 11],
   )

   frames = [df1, df2, df3]
   result = pd.concat(frames)
   result

   @savefig merging_concat_basic.png
   p.plot(frames, result, labels=["df1", "df2", "df3"], vertical=True);
   plt.close("all");

   reusing :func:`~pandas.concat` can create unnecessary copies. Collect all

   .. code-block:: python

      frames = [process_your_file(f) for f in files]
      result = pd.concat(frames)

   When concatenating :class:`DataFrame` with named axes, pandas will attempt to preserve
   these index/column names whenever possible. In the case where all inputs share a
   common name, this name will be assigned to the result. When the input names do
   not all agree, the result will be unnamed. The same is true for :class:`MultiIndex`,
   but the logic is applied separately on a level-by-level basis.

Joining logic of the resulting axis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``join`` keyword specifies how to handle axis values that don't exist in the first

``join='outer'`` takes the union of all axis values

   df4 = pd.DataFrame(
       {
           "B": ["B2", "B3", "B6", "B7"],
           "D": ["D2", "D3", "D6", "D7"],
           "F": ["F2", "F3", "F6", "F7"],
       },
       index=[2, 3, 6, 7],
   )
   result = pd.concat([df1, df4], axis=1)
   result

   @savefig merging_concat_axis1.png
   p.plot([df1, df4], result, labels=["df1", "df4"], vertical=False);
   plt.close("all");

``join='inner'`` takes the intersection of the axis values

   result = pd.concat([df1, df4], axis=1, join="inner")
   result

   @savefig merging_concat_axis1_inner.png
   p.plot([df1, df4], result, labels=["df1", "df4"], vertical=False);
   plt.close("all");

To perform an effective "left" join using the *exact index* from the original

   result = pd.concat([df1, df4], axis=1).reindex(df1.index)
   result

   @savefig merging_concat_axis1_join_axes.png
   p.plot([df1, df4], result, labels=["df1", "df4"], vertical=False);
   plt.close("all");

.. _merging.ignore_index:

Ignoring indexes on the concatenation axis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For :class:`DataFrame` objects which don't have a meaningful index, the ``ignore_index``
ignores overlapping indexes.

   result = pd.concat([df1, df4], ignore_index=True, sort=False)
   result

   @savefig merging_concat_ignore_index.png
   p.plot([df1, df4], result, labels=["df1", "df4"], vertical=True);
   plt.close("all");

.. _merging.mixed_ndims:

Concatenating :class:`Series` and :class:`DataFrame` together
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can concatenate a mix of :class:`Series` and :class:`DataFrame` objects. The

the name of the :class:`Series`.

   s1 = pd.Series(["X0", "X1", "X2", "X3"], name="X")
   result = pd.concat([df1, s1], axis=1)
   result

   @savefig merging_concat_mixed_ndim.png
   p.plot([df1, s1], result, labels=["df1", "s1"], vertical=False);
   plt.close("all");

Unnamed :class:`Series` will be numbered consecutively.

   s2 = pd.Series(["_0", "_1", "_2", "_3"])
   result = pd.concat([df1, s2, s2, s2], axis=1)
   result

   @savefig merging_concat_unnamed_series.png
   p.plot([df1, s2], result, labels=["df1", "s2"], vertical=False);
   plt.close("all");

``ignore_index=True`` will drop all name references.

   result = pd.concat([df1, s1], axis=1, ignore_index=True)
   result

   @savefig merging_concat_series_ignore_index.png
   p.plot([df1, s1], result, labels=["df1", "s1"], vertical=False);
   plt.close("all");

Resulting ``keys``
~~~~~~~~~~~~~~~~~~

The ``keys`` argument adds another axis level to the resulting index or column (creating
a :class:`MultiIndex`) associate specific keys with each original :class:`DataFrame`.

   result = pd.concat(frames, keys=["x", "y", "z"])
   result
   result.loc["y"]

   @savefig merging_concat_keys.png
   p.plot(frames, result, labels=["df1", "df2", "df3"], vertical=True)
   plt.close("all");

The ``keys`` argument cane override the column names
when creating a new :class:`DataFrame` based on existing :class:`Series`.

   s3 = pd.Series([0, 1, 2, 3], name="foo")
   s4 = pd.Series([0, 1, 2, 3])
   s5 = pd.Series([0, 1, 4, 5])

   pd.concat([s3, s4, s5], axis=1)
   pd.concat([s3, s4, s5], axis=1, keys=["red", "blue", "yellow"])

You can also pass a dict to :func:`concat` in which case the dict keys will be used
for the ``keys`` argument unless other ``keys`` argument is specified:

   pieces = {"x": df1, "y": df2, "z": df3}
   result = pd.concat(pieces)
   result

   @savefig merging_concat_dict.png
   p.plot([df1, df2, df3], result, labels=["df1", "df2", "df3"], vertical=True);
   plt.close("all");

   result = pd.concat(pieces, keys=["z", "y"])
   result

   @savefig merging_concat_dict_keys.png
   p.plot([df1, df2, df3], result, labels=["df1", "df2", "df3"], vertical=True);
   plt.close("all");

The :class:`MultiIndex` created has levels that are constructed from the passed keys and
the index of the :class:`DataFrame` pieces:

   result.index.levels

``levels`` argument allows specifying resulting levels associated with the ``keys``

   result = pd.concat(
       pieces, keys=["x", "y", "z"], levels=[["z", "y", "x", "w"]], names=["group_key"]
   )
   result

   @savefig merging_concat_dict_keys_names.png
   p.plot([df1, df2, df3], result, labels=["df1", "df2", "df3"], vertical=True);
   plt.close("all");

   result.index.levels

.. _merging.append.row:

Appending rows to a :class:`DataFrame`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have a :class:`Series` that you want to append as a single row to a :class:`DataFrame`, you can convert the row into a

   s2 = pd.Series(["X0", "X1", "X2", "X3"], index=["A", "B", "C", "D"])
   result = pd.concat([df1, s2.to_frame().T], ignore_index=True)
   result

   @savefig merging_append_series_as_row.png
   p.plot([df1, s2], result, labels=["df1", "s2"], vertical=True);
   plt.close("all");

.. _merging.join:

---------------------

Users who are familiar with SQL but new to pandas can reference a

Merge types
~~~~~~~~~~~

* **one-to-one**: joining two :class:`DataFrame` objects on
  their indexes which must contain unique values.
* **many-to-one**: joining a unique index to one or
  more columns in a different :class:`DataFrame`.
* **many-to-many** : joining columns on columns.

   When joining columns on columns, potentially a many-to-many join, any
   indexes on the passed :class:`DataFrame` objects **will be discarded**.

For a **many-to-many** join, if a key combination appears
more than once in both tables, the :class:`DataFrame` will have the **Cartesian
product** of the associated data.

   left = pd.DataFrame(
       {
           "key": ["K0", "K1", "K2", "K3"],
           "A": ["A0", "A1", "A2", "A3"],
           "B": ["B0", "B1", "B2", "B3"],
       }
   )

   right = pd.DataFrame(
       {
           "key": ["K0", "K1", "K2", "K3"],
           "C": ["C0", "C1", "C2", "C3"],
           "D": ["D0", "D1", "D2", "D3"],
       }
   )
   result = pd.merge(left, right, on="key")
   result

   @savefig merging_merge_on_key.png
   p.plot([left, right], result, labels=["left", "right"], vertical=False);
   plt.close("all");

The ``how`` argument to :func:`~pandas.merge` specifies which keys are
included in the resulting table. If a key combination **does not appear** in
either the left or right tables, the values in the joined table will be
``NA``. Here is a summary of the ``how`` options and their SQL equivalent names:

.. csv-table::

    ``left``, ``LEFT OUTER JOIN``, Use keys from left frame only
    ``right``, ``RIGHT OUTER JOIN``, Use keys from right frame only
    ``outer``, ``FULL OUTER JOIN``, Use union of keys from both frames
    ``inner``, ``INNER JOIN``, Use intersection of keys from both frames
    ``cross``, ``CROSS JOIN``, Create the cartesian product of rows of both frames

   left = pd.DataFrame(
      {
         "key1": ["K0", "K0", "K1", "K2"],
         "key2": ["K0", "K1", "K0", "K1"],
         "A": ["A0", "A1", "A2", "A3"],
         "B": ["B0", "B1", "B2", "B3"],
      }
   )
   right = pd.DataFrame(
      {
         "key1": ["K0", "K1", "K1", "K2"],
         "key2": ["K0", "K0", "K0", "K0"],
         "C": ["C0", "C1", "C2", "C3"],
         "D": ["D0", "D1", "D2", "D3"],
      }
   )
   result = pd.merge(left, right, how="left", on=["key1", "key2"])
   result

   @savefig merging_merge_on_key_left.png
   p.plot([left, right], result, labels=["left", "right"], vertical=False);
   plt.close("all");

   result = pd.merge(left, right, how="right", on=["key1", "key2"])
   result

   @savefig merging_merge_on_key_right.png
   p.plot([left, right], result, labels=["left", "right"], vertical=False);

   result = pd.merge(left, right, how="outer", on=["key1", "key2"])
   result

   @savefig merging_merge_on_key_outer.png
   p.plot([left, right], result, labels=["left", "right"], vertical=False);
   plt.close("all");

   result = pd.merge(left, right, how="inner", on=["key1", "key2"])
   result

   @savefig merging_merge_on_key_inner.png
   p.plot([left, right], result, labels=["left", "right"], vertical=False);
   plt.close("all");

   result = pd.merge(left, right, how="cross")
   result

   @savefig merging_merge_cross.png
   p.plot([left, right], result, labels=["left", "right"], vertical=False);
   plt.close("all");

You can :class:`Series` and a :class:`DataFrame` with a :class:`MultiIndex` if the names of
the :class:`MultiIndex` correspond to the columns from the :class:`DataFrame`. Transform
the :class:`Series` to a :class:`DataFrame` using :meth:`Series.reset_index` before merging

   df = pd.DataFrame({"Let": ["A", "B", "C"], "Num": [1, 2, 3]})
   df

   ser = pd.Series(
       ["a", "b", "c", "d", "e", "f"],
       index=pd.MultiIndex.from_arrays(
           [["A", "B", "C"] * 2, [1, 2, 3, 4, 5, 6]], names=["Let", "Num"]
       ),
   )
   ser

   pd.merge(df, ser.reset_index(), on=["Let", "Num"])

Performing an outer join with duplicate join keys in :class:`DataFrame`

   left = pd.DataFrame({"A": [1, 2], "B": [2, 2]})

   right = pd.DataFrame({"A": [4, 5, 6], "B": [2, 2, 2]})

   result = pd.merge(left, right, on="B", how="outer")
   result

   @savefig merging_merge_on_key_dup.png
   p.plot([left, right], result, labels=["left", "right"], vertical=False);
   plt.close("all");

  Merging on duplicate keys significantly increase the dimensions of the result
  and can cause a memory overflow.

.. _merging.validation:

Merge key uniqueness
~~~~~~~~~~~~~~~~~~~~

The ``validate`` argument checks whether the uniqueness of merge keys.
Key uniqueness is checked before merge operations and can protect against memory overflows
and unexpected key duplication.

   left = pd.DataFrame({"A": [1, 2], "B": [1, 2]})
   right = pd.DataFrame({"A": [4, 5, 6], "B": [2, 2, 2]})
   result = pd.merge(left, right, on="B", how="outer", validate="one_to_one")

If the user is aware of the duplicates in the right :class:`DataFrame` but wants to
ensure there are no duplicates in the left :class:`DataFrame`, one can use the
``validate='one_to_many'`` argument instead, which will not raise an exception.

   pd.merge(left, right, on="B", how="outer", validate="one_to_many")

.. _merging.indicator:

Merge result indicator
~~~~~~~~~~~~~~~~~~~~~~

Categorical-type column called ``_merge`` will be added to the output object
that takes on values:

  ===================================   ================
  Observation Origin                    ``_merge`` value
  ===================================   ================
  Merge key only in ``'left'`` frame    ``left_only``
  Merge key only in ``'right'`` frame   ``right_only``
  Merge key in both frames              ``both``
  ===================================   ================

   df1 = pd.DataFrame({"col1": [0, 1], "col_left": ["a", "b"]})
   df2 = pd.DataFrame({"col1": [1, 2, 2], "col_right": [2, 2, 2]})
   pd.merge(df1, df2, on="col1", how="outer", indicator=True)

A string argument to ``indicator`` will use the value as the name for the indicator column.

   pd.merge(df1, df2, on="col1", how="outer", indicator="indicator_column")

Overlapping value columns
~~~~~~~~~~~~~~~~~~~~~~~~~

The merge ``suffixes`` argument takes a tuple of list of strings to append to
overlapping column names in the input :class:`DataFrame` to disambiguate the result
columns:

   left = pd.DataFrame({"k": ["K0", "K1", "K2"], "v": [1, 2, 3]})
   right = pd.DataFrame({"k": ["K0", "K0", "K3"], "v": [4, 5, 6]})

   result = pd.merge(left, right, on="k")
   result

   @savefig merging_merge_overlapped.png
   p.plot([left, right], result, labels=["left", "right"], vertical=False);
   plt.close("all");

   result = pd.merge(left, right, on="k", suffixes=("_l", "_r"))
   result

   @savefig merging_merge_overlapped_suffix.png
   p.plot([left, right], result, labels=["left", "right"], vertical=False);
   plt.close("all");

----------------------

potentially differently-indexed :class:`DataFrame` into a single result

   left = pd.DataFrame(
       {"A": ["A0", "A1", "A2"], "B": ["B0", "B1", "B2"]}, index=["K0", "K1", "K2"]
   )

   right = pd.DataFrame(
       {"C": ["C0", "C2", "C3"], "D": ["D0", "D2", "D3"]}, index=["K0", "K2", "K3"]
   )

   result = left.join(right)
   result

   @savefig merging_join.png
   p.plot([left, right], result, labels=["left", "right"], vertical=False);
   plt.close("all");

   result = left.join(right, how="outer")
   result

   @savefig merging_join_outer.png
   p.plot([left, right], result, labels=["left", "right"], vertical=False);
   plt.close("all");

   result = left.join(right, how="inner")
   result

   @savefig merging_join_inner.png
   p.plot([left, right], result, labels=["left", "right"], vertical=False);
   plt.close("all");

or multiple column names that the passed :class:`DataFrame` is to be
aligned.

   left = pd.DataFrame(
       {
           "A": ["A0", "A1", "A2", "A3"],
           "B": ["B0", "B1", "B2", "B3"],
           "key": ["K0", "K1", "K0", "K1"],
       }
   )

   right = pd.DataFrame({"C": ["C0", "C1"], "D": ["D0", "D1"]}, index=["K0", "K1"])

   result = left.join(right, on="key")
   result

   @savefig merging_join_key_columns.png
   p.plot([left, right], result, labels=["left", "right"], vertical=False);
   plt.close("all");

   result = pd.merge(
       left, right, left_on="key", right_index=True, how="left", sort=False
   )
   result

   @savefig merging_merge_key_columns.png
   p.plot([left, right], result, labels=["left", "right"], vertical=False);
   plt.close("all");

.. _merging.multikey_join:

To join on multiple keys, the passed :class:`DataFrame` must have a :class:`MultiIndex`:

   left = pd.DataFrame(
       {
           "A": ["A0", "A1", "A2", "A3"],
           "B": ["B0", "B1", "B2", "B3"],
           "key1": ["K0", "K0", "K1", "K2"],
           "key2": ["K0", "K1", "K0", "K1"],
       }
   )

   index = pd.MultiIndex.from_tuples(
       [("K0", "K0"), ("K1", "K0"), ("K2", "K0"), ("K2", "K1")]
   )
   right = pd.DataFrame(
       {"C": ["C0", "C1", "C2", "C3"], "D": ["D0", "D1", "D2", "D3"]}, index=index
   )
   result = left.join(right, on=["key1", "key2"])
   result

   @savefig merging_join_multikeys.png
   p.plot([left, right], result, labels=["left", "right"], vertical=False);
   plt.close("all");

.. _merging.df_inner_join:

The default for :class:`DataFrame.join` is to perform a left join
which uses only the keys found in the
calling :class:`DataFrame`. Other join types can be specified with ``how``.

   result = left.join(right, on=["key1", "key2"], how="inner")
   result

   @savefig merging_join_multikeys_inner.png
   p.plot([left, right], result, labels=["left", "right"], vertical=False);
   plt.close("all");

.. _merging.join_on_mi:

Joining a single Index to a MultiIndex
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can join a :class:`DataFrame` with a :class:`Index` to a :class:`DataFrame` with a :class:`MultiIndex` on a level.
The ``name`` of the :class:`Index` with match the level name of the :class:`MultiIndex`.

    left = pd.DataFrame(
        {"A": ["A0", "A1", "A2"], "B": ["B0", "B1", "B2"]},
        index=pd.Index(["K0", "K1", "K2"], name="key"),
    )

    index = pd.MultiIndex.from_tuples(
        [("K0", "Y0"), ("K1", "Y1"), ("K2", "Y2"), ("K2", "Y3")],
        names=["key", "Y"],
    )
    right = pd.DataFrame(
        {"C": ["C0", "C1", "C2", "C3"], "D": ["D0", "D1", "D2", "D3"]},
        index=index,
    )

    result = left.join(right, how="inner")
    result

   @savefig merging_join_multiindex_inner.png
   p.plot([left, right], result, labels=["left", "right"], vertical=False);
   plt.close("all");

.. _merging.join_with_two_multi_indexes:

Joining with two :class:`MultiIndex`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :class:`MultiIndex` of the input argument must be completely used
in the join and is a subset of the indices in the left argument.

   leftindex = pd.MultiIndex.from_product(
       [list("abc"), list("xy"), [1, 2]], names=["abc", "xy", "num"]
   )
   left = pd.DataFrame({"v1": range(12)}, index=leftindex)
   left

   rightindex = pd.MultiIndex.from_product(
       [list("abc"), list("xy")], names=["abc", "xy"]
   )
   right = pd.DataFrame({"v2": [100 * i for i in range(1, 7)]}, index=rightindex)
   right

   left.join(right, on=["abc", "xy"], how="inner")

   leftindex = pd.MultiIndex.from_tuples(
       [("K0", "X0"), ("K0", "X1"), ("K1", "X2")], names=["key", "X"]
   )
   left = pd.DataFrame(
       {"A": ["A0", "A1", "A2"], "B": ["B0", "B1", "B2"]}, index=leftindex
   )

   rightindex = pd.MultiIndex.from_tuples(
       [("K0", "Y0"), ("K1", "Y1"), ("K2", "Y2"), ("K2", "Y3")], names=["key", "Y"]
   )
   right = pd.DataFrame(
       {"C": ["C0", "C1", "C2", "C3"], "D": ["D0", "D1", "D2", "D3"]}, index=rightindex
   )

   result = pd.merge(
       left.reset_index(), right.reset_index(), on=["key"], how="inner"
   ).set_index(["key", "X", "Y"])
   result

   @savefig merging_merge_two_multiindex.png
   p.plot([left, right], result, labels=["left", "right"], vertical=False);
   plt.close("all");

.. _merging.merge_on_columns_and_levels:

Merging on a combination of columns and index levels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Strings passed as the ``on``, ``left_on``, and ``right_on`` parameters
may refer to either column names or index level names.  This enables merging

resetting indexes.

   left_index = pd.Index(["K0", "K0", "K1", "K2"], name="key1")

   left = pd.DataFrame(
       {
           "A": ["A0", "A1", "A2", "A3"],
           "B": ["B0", "B1", "B2", "B3"],
           "key2": ["K0", "K1", "K0", "K1"],
       },
       index=left_index,
   )

   right_index = pd.Index(["K0", "K1", "K2", "K2"], name="key1")

   right = pd.DataFrame(
       {
           "C": ["C0", "C1", "C2", "C3"],
           "D": ["D0", "D1", "D2", "D3"],
           "key2": ["K0", "K0", "K0", "K1"],
       },
       index=right_index,
   )

   result = left.merge(right, on=["key1", "key2"])
   result

   @savefig merge_on_index_and_column.png
   p.plot([left, right], result, labels=["left", "right"], vertical=False);
   plt.close("all");

   When :class:`DataFrame` are joined on a string that matches an index level in both
   arguments, the index level is preserved as an index level in the resulting

   When :class:`DataFrame` are joined using only some of the levels of a :class:`MultiIndex`,
   the extra levels will be dropped from the resulting join. To
   preserve those levels, use :meth:`DataFrame.reset_index` on those level
   names to move those levels to columns prior to the join.

.. _merging.multiple_join:

Joining multiple :class:`DataFrame`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A list or tuple of ``:class:`DataFrame``` can also be passed to :meth:`~DataFrame.join`
to join them together on their indexes.

   right2 = pd.DataFrame({"v": [7, 8, 9]}, index=["K1", "K1", "K2"])
   result = left.join([right, right2])

   @savefig merging_join_multi_df.png
   p.plot(
       [left, right, right2],
       result,
       labels=["left", "right", "right2"],
       vertical=False,
   );
   plt.close("all");

.. _merging.combine_first.update:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

with the non-missing values in another :class:`DataFrame` in the corresponding
location.

   df1 = pd.DataFrame(
       [[np.nan, 3.0, 5.0], [-4.6, np.nan, np.nan], [np.nan, 7.0, np.nan]]
   )
   df2 = pd.DataFrame([[-42.6, np.nan, -8.2], [-5.0, 1.6, 4]], index=[1, 2])
   result = df1.combine_first(df2)
   result

   @savefig merging_combine_first.png
   p.plot([df1, df2], result, labels=["df1", "df2"], vertical=False);
   plt.close("all");

.. _merging.merge_ordered:

---------------------

with optional filling of missing data with ``fill_method``.

   left = pd.DataFrame(
       {"k": ["K0", "K1", "K1", "K2"], "lv": [1, 2, 3, 4], "s": ["a", "b", "c", "d"]}
   )

   right = pd.DataFrame({"k": ["K1", "K2", "K4"], "rv": [1, 2, 3]})

   pd.merge_ordered(left, right, fill_method="ffill", left_by="s")

.. _merging.merge_asof:

---------------------

nearest key rather than equal keys. For each row in the ``left`` :class:`DataFrame`,
the last row in the ``right`` :class:`DataFrame` are selected where the ``on`` key is less
than the left's key. Both :class:`DataFrame` must be sorted by the key.

Optionally an :func:`merge_asof` can perform a group-wise merge by matching the
``by`` key in addition to the nearest match on the ``on`` key.

   trades = pd.DataFrame(
       {
           "time": pd.to_datetime(
               [
                   "20160525 13:30:00.023",
                   "20160525 13:30:00.038",
                   "20160525 13:30:00.048",
                   "20160525 13:30:00.048",
                   "20160525 13:30:00.048",
               ]
           ),
           "ticker": ["MSFT", "MSFT", "GOOG", "GOOG", "AAPL"],
           "price": [51.95, 51.95, 720.77, 720.92, 98.00],
           "quantity": [75, 155, 100, 100, 100],
       },
       columns=["time", "ticker", "price", "quantity"],
   )

   quotes = pd.DataFrame(
       {
           "time": pd.to_datetime(
               [
                   "20160525 13:30:00.023",
                   "20160525 13:30:00.023",
                   "20160525 13:30:00.030",
                   "20160525 13:30:00.041",
                   "20160525 13:30:00.048",
                   "20160525 13:30:00.049",
                   "20160525 13:30:00.072",
                   "20160525 13:30:00.075",
               ]
           ),
           "ticker": ["GOOG", "MSFT", "MSFT", "MSFT", "GOOG", "AAPL", "GOOG", "MSFT"],
           "bid": [720.50, 51.95, 51.97, 51.99, 720.50, 97.99, 720.50, 52.01],
           "ask": [720.93, 51.96, 51.98, 52.00, 720.93, 98.01, 720.88, 52.03],
       },
       columns=["time", "ticker", "bid", "ask"],
   )
   trades
   quotes
   pd.merge_asof(trades, quotes, on="time", by="ticker")

   pd.merge_asof(trades, quotes, on="time", by="ticker", tolerance=pd.Timedelta("2ms"))

exclude exact matches on time. Note that though we exclude the exact matches
(of the quotes), prior quotes **do** propagate to that point in time.

   pd.merge_asof(
       trades,
       quotes,
       on="time",
       by="ticker",
       tolerance=pd.Timedelta("10ms"),
       allow_exact_matches=False,
   )

.. _merging.compare:

-----------------------

The :meth:`Series.compare` and :meth:`DataFrame.compare` methods allow you to
compare two :class:`DataFrame` or :class:`Series`, respectively, and summarize their differences.

   df = pd.DataFrame(
       {
           "col1": ["a", "a", "b", "b", "a"],
           "col2": [1.0, 2.0, 3.0, np.nan, 5.0],
           "col3": [1.0, 2.0, 3.0, 4.0, 5.0],
       },
       columns=["col1", "col2", "col3"],
   )
   df
   df2 = df.copy()
   df2.loc[0, "col1"] = "c"
   df2.loc[2, "col3"] = 4.0
   df2
   df.compare(df2)

By default, if two corresponding values are equal, they will be shown as ``NaN``.
Furthermore, if all values in an entire row / column, the row / column will be
omitted from the result. The remaining differences will be aligned on columns.

Stack the differences on rows.

   df.compare(df2, align_axis=0)

Keep all original rows and columns with ``keep_shape=True``

   df.compare(df2, keep_shape=True)

Keep all the original values even if they are equal.

   df.compare(df2, keep_shape=True, keep_equal=True)
