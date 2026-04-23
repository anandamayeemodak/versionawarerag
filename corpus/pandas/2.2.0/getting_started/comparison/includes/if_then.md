The same operation in pandas can be accomplished using
the ``where`` method from ``numpy``.

   tips["bucket"] = np.where(tips["total_bill"] < 10, "low", "high")
   tips

   tips = tips.drop("bucket", axis=1)
