import numpy as np


def get_cutting_speed(tool_diameter, rotational_speed):
    """
    Parameters
    ----------
    tool_diameter : float or int
        Tool diameter in [mm].
    rotational_speed : float or int
        Rotational speed in [1/min].

    Returns
    -------
    Cutting speed in [m/s] rounded to 1 decimal place.

    """
    result = (tool_diameter / 1000) * (rotational_speed / 60) * np.pi
    return round(result, 1)


def get_feed_per_tooth(feed_speed, rotational_speed, teeth_number):
    """
    Parameters
    ----------
    feed_speed : float or int
        Feed speed in [m/min].
    rotational_speed : float or int
        Rotational speed in [1/min].
    teeth_number : int
            Number of teeth.

    Returns
    -------
    Feed per tooth in [mm] rounded to 1 decimal place.

    """
    result = (feed_speed * 1000) / (rotational_speed * teeth_number)
    return round(result, 1)


def get_feed_speed(feed_per_tooth, rotational_speed, teeth_number):
    """
    Parameters
    ----------
    feed_per_tooth : float or int
        Feed per tooth in [mm].
    rotational_speed : float or int
        Rotational speed in [1/min].
    teeth_number : int
            Number of teeth.

    Returns
    -------
    Feed speed in [m/min] rounded to 1 decimal place.

    """
    result = (feed_per_tooth / 1000) * rotational_speed * teeth_number
    return round(result, 1)


def get_engagement_angle(tool_diameter, cutting_depth):
    """
    Parameters
    ----------
    tool_diameter : float or int
        Tool diameter in [mm].
    cutting_depth : float or int
        Cutting depth in [mm].

    Returns
    -------
    Engagement angle in [deg].

    """
    tool_r = tool_diameter / 2
    cos_phi = (tool_r - cutting_depth) / tool_r
    return np.arccos(cos_phi) * 180 * (1 / np.pi)


def get_mean_chip_thickness(
    cutting_angle, tool_diameter, cutting_depth, feed_per_tooth
):
    """
    Parameters
    ----------
    cutting_angle : float or int
        Cutting angle in [deg].
    tool_diameter : float or int
        Tool diameter in [mm].
    cutting_depth : float or int
        Cutting depth in [mm].
    feed_per_tooth : float or int
        Feed per tooth in [mm].

    Returns
    -------
    Mean chip thickness in [mm] rounded to 3 decimal places.

    """
    sin_kappa = np.sin(cutting_angle * np.pi * (1 / 180))
    engagement_angle = get_engagement_angle(tool_diameter, cutting_depth)
    numerator = feed_per_tooth * cutting_depth * 360
    denominator = tool_diameter * np.pi * engagement_angle * sin_kappa
    result = numerator / denominator
    return round(result, 3)


def get_mean_chip_length(tool_diameter, cutting_depth):
    """
    Parameters
    ----------
    tool_diameter : float or int
        Tool diameter in [mm].
    cutting_depth : float or int
        Cutting depth in [mm].

    Returns
    -------
    Mean chip length in [mm] rounded to 2 decimal places.

    """
    engagement_angle = get_engagement_angle(tool_diameter, cutting_depth)
    result = tool_diameter * np.pi * (engagement_angle / 360)
    return round(result, 2)
