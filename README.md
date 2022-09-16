msmath package
==============

mathematical Python classes

Classes implementing
* finite fields (ffield.py)
* Z_m finite rings (fring.py)
* rationals: real, complex, quaternion (rational.py)
* quaternions (quaternion.py)
* binary matrices and matrices over any ring (matrix.py)
* single-variable polynomials and rational functions with coefficients in any field (poly.py)
* undirected graphs (graph.py)
* bitstrings (bitstrings.py)

Support modules:
* conversions.py: utilities for Python 2 and 3 compatibility
* numfuns.py: assorted numerical functions
* ffpoly.py: functions to enumerate irreducible polynomials mod p

Demonstration modules:
* bch.py: create BCH codes using the classes
* share.py: secret sharing using finite fields
* optable.py: create a printable op table for a finite ring

Standalone test programs for the various classes are included:
* test_bitstring.py tests bitstring classes
* test_ffield.py primarily tests ffield.py, but also uses matrix.py and poly.py
* test_matrix.py primarily tests matrix.py, but also uses poly.py and rational.py
* test_poly.py primarily tests poly.py, but also uses ffield.py and rational.py
* test_rational.py tests rational classes
