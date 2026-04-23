.. Places parent toc into the sidebar

.. _data-transforms:

Dataset transformations
-----------------------

scikit-learn provides a library of transformers, which may clean (see

feature representations.

Like other estimators, these are represented by classes with a ``fit`` method,
which learns model parameters (e.g. mean and standard deviation for
normalization) from a training set, and a ``transform`` method which applies
this transformation model to unseen data. ``fit_transform`` may be more
convenient and efficient for modelling and transforming the training data
simultaneously.

Combining such transformers, either in parallel or series is covered in

spaces into affinity matrices, while :ref:`preprocessing_targets` considers
transformations of the target space (e.g. categorical labels) for use in
scikit-learn.

    modules/compose
    modules/feature_extraction
    modules/preprocessing
    modules/impute
    modules/unsupervised_reduction
    modules/random_projection
    modules/kernel_approximation
    modules/metrics
    modules/preprocessing_targets
