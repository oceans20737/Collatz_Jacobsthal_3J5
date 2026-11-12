# **Algebraic Formulation of the 3n+5 Collatz Operator in Jacobsthal Space: The 3J + 5J(0,1) Transformation**

**Hiroshi Harada - November 12, 2026**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24160370.svg)](https://doi.org/10.5281/zenodo.24160370)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## **Overview**
This repository contains a research report and a Python simulator that implement this algebraic formulation of the "3n+5 problem"—an extended model of the Collatz conjecture—as affine transformations within Jacobsthal (J) space.

By defining the standard Collatz operation on two-component column vectors (J-Spinors) in J-space and isolating the additive noise `+5`, we propose a method that explicitly describes the multiplicative component of the orbital calculation:

**$$3\boldsymbol{J}(a,b) + 5\boldsymbol{J}(0,1)$$**

This algorithm enables the uniform description of all known loops in the 3n+5 space (1, 5, 19, 23, 187, 347) under a common dynamical framework while avoiding fractional states through J-Reduction and J-Normalization.

## **Files**
*   `REPORT_EN.md` : Research report (English version)
*   `REPORT_JP.md` : Research report (Japanese version)
*   `code_01_collatz_3j5.py` : Python script to generate and verify J-Spinor orbits

## **Theoretical Background**
The Python script in this study implements the following two algebraic methods:
1.  **J-Reduction (J-space 2-adic Reduction)**: Traces the orbital branch back to its root to extract a representative element (Reduced Spinor) that avoids the generation of fractions.
2.  **J-Normalization**: Applies sequence expansion and normalization on the J-sequence to the vector post-affine transformation, landing precisely on the standard spinor of the next node.

These algebraic methods reveal the separation structure of phase shifts and scalar multiplication that lies behind the conventional scalar operation of "k divisions by 2 ($1/2^k$)."

## **Requirements**
*   Python 3.8 or higher
*   `pandas` library

## **Usage**
When executed, the script calculates the J-Spinor orbit starting from the specified initial odd node (default is `347`) and automatically tracks it until a loop is detected.

```bash
# Install dependencies
pip install pandas

# Run the simulator
python code_01_collatz_3j5.py

```

Upon execution, a Markdown-formatted orbital transition table (**Table 1**) will be printed to the console, and a CSV file (e.g., `collatz_3J5_347.csv`) will be saved in the same directory. You can analyze the orbit of any odd node by modifying the `start_node` variable within the script.

## **License**

* **Python Source Code:** MIT License
* **Research Documents:** CC BY 4.0

Copyright (c) 2026 Hiroshi Harada
