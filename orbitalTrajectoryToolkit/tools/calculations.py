import numpy


def deltav(wet, dry, exv, mode):  # Mode 0 for ISP input, mode 1 for ExVel input
    if dry <= wet:
        if mode == 0:
            exv = exv * 9.80665
            # TODO: DOES G FOR ISP CHANGE BASED ON ORBITAL BODY?
        return exv*numpy.log((wet/dry))
    else:
        raise ValueError


def twr(f, w, g):
    return f/(w*g)
