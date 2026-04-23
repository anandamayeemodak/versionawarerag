{{ header }}

.. _api.indexing:

=============
Index objects
=============

Index
-----

**Many of these methods or variants thereof are available on the objects
that contain an index (Series/DataFrame) and those should most likely be
used before calling these methods directly.**

   Index

Properties
~~~~~~~~~~

   Index.values
   Index.is_monotonic_increasing
   Index.is_monotonic_decreasing
   Index.is_unique
   Index.has_duplicates
   Index.hasnans
   Index.dtype
   Index.inferred_type
   Index.shape
   Index.name
   Index.names
   Index.nbytes
   Index.ndim
   Index.size
   Index.empty
   Index.T
   Index.memory_usage

Modifying and computations
~~~~~~~~~~~~~~~~~~~~~~~~~~

   Index.all
   Index.any
   Index.argmin
   Index.argmax
   Index.copy
   Index.delete
   Index.drop
   Index.drop_duplicates
   Index.duplicated
   Index.equals
   Index.factorize
   Index.identical
   Index.insert
   Index.is_
   Index.is_boolean
   Index.is_categorical
   Index.is_floating
   Index.is_integer
   Index.is_interval
   Index.is_numeric
   Index.is_object
   Index.min
   Index.max
   Index.reindex
   Index.rename
   Index.repeat
   Index.where
   Index.take
   Index.putmask
   Index.unique
   Index.nunique
   Index.value_counts

Compatibility with MultiIndex
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Index.set_names
   Index.droplevel

Missing values
~~~~~~~~~~~~~~

   Index.fillna
   Index.dropna
   Index.isna
   Index.notna

Conversion
~~~~~~~~~~

   Index.astype
   Index.item
   Index.map
   Index.ravel
   Index.to_list
   Index.to_series
   Index.to_frame
   Index.view

Sorting
~~~~~~~

   Index.argsort
   Index.searchsorted
   Index.sort_values

Time-specific operations
~~~~~~~~~~~~~~~~~~~~~~~~

   Index.shift

Combining / joining / set operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Index.append
   Index.join
   Index.intersection
   Index.union
   Index.difference
   Index.symmetric_difference

Selecting
~~~~~~~~~

   Index.asof
   Index.asof_locs
   Index.get_indexer
   Index.get_indexer_for
   Index.get_indexer_non_unique
   Index.get_level_values
   Index.get_loc
   Index.get_slice_bound
   Index.isin
   Index.slice_indexer
   Index.slice_locs

.. _api.numericindex:

Numeric Index
-------------

   RangeIndex

.. We need this autosummary so that the methods are generated.
.. Separate block, since they aren't classes.

   RangeIndex.start
   RangeIndex.stop
   RangeIndex.step
   RangeIndex.from_range

.. _api.categoricalindex:

CategoricalIndex
----------------

   CategoricalIndex

Categorical components
~~~~~~~~~~~~~~~~~~~~~~

   CategoricalIndex.codes
   CategoricalIndex.categories
   CategoricalIndex.ordered
   CategoricalIndex.rename_categories
   CategoricalIndex.reorder_categories
   CategoricalIndex.add_categories
   CategoricalIndex.remove_categories
   CategoricalIndex.remove_unused_categories
   CategoricalIndex.set_categories
   CategoricalIndex.as_ordered
   CategoricalIndex.as_unordered

Modifying and computations
~~~~~~~~~~~~~~~~~~~~~~~~~~

   CategoricalIndex.map
   CategoricalIndex.equals

.. _api.intervalindex:

IntervalIndex
-------------

   IntervalIndex

IntervalIndex components
~~~~~~~~~~~~~~~~~~~~~~~~

   IntervalIndex.from_arrays
   IntervalIndex.from_tuples
   IntervalIndex.from_breaks
   IntervalIndex.left
   IntervalIndex.right
   IntervalIndex.mid
   IntervalIndex.closed
   IntervalIndex.length
   IntervalIndex.values
   IntervalIndex.is_empty
   IntervalIndex.is_non_overlapping_monotonic
   IntervalIndex.is_overlapping
   IntervalIndex.get_loc
   IntervalIndex.get_indexer
   IntervalIndex.set_closed
   IntervalIndex.contains
   IntervalIndex.overlaps
   IntervalIndex.to_tuples

.. _api.multiindex:

MultiIndex
----------

   IndexSlice

   MultiIndex

MultiIndex constructors
~~~~~~~~~~~~~~~~~~~~~~~

   MultiIndex.from_arrays
   MultiIndex.from_tuples
   MultiIndex.from_product
   MultiIndex.from_frame

