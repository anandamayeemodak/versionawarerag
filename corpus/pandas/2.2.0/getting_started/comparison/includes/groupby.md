pandas provides a flexible ``groupby`` mechanism that allows similar aggregations. See the

   tips_summed = tips.groupby(["sex", "smoker"])[["total_bill", "tip"]].sum()
   tips_summed
