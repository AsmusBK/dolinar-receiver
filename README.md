# Dolinar Receiver Simulation

This project investigates the **Dolinar receiver**, an adaptive quantum receiver for discriminating non-orthogonal coherent states.

## Project synopsis

I'll be working alone on the Dolinar receiver. My goal is to simulate the adaptive feedback used and investigate how different feedback strategies affect the outcome. I will compare the adaptive receiver with fixed approaches and make plots to visualise the differences. If time allows, I will also investigate optimization methods inspired by recent work on adaptive learning for quantum receivers.

## Goals (Possible changes)

Simulate discrimination between binary coherent states.
Implement fixed and adaptive displacement strategies.
Investigate how feedback affects the discrimination error.
Compare the simulated receivers with theoretical benchmarks such as the Helstrom bound.
Visualise the performance of the different strategies.
If time allows, investigate numerical optimization or adaptive-learning approaches.

## Tools

The project is written in Python and uses:

NumPy
SciPy
Matplotlib
QuTiP
Jupyter

Dependencies and the Python environment are managed using `uv`.

## References

* S. Izumi, J. S. Neergaard-Nielsen, and U. L. Andersen, *Tomography of a Feedback Measurement with Photon Detection*, Physical Review Letters **124**, 070502 (2020).
* C. Cui et al., *Quantum receiver enhanced by adaptive learning*, Light: Science & Applications **11**, 344 (2022).

## Status

Work in progress.