MultiIndex properties
~~~~~~~~~~~~~~~~~~~~~

   MultiIndex.names
   MultiIndex.levels
   MultiIndex.codes
   MultiIndex.nlevels
   MultiIndex.levshape
   MultiIndex.dtypes

MultiIndex components
~~~~~~~~~~~~~~~~~~~~~

   MultiIndex.set_levels
   MultiIndex.set_codes
   MultiIndex.to_flat_index
   MultiIndex.to_frame
   MultiIndex.sortlevel
   MultiIndex.droplevel
   MultiIndex.swaplevel
   MultiIndex.reorder_levels
   MultiIndex.remove_unused_levels
   MultiIndex.drop
   MultiIndex.copy
   MultiIndex.append
   MultiIndex.truncate

MultiIndex selecting
~~~~~~~~~~~~~~~~~~~~

   MultiIndex.get_loc
   MultiIndex.get_locs
   MultiIndex.get_loc_level
   MultiIndex.get_indexer
   MultiIndex.get_level_values

.. _api.datetimeindex:

DatetimeIndex
-------------

   DatetimeIndex

Time/date components
~~~~~~~~~~~~~~~~~~~~

   DatetimeIndex.year
   DatetimeIndex.month
   DatetimeIndex.day
   DatetimeIndex.hour
   DatetimeIndex.minute
   DatetimeIndex.second
   DatetimeIndex.microsecond
   DatetimeIndex.nanosecond
   DatetimeIndex.date
   DatetimeIndex.time
   DatetimeIndex.timetz
   DatetimeIndex.dayofyear
   DatetimeIndex.day_of_year
   DatetimeIndex.dayofweek
   DatetimeIndex.day_of_week
   DatetimeIndex.weekday
   DatetimeIndex.quarter
   DatetimeIndex.tz
   DatetimeIndex.freq
   DatetimeIndex.freqstr
   DatetimeIndex.is_month_start
   DatetimeIndex.is_month_end
   DatetimeIndex.is_quarter_start
   DatetimeIndex.is_quarter_end
   DatetimeIndex.is_year_start
   DatetimeIndex.is_year_end
   DatetimeIndex.is_leap_year
   DatetimeIndex.inferred_freq

Selecting
~~~~~~~~~

   DatetimeIndex.indexer_at_time
   DatetimeIndex.indexer_between_time

Time-specific operations
~~~~~~~~~~~~~~~~~~~~~~~~

   DatetimeIndex.normalize
   DatetimeIndex.strftime
   DatetimeIndex.snap
   DatetimeIndex.tz_convert
   DatetimeIndex.tz_localize
   DatetimeIndex.round
   DatetimeIndex.floor
   DatetimeIndex.ceil
   DatetimeIndex.month_name
   DatetimeIndex.day_name

Conversion
~~~~~~~~~~

   DatetimeIndex.as_unit
   DatetimeIndex.to_period
   DatetimeIndex.to_pydatetime
   DatetimeIndex.to_series
   DatetimeIndex.to_frame

Methods
~~~~~~~

    DatetimeIndex.mean
    DatetimeIndex.std

TimedeltaIndex
--------------

   TimedeltaIndex

Components
~~~~~~~~~~

   TimedeltaIndex.days
   TimedeltaIndex.seconds
   TimedeltaIndex.microseconds
   TimedeltaIndex.nanoseconds
   TimedeltaIndex.components
   TimedeltaIndex.inferred_freq

Conversion
~~~~~~~~~~

   TimedeltaIndex.as_unit
   TimedeltaIndex.to_pytimedelta
   TimedeltaIndex.to_series
   TimedeltaIndex.round
   TimedeltaIndex.floor
   TimedeltaIndex.ceil
   TimedeltaIndex.to_frame

Methods
~~~~~~~

    TimedeltaIndex.mean

PeriodIndex
-----------

   PeriodIndex

Properties
~~~~~~~~~~

    PeriodIndex.day
    PeriodIndex.dayofweek
    PeriodIndex.day_of_week
    PeriodIndex.dayofyear
    PeriodIndex.day_of_year
    PeriodIndex.days_in_month
    PeriodIndex.daysinmonth
    PeriodIndex.end_time
    PeriodIndex.freq
    PeriodIndex.freqstr
    PeriodIndex.hour
    PeriodIndex.is_leap_year
    PeriodIndex.minute
    PeriodIndex.month
    PeriodIndex.quarter
    PeriodIndex.qyear
    PeriodIndex.second
    PeriodIndex.start_time
    PeriodIndex.week
    PeriodIndex.weekday
    PeriodIndex.weekofyear
    PeriodIndex.year

Methods
~~~~~~~

    PeriodIndex.asfreq
    PeriodIndex.strftime
    PeriodIndex.to_timestamp
