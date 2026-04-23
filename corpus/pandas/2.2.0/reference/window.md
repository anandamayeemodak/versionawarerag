{{ header }}

.. _api.window:

======
Window
======

calls: :func:`pandas.DataFrame.ewm` and :func:`pandas.Series.ewm`.

.. _api.functions_rolling:

Rolling window functions
------------------------

   Rolling.count
   Rolling.sum
   Rolling.mean
   Rolling.median
   Rolling.var
   Rolling.std
   Rolling.min
   Rolling.max
   Rolling.corr
   Rolling.cov
   Rolling.skew
   Rolling.kurt
   Rolling.apply
   Rolling.aggregate
   Rolling.quantile
   Rolling.sem
   Rolling.rank

.. _api.functions_window:

Weighted window functions
-------------------------

   Window.mean
   Window.sum
   Window.var
   Window.std

.. _api.functions_expanding:

Expanding window functions
--------------------------

   Expanding.count
   Expanding.sum
   Expanding.mean
   Expanding.median
   Expanding.var
   Expanding.std
   Expanding.min
   Expanding.max
   Expanding.corr
   Expanding.cov
   Expanding.skew
   Expanding.kurt
   Expanding.apply
   Expanding.aggregate
   Expanding.quantile
   Expanding.sem
   Expanding.rank

.. _api.functions_ewm:

Exponentially-weighted window functions
---------------------------------------

   ExponentialMovingWindow.mean
   ExponentialMovingWindow.sum
   ExponentialMovingWindow.std
   ExponentialMovingWindow.var
   ExponentialMovingWindow.corr
   ExponentialMovingWindow.cov

.. _api.indexers_window:

Window indexer
--------------

Base class for defining custom window boundaries.

   api.indexers.BaseIndexer
   api.indexers.FixedForwardWindowIndexer
   api.indexers.VariableOffsetWindowIndexer
