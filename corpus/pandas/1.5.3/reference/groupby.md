{{ header }}

.. _api.groupby:

=======
GroupBy
=======

GroupBy objects are returned by groupby calls: :func:`pandas.DataFrame.groupby`, :func:`pandas.Series.groupby`, etc.

Indexing, iteration
-------------------

   GroupBy.__iter__
   GroupBy.groups
   GroupBy.indices
   GroupBy.get_group

   Grouper

Function application
--------------------

   GroupBy.apply
   GroupBy.agg
   SeriesGroupBy.aggregate
   DataFrameGroupBy.aggregate
   SeriesGroupBy.transform
   DataFrameGroupBy.transform
   GroupBy.pipe

Computations / descriptive stats
--------------------------------

   GroupBy.all
   GroupBy.any
   GroupBy.bfill
   GroupBy.backfill
   GroupBy.count
   GroupBy.cumcount
   GroupBy.cummax
   GroupBy.cummin
   GroupBy.cumprod
   GroupBy.cumsum
   GroupBy.ffill
   GroupBy.first
   GroupBy.head
   GroupBy.last
   GroupBy.max
   GroupBy.mean
   GroupBy.median
   GroupBy.min
   GroupBy.ngroup
   GroupBy.nth
   GroupBy.ohlc
   GroupBy.pad
   GroupBy.prod
   GroupBy.rank
   GroupBy.pct_change
   GroupBy.size
   GroupBy.sem
   GroupBy.std
   GroupBy.sum
   GroupBy.var
   GroupBy.tail

The following methods are available in both ``SeriesGroupBy`` and
``DataFrameGroupBy`` objects, but may differ slightly, usually in that
the ``DataFrameGroupBy`` version usually permits the specification of an
axis argument, and often an argument indicating whether to restrict
application to columns of a specific data type.

   DataFrameGroupBy.all
   DataFrameGroupBy.any
   DataFrameGroupBy.backfill
   DataFrameGroupBy.bfill
   DataFrameGroupBy.corr
   DataFrameGroupBy.count
   DataFrameGroupBy.cov
   DataFrameGroupBy.cumcount
   DataFrameGroupBy.cummax
   DataFrameGroupBy.cummin
   DataFrameGroupBy.cumprod
   DataFrameGroupBy.cumsum
   DataFrameGroupBy.describe
   DataFrameGroupBy.diff
   DataFrameGroupBy.ffill
   DataFrameGroupBy.fillna
   DataFrameGroupBy.filter
   DataFrameGroupBy.hist
   DataFrameGroupBy.idxmax
   DataFrameGroupBy.idxmin
   DataFrameGroupBy.mad
   DataFrameGroupBy.nunique
   DataFrameGroupBy.pad
   DataFrameGroupBy.pct_change
   DataFrameGroupBy.plot
   DataFrameGroupBy.quantile
   DataFrameGroupBy.rank
   DataFrameGroupBy.resample
   DataFrameGroupBy.sample
   DataFrameGroupBy.shift
   DataFrameGroupBy.size
   DataFrameGroupBy.skew
   DataFrameGroupBy.take
   DataFrameGroupBy.tshift
   DataFrameGroupBy.value_counts

The following methods are available only for ``SeriesGroupBy`` objects.

   SeriesGroupBy.hist
   SeriesGroupBy.nlargest
   SeriesGroupBy.nsmallest
   SeriesGroupBy.unique
   SeriesGroupBy.is_monotonic_increasing
   SeriesGroupBy.is_monotonic_decreasing

The following methods are available only for ``DataFrameGroupBy`` objects.

   DataFrameGroupBy.corrwith
   DataFrameGroupBy.boxplot
