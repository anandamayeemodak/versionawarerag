The same operations are expressed in pandas below.

Keep certain columns
''''''''''''''''''''

   tips[["sex", "total_bill", "tip"]]

Drop a column
'''''''''''''

   tips.drop("sex", axis=1)

Rename a column
'''''''''''''''

   tips.rename(columns={"total_bill": "total_bill_2"})
