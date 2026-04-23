.. Places parent toc into the sidebar

.. _sample_generators:

Generated datasets
==================

In addition, scikit-learn includes various random sample generators that
can be used to build artificial datasets of controlled size and complexity.

Generators for classification and clustering
--------------------------------------------

These generators produce a matrix of features and corresponding discrete
targets.

Single label
~~~~~~~~~~~~

Both :func:`make_blobs` and :func:`make_classification` create multiclass
datasets by allocating each class one or more normally-distributed clusters of
points.  :func:`make_blobs` provides greater control regarding the centers and
standard deviations of each cluster, and is used to demonstrate clustering.

correlated, redundant and uninformative features; multiple Gaussian clusters
per class; and linear transformations of the feature space.

near-equal-size classes separated by concentric hyperspheres.

datasets that are challenging to certain algorithms (e.g. centroid-based
clustering or linear classification), including optional Gaussian noise.
They are useful for visualization. :func:`make_circles` produces Gaussian data
with a spherical decision boundary for binary classification, while

Multilabel
~~~~~~~~~~

labels, reflecting a bag of words drawn from a mixture of topics. The number of
topics for each document is drawn from a Poisson distribution, and the topics
themselves are drawn from a fixed random distribution. Similarly, the number of
words is drawn from Poisson, with words drawn from a multinomial, where each
topic defines a probability distribution over words. Simplifications with
respect to true bag-of-words mixtures include:

* Per-topic word distributions are independently drawn, where in reality all
  would be affected by a sparse base distribution, and would be correlated.
* For a document generated from multiple topics, all topics are weighted
  equally in generating its bag of words.
* Documents without labels words at random, rather than from a base
  distribution.

Biclustering
~~~~~~~~~~~~

   make_biclusters
   make_checkerboard

Generators for regression
-------------------------

random linear combination of random features, with noise. Its informative
features may be uncorrelated, or low rank (few features account for most of the
variance).

Other regression generators generate functions deterministically from
randomized features.  :func:`make_sparse_uncorrelated` produces a target as a
linear combination of four features with fixed coefficients.
Others encode explicitly non-linear relations:

Generators for manifold learning
--------------------------------

   make_s_curve
   make_swiss_roll

Generators for decomposition
----------------------------

   make_low_rank_matrix
   make_sparse_coded_signal
   make_spd_matrix
   make_sparse_spd_matrix
