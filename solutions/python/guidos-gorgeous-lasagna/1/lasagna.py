EXPECTED_BAKE_TIME = 40
"""Constant representing expected bake time in minutes."""


def bake_time_remaining(baking_time):
    """Calculate the remaining baking time.

    :param baking_time: The time the lasagna has been baking in the oven, in minutes.
    :return: The remaining baking time in minutes.
    """
    return EXPECTED_BAKE_TIME - baking_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time based on the number of layers.

    :param number_of_layers: The number of layers in the lasagna.
    :return: The preparation time in minutes.
    """
    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time for preparing and baking the lasagna.

    :param number_of_layers: The number of layers in the lasagna.
    :param elapsed_bake_time: The time the lasagna has been baking in the oven, in minutes.
    :return: The total elapsed time in minutes.
    """
    total = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return total