{{ header }}

.. _api.io:

============
Input/output
============

Pickling
~~~~~~~~

   read_pickle
   DataFrame.to_pickle

Flat file
~~~~~~~~~

   read_table
   read_csv
   DataFrame.to_csv
   read_fwf

Clipboard
~~~~~~~~~

   read_clipboard
   DataFrame.to_clipboard

Excel
~~~~~

   read_excel
   DataFrame.to_excel
   ExcelFile
   ExcelFile.book
   ExcelFile.sheet_names
   ExcelFile.parse

   Styler.to_excel

   ExcelWriter

JSON
~~~~

   read_json
   json_normalize
   DataFrame.to_json

   build_table_schema

HTML
~~~~

   read_html
   DataFrame.to_html

   Styler.to_html

XML
~~~~

   read_xml
   DataFrame.to_xml

Latex
~~~~~

   DataFrame.to_latex

   Styler.to_latex

HDFStore: PyTables (HDF5)
~~~~~~~~~~~~~~~~~~~~~~~~~

   read_hdf
   HDFStore.put
   HDFStore.append
   HDFStore.get
   HDFStore.select
   HDFStore.info
   HDFStore.keys
   HDFStore.groups
   HDFStore.walk

   One can store a subclass of :class:`DataFrame` or :class:`Series` to HDF5,
   but the type of the subclass is lost upon storing.

Feather
~~~~~~~

   read_feather
   DataFrame.to_feather

Parquet
~~~~~~~

   read_parquet
   DataFrame.to_parquet

ORC
~~~

   read_orc
   DataFrame.to_orc

SAS
~~~

   read_sas

SPSS
~~~~

   read_spss

SQL
~~~

   read_sql_table
   read_sql_query
   read_sql
   DataFrame.to_sql

Google BigQuery
~~~~~~~~~~~~~~~

   read_gbq

STATA
~~~~~

   read_stata
   DataFrame.to_stata

   StataReader.data_label
   StataReader.value_labels
   StataReader.variable_labels
   StataWriter.write_file
