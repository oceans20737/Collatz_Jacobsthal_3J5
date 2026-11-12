# -*- coding: utf-8 -*-
"""code_01_collatz_3j5.ipynb
"""

"""
Algebraic Formulation of the 3n+5 Collatz Operator in Jacobsthal Space:
The 3J + 5J(0,1) Transformation

Author: Hiroshi Harada
Date: December 12, 2026
License: MIT License
Copyright (c) 2026 Hiroshi Harada
"""

from typing import Tuple
import pandas as pd


# Maximum search depth used during J-normalization
MAX_EXPANSION_DEPTH = 20


def collatz_3n5_step(n: int) -> int:
    """
    Standard odd-node 3n+5 mapping.

    Computes

        n -> (3n + 5) / 2^k

    where k is chosen so that the result is odd.
    """

    m = 3 * n + 5

    while m % 2 == 0:
        m //= 2

    return m


def reduce_spinor(a: int, b: int) -> Tuple[int, int]:
    """
    J-space 2-adic Reduction.

    Traces the Jacobsthal recurrence in the reverse direction
    and returns a reduced representative spinor.
    """

    while (b - a) % 2 == 0:
        a_prev = (b - a) // 2
        b = a
        a = a_prev

    return a, b


def normalize_spinor(u: int, v: int) -> Tuple[int, int]:
    """
    J-Normalization by sequence expansion.

    Searches for an expanded spinor satisfying

        (2u - v) = 5 * 2^k

    and returns

        (normalized_u, normalized_v)

    where normalized_v is odd.
    """

    seq_u, seq_v = u, v

    for _ in range(MAX_EXPANSION_DEPTH):

        diff = 2 * seq_u - seq_v

        if diff > 0 and diff % 5 == 0:

            power_of_2 = diff // 5

            # Check whether power_of_2 is exactly a power of two
            if power_of_2 > 0 and (power_of_2 & (power_of_2 - 1)) == 0:

                norm_v = seq_v // power_of_2

                if norm_v % 2 == 1:

                    norm_u = seq_u // power_of_2

                    return norm_u, norm_v

        # Jacobsthal forward expansion
        next_u = seq_v
        next_v = seq_v + 2 * seq_u

        seq_u, seq_v = next_u, next_v

    # Fallback arithmetic reduction
    while v % 2 == 0:
        v //= 2

    return (v + 5) // 2, v


def generate_3n5_orbit(
    start_node: int,
    max_steps: int = 1000
) -> pd.DataFrame:
    """
    Generate a 3n+5 trajectory using the J-Spinor framework.
    """

    orbit_data = []

    seen_nodes = set()
    b = start_node

    for step in range(max_steps):

        # Standard spinor
        a = (b + 5) // 2

        # Reduced representative spinor
        red_a, red_b = reduce_spinor(a, b)

        # Affine transformation
        trans_a = 3 * red_a
        trans_b = 3 * red_b + 5

        # J-normalization
        norm_a, norm_b = normalize_spinor(trans_a, trans_b)

        # Verification against the standard 3n+5 map
        expected_next = collatz_3n5_step(b)

        assert norm_b == expected_next, (
            f"Verification failed at node {b}: "
            f"J-spinor result = {norm_b}, "
            f"standard result = {expected_next}"
        )

        orbit_data.append(
            {
                "Step": step,
                "Odd Node": b,
                "Standard J": f"J({a}, {b})",
                "Reduced J": f"J({red_a}, {red_b})",
                "3J + 5J(0,1)": f"J({trans_a}, {trans_b})",
                "Next J": f"J({norm_a}, {norm_b})",
            }
        )

        if norm_b in seen_nodes:

            orbit_data.append(
                {
                    "Step": step + 1,
                    "Odd Node": norm_b,
                    "Standard J": f"J({norm_a}, {norm_b})",
                    "Reduced J": "-",
                    "3J + 5J(0,1)": "-",
                    "Next J": "LOOP DETECTED",
                }
            )

            break

        seen_nodes.add(b)
        b = norm_b

    return pd.DataFrame(orbit_data)


def main():

    # Example:
    # 1, 5, 19, 23, 187, 347

    start_node = 347

    print(
        f"\nCalculating 3n+5 orbit for initial node: "
        f"{start_node}\n"
    )

    df_orbit = generate_3n5_orbit(start_node)

    print(df_orbit.to_markdown(index=False))

    csv_filename = f"collatz_3J5_{start_node}.csv"

    df_orbit.to_csv(csv_filename, index=False)

    print(
        f"\nOrbit successfully saved to "
        f"{csv_filename}"
    )


if __name__ == "__main__":
    main()