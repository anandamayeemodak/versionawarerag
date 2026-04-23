{{ header }}

.. _api.general_functions:

=================
General functions
=================

Data manipulations
~~~~~~~~~~~~~~~~~~

   melt
   pivot
   pivot_table
   crosstab
   cut
   qcut
   merge
   merge_ordered
   merge_asof
   concat
   get_dummies
   from_dummies
   factorize
   unique
   lreshape
   wide_to_long

Top-level missing data
~~~~~~~~~~~~~~~~~~~~~~

   isna
   isnull
   notna
   notnull

Top-level dealing with numeric data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   to_numeric

Top-level dealing with datetimelike data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   to_datetime
   to_timedelta
   date_range
   bdate_range
   period_range
   timedelta_range
   infer_freq

Top-level dealing with Interval data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   interval_range

Top-level evaluation
~~~~~~~~~~~~~~~~~~~~

   eval

Datetime formats
~~~~~~~~~~~~~~~~

   tseries.api.guess_datetime_format

Hashing
~~~~~~~

   util.hash_array
   util.hash_pandas_object

Importing from other DataFrame libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   api.interchange.from_dataframe
