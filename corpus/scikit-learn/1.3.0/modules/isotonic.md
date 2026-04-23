.. _isotonic:

===================
Isotonic regression
===================

The class :class:`IsotonicRegression` fits a non-decreasing real function to
1-dimensional data. It solves the following problem:

  minimize :math:`\sum_i w_i (y_i - \hat{y}_i)^2`

  subject to :math:`\hat{y}_i \le \hat{y}_j` whenever :math:`X_i \le X_j`,

where the weights :math:`w_i` are strictly positive, and both `X` and `y` are
arbitrary real quantities.

The `increasing` parameter changes the constraint to

'auto' will automatically choose the constraint based on `Spearman's rank
correlation coefficient
<https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient>`_.

for predicting to unseen data. The predictions of :class:`IsotonicRegression`
thus form a function that is piecewise linear:
