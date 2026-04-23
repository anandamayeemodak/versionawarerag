{{ header }}

.. _api.dataframe:

=========
DataFrame
=========

Constructor
~~~~~~~~~~~

   DataFrame

Attributes and underlying data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Axes**

   DataFrame.index
   DataFrame.columns

   DataFrame.dtypes
   DataFrame.info
   DataFrame.select_dtypes
   DataFrame.values
   DataFrame.axes
   DataFrame.ndim
   DataFrame.size
   DataFrame.shape
   DataFrame.memory_usage
   DataFrame.empty
   DataFrame.set_flags

Conversion
~~~~~~~~~~

   DataFrame.astype
   DataFrame.convert_dtypes
   DataFrame.infer_objects
   DataFrame.copy
   DataFrame.bool

Indexing, iteration
~~~~~~~~~~~~~~~~~~~

   DataFrame.head
   DataFrame.at
   DataFrame.iat
   DataFrame.loc
   DataFrame.iloc
   DataFrame.insert
   DataFrame.__iter__
   DataFrame.items
   DataFrame.iteritems
   DataFrame.keys
   DataFrame.iterrows
   DataFrame.itertuples
   DataFrame.lookup
   DataFrame.pop
   DataFrame.tail
   DataFrame.xs
   DataFrame.get
   DataFrame.isin
   DataFrame.where
   DataFrame.mask
   DataFrame.query

For more information on ``.at``, ``.iat``, ``.loc``, and
``.iloc``,  see the :ref:`indexing documentation <indexing>`.

Binary operator functions
~~~~~~~~~~~~~~~~~~~~~~~~~

   DataFrame.add
   DataFrame.sub
   DataFrame.mul
   DataFrame.div
   DataFrame.truediv
   DataFrame.floordiv
   DataFrame.mod
   DataFrame.pow
   DataFrame.dot
   DataFrame.radd
   DataFrame.rsub
   DataFrame.rmul
   DataFrame.rdiv
   DataFrame.rtruediv
   DataFrame.rfloordiv
   DataFrame.rmod
   DataFrame.rpow
   DataFrame.lt
   DataFrame.gt
   DataFrame.le
   DataFrame.ge
   DataFrame.ne
   DataFrame.eq
   DataFrame.combine
   DataFrame.combine_first

Function application, GroupBy & window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   DataFrame.apply
   DataFrame.applymap
   DataFrame.pipe
   DataFrame.agg
   DataFrame.aggregate
   DataFrame.transform
   DataFrame.groupby
   DataFrame.rolling
   DataFrame.expanding
   DataFrame.ewm

.. _api.dataframe.stats:

Computations / descriptive stats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   DataFrame.abs
   DataFrame.all
   DataFrame.any
   DataFrame.clip
   DataFrame.corr
   DataFrame.corrwith
   DataFrame.count
   DataFrame.cov
   DataFrame.cummax
   DataFrame.cummin
   DataFrame.cumprod
   DataFrame.cumsum
   DataFrame.describe
   DataFrame.diff
   DataFrame.eval
   DataFrame.kurt
   DataFrame.kurtosis
   DataFrame.mad
   DataFrame.max
   DataFrame.mean
   DataFrame.median
   DataFrame.min
   DataFrame.mode
   DataFrame.pct_change
   DataFrame.prod
   DataFrame.product
   DataFrame.quantile
   DataFrame.rank
   DataFrame.round
   DataFrame.sem
   DataFrame.skew
   DataFrame.sum
   DataFrame.std
   DataFrame.var
   DataFrame.nunique
   DataFrame.value_counts

Reindexing / selection / label manipulation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   DataFrame.add_prefix
   DataFrame.add_suffix
   DataFrame.align
   DataFrame.at_time
   DataFrame.between_time
   DataFrame.drop
   DataFrame.drop_duplicates
   DataFrame.duplicated
   DataFrame.equals
   DataFrame.filter
   DataFrame.first
   DataFrame.head
   DataFrame.idxmax
   DataFrame.idxmin
   DataFrame.last
   DataFrame.reindex
   DataFrame.reindex_like
   DataFrame.rename
   DataFrame.rename_axis
   DataFrame.reset_index
   DataFrame.sample
   DataFrame.set_axis
   DataFrame.set_index
   DataFrame.tail
   DataFrame.take
   DataFrame.truncate

