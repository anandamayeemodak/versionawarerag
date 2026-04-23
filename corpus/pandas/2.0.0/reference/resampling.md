{{ header }}

.. _api.resampling:

==========
Resampling
==========

Resampler objects are returned by resample calls: :func:`pandas.DataFrame.resample`, :func:`pandas.Series.resample`.

Indexing, iteration
~~~~~~~~~~~~~~~~~~~

   Resampler.__iter__
   Resampler.groups
   Resampler.indices
   Resampler.get_group

Function application
~~~~~~~~~~~~~~~~~~~~

   Resampler.apply
   Resampler.aggregate
   Resampler.transform
   Resampler.pipe

Upsampling
~~~~~~~~~~

   Resampler.ffill
   Resampler.bfill
   Resampler.nearest
   Resampler.fillna
   Resampler.asfreq
   Resampler.interpolate

Computations / descriptive stats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Resampler.count
   Resampler.nunique
   Resampler.first
   Resampler.last
   Resampler.max
   Resampler.mean
   Resampler.median
   Resampler.min
   Resampler.ohlc
   Resampler.prod
   Resampler.size
   Resampler.sem
   Resampler.std
   Resampler.sum
   Resampler.var
   Resampler.quantile
