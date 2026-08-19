import numpy as np

from scipy.optimize import minimize_scalar
from scipy.special import erfc


def helstrom_error(nbar):
   
    return 0.5 * (1 - np.sqrt(1 - np.exp(-4 * nbar)))


def homodyne_error(nbar):
   
    return 0.5 * erfc(np.sqrt(2 * nbar))


def no_click_probability(amplitude):
  
    return np.exp(-np.abs(amplitude) ** 2)


def click_probability(amplitude):

    return 1 - no_click_probability(amplitude)


def kennedy_error(nbar):


    alpha = np.sqrt(nbar)

    displaced_minus = -alpha + alpha
    displaced_plus = alpha + alpha

    error_given_minus = click_probability(displaced_minus)
    error_given_plus = no_click_probability(displaced_plus)

    return 0.5 * error_given_minus + 0.5 * error_given_plus


def fixed_displacement_error(nbar, beta):

    alpha = np.sqrt(nbar)

    amp_plus = alpha + beta
    amp_minus = -alpha + beta

    p0_plus = no_click_probability(amp_plus)
    p0_minus = no_click_probability(amp_minus)

    p1_plus = 1 - p0_plus
    p1_minus = 1 - p0_minus

    error_no_click = 0.5 * np.minimum(p0_plus, p0_minus)
    error_click = 0.5 * np.minimum(p1_plus, p1_minus)

    return error_no_click + error_click


def optimized_displacement(nbar):


    if np.isclose(nbar, 0):
        return 0.0, 0.5

    alpha = np.sqrt(nbar)

    result = minimize_scalar(
        lambda beta: fixed_displacement_error(nbar, beta),
        bounds=(0, 2 * alpha + 2),
        method="bounded"
    )

    return result.x, result.fun

def detector_outcome_probability(signal, beta, clicked):

    displaced_amplitude = signal + beta
    p_no_click = no_click_probability(displaced_amplitude)

    if clicked:
        return 1 - p_no_click

    return p_no_click


def two_stage_error(
    nbar,
    beta_first,
    beta_after_no_click,
    beta_after_click
):

    alpha_bin = np.sqrt(nbar / 2)

    total_error = 0.0

    for first_click in [False, True]:

        if first_click:
            beta_second = beta_after_click
        else:
            beta_second = beta_after_no_click

        for second_click in [False, True]:

            p_plus = (
                detector_outcome_probability(
                    +alpha_bin,
                    beta_first,
                    first_click
                )
                *
                detector_outcome_probability(
                    +alpha_bin,
                    beta_second,
                    second_click
                )
            )

            p_minus = (
                detector_outcome_probability(
                    -alpha_bin,
                    beta_first,
                    first_click
                )
                *
                detector_outcome_probability(
                    -alpha_bin,
                    beta_second,
                    second_click
                )
            )

            total_error += min(
                0.5 * p_plus,
                0.5 * p_minus
            )

    return total_error