.. _api.dataframe.missing:

Missing data handling
~~~~~~~~~~~~~~~~~~~~~

   DataFrame.backfill
   DataFrame.bfill
   DataFrame.dropna
   DataFrame.ffill
   DataFrame.fillna
   DataFrame.interpolate
   DataFrame.isna
   DataFrame.isnull
   DataFrame.notna
   DataFrame.notnull
   DataFrame.pad
   DataFrame.replace

Reshaping, sorting, transposing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   DataFrame.droplevel
   DataFrame.pivot
   DataFrame.pivot_table
   DataFrame.reorder_levels
   DataFrame.sort_values
   DataFrame.sort_index
   DataFrame.nlargest
   DataFrame.nsmallest
   DataFrame.swaplevel
   DataFrame.stack
   DataFrame.unstack
   DataFrame.swapaxes
   DataFrame.melt
   DataFrame.explode
   DataFrame.squeeze
   DataFrame.to_xarray
   DataFrame.T
   DataFrame.transpose

Combining / comparing / joining / merging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   DataFrame.append
   DataFrame.assign
   DataFrame.compare
   DataFrame.join
   DataFrame.merge
   DataFrame.update

Time Series-related
~~~~~~~~~~~~~~~~~~~

   DataFrame.asfreq
   DataFrame.asof
   DataFrame.shift
   DataFrame.slice_shift
   DataFrame.tshift
   DataFrame.first_valid_index
   DataFrame.last_valid_index
   DataFrame.resample
   DataFrame.to_period
   DataFrame.to_timestamp
   DataFrame.tz_convert
   DataFrame.tz_localize

.. _api.frame.flags:

Flags
~~~~~

Flags refer to attributes of the pandas object. Properties of the dataset (like
the date is was recorded, the URL it was accessed from, etc.) should be stored
in :attr:`DataFrame.attrs`.

   Flags

.. _api.frame.metadata:

Metadata
~~~~~~~~

   DataFrame.attrs

.. _api.dataframe.plotting:

Plotting
~~~~~~~~
``DataFrame.plot`` is both a callable method and a namespace attribute for
specific plotting methods of the form ``DataFrame.plot.<kind>``.

   DataFrame.plot

   DataFrame.plot.area
   DataFrame.plot.bar
   DataFrame.plot.barh
   DataFrame.plot.box
   DataFrame.plot.density
   DataFrame.plot.hexbin
   DataFrame.plot.hist
   DataFrame.plot.kde
   DataFrame.plot.line
   DataFrame.plot.pie
   DataFrame.plot.scatter

   DataFrame.boxplot
   DataFrame.hist

.. _api.frame.sparse:

Sparse accessor
~~~~~~~~~~~~~~~

Sparse-dtype specific methods and attributes are provided under the
``DataFrame.sparse`` accessor.

   DataFrame.sparse.density

   DataFrame.sparse.from_spmatrix
   DataFrame.sparse.to_coo
   DataFrame.sparse.to_dense

Serialization / IO / conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   DataFrame.from_dict
   DataFrame.from_records
   DataFrame.to_orc
   DataFrame.to_parquet
   DataFrame.to_pickle
   DataFrame.to_csv
   DataFrame.to_hdf
   DataFrame.to_sql
   DataFrame.to_dict
   DataFrame.to_excel
   DataFrame.to_json
   DataFrame.to_html
   DataFrame.to_feather
   DataFrame.to_latex
   DataFrame.to_stata
   DataFrame.to_gbq
   DataFrame.to_records
   DataFrame.to_string
   DataFrame.to_clipboard
   DataFrame.to_markdown
   DataFrame.style
   DataFrame.__dataframe__
