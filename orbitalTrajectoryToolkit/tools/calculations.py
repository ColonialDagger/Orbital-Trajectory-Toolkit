import numpy
import math
from scipy.constants import gravitational_constant


def deltav(wet, dry, exv, mode):  # Mode 0 for ISP input, mode 1 for ExVel input
    if dry <= wet:
        if mode == 0:
            exv = isp_exvel(exv)
            # TODO: DOES G FOR ISP CHANGE BASED ON ORBITAL BODY?
        return exv*numpy.log((wet/dry))
    else:
        raise ValueError


def isp_exvel(exv):  # ISP to Exhaust Velocity conversion
    return exv * 9.80665


def twr(f, w, g):
    return f/(w*g)


def burntime(wet, exv, f, dv):  # TODO: Figure out burn time calculation
    time = (1-math.pow(math.e, (numpy.negative(dv)/exv)))*((wet*exv)/f)
    return time


def gravity_force(m1, m2, r):  # TODO: Add check for real world masses (i.e. Earth, Mars, Moon, etc.)
    return (gravitational_constant*m1*m2)/(r**2)
