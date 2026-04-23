.. _data_reduction:

=====================================
Unsupervised dimensionality reduction
=====================================

If your number of features is high, it may be useful to reduce it with an
unsupervised step prior to supervised steps. Many of the

can be used to reduce the dimensionality. Below we discuss two specific
example of this pattern that are heavily used.

    The unsupervised data reduction and the supervised estimator can be
    chained in one step. See :ref:`pipeline`.

PCA: principal component analysis
----------------------------------

capture well the variance of the original features. See :ref:`decompositions`.

   * :ref:`sphx_glr_auto_examples_applications_plot_face_recognition.py`

Random projections
-------------------

The module: :mod:`~sklearn.random_projection` provides several tools for data
reduction by random projections. See the relevant section of the
documentation: :ref:`random_projection`.

   * :ref:`sphx_glr_auto_examples_miscellaneous_plot_johnson_lindenstrauss_bound.py`

Feature agglomeration
------------------------

similarly.

   * :ref:`sphx_glr_auto_examples_cluster_plot_feature_agglomeration_vs_univariate_selection.py`
   * :ref:`sphx_glr_auto_examples_cluster_plot_digits_agglomeration.py`

   Note that if features have very different scaling or statistical
   properties, :class:`cluster.FeatureAgglomeration` may not be able to
   capture the links between related features. Using a
