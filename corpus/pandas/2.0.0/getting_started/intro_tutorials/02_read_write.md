.. _10min_tut_02_read_write:

{{ header }}

    import pandas as pd

    <div class="card gs-data">
        <div class="card-header gs-data-header">
            <div class="gs-data-title">
                Data used for this tutorial:
            </div>
        </div>
        <ul class="list-group list-group-flush">
            <li class="list-group-item gs-data-list">

            </li>
        </ul>
    </div>

How do I read and write tabular data?
=====================================

    <ul class="task-bullet">
        <li>

I want to analyze the Titanic passenger data, available as a CSV file.

    titanic = pd.read_csv("data/titanic.csv")

pandas provides the :func:`read_csv` function to read data stored as a csv
file into a pandas ``DataFrame``. pandas supports many different file
formats or data sources out of the box (csv, excel, sql, json, parquet,
…), each of them with the prefix ``read_*``.

        </li>
    </ul>

Make sure to always have a check on the data after reading in the
data. When displaying a ``DataFrame``, the first and last 5 rows will be
shown by default:

    titanic

    <ul class="task-bullet">
        <li>

I want to see the first 8 rows of a pandas DataFrame.

    titanic.head(8)

To see the first N rows of a ``DataFrame``, use the :meth:`~DataFrame.head` method with
the required number of rows (in this case 8) as argument.

        </li>
    </ul>

    Interested in the last N rows instead? pandas also provides a

    10 rows of the DataFrame.

A check on how pandas interpreted each of the column data types can be
done by requesting the pandas ``dtypes`` attribute:

    titanic.dtypes

For each of the columns, the used data type is enlisted. The data types
in this ``DataFrame`` are integers (``int64``), floats (``float64``) and
strings (``object``).

    When asking for the ``dtypes``, no brackets are used!
    ``dtypes`` is an attribute of a ``DataFrame`` and ``Series``. Attributes
    of ``DataFrame`` or ``Series`` do not need brackets. Attributes
    represent a characteristic of a ``DataFrame``/``Series``, whereas a
    method (which requires brackets) *do* something with the
    ``DataFrame``/``Series`` as introduced in the :ref:`first tutorial <10min_tut_01_tableoriented>`.

    <ul class="task-bullet">
        <li>

My colleague requested the Titanic data as a spreadsheet.

    titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)

Whereas ``read_*`` functions are used to read data to pandas, the
``to_*`` methods are used to store data. The :meth:`~DataFrame.to_excel` method stores
the data as an excel file. In the example here, the ``sheet_name`` is
named *passengers* instead of the default *Sheet1*. By setting
``index=False`` the row index labels are not saved in the spreadsheet.

        </li>
    </ul>

The equivalent read function :meth:`~DataFrame.read_excel` will reload the data to a
``DataFrame``:

    titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")

    titanic.head()

   import os

   os.remove("titanic.xlsx")

    <ul class="task-bullet">
        <li>

I’m interested in a technical summary of a ``DataFrame``

    titanic.info()

The method :meth:`~DataFrame.info` provides technical information about a
``DataFrame``, so let’s explain the output in more detail:

-  It is indeed a :class:`DataFrame`.
-  There are 891 entries, i.e. 891 rows.
-  Each row has a row label (aka the ``index``) with values ranging from
   0 to 890.
-  The table has 12 columns. Most columns have a value for each of the
   rows (all 891 values are ``non-null``). Some columns do have missing
   values and less than 891 ``non-null`` values.
-  The columns ``Name``, ``Sex``, ``Cabin`` and ``Embarked`` consists of
   textual data (strings, aka ``object``). The other columns are
   numerical data with some of them whole numbers (aka ``integer``) and
   others are real numbers (aka ``float``).
-  The kind of data (characters, integers,…) in the different columns
   are summarized by listing the ``dtypes``.
-  The approximate amount of RAM used to hold the DataFrame is provided
   as well.

        </li>
    </ul>

    <div class="shadow gs-callout gs-callout-remember">
        <h4>REMEMBER</h4>

-  Getting data in to pandas from many different file formats or data
   sources is supported by ``read_*`` functions.
-  Exporting data out of pandas is provided by different
   ``to_*``\ methods.
-  The ``head``/``tail``/``info`` methods and the ``dtypes`` attribute
   are convenient for a first check.

    </div>

    <div class="d-flex flex-row gs-torefguide">
        <span class="badge badge-info">To user guide</span>

For a complete overview of the input and output possibilities from and to pandas, see the user guide section about :ref:`reader and writer functions <io>`.

    </div>
