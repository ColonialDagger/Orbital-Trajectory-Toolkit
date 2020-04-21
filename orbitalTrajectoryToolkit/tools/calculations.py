import numpy


def deltav(wet, dry, exv, mode):
    if mode == 0:
        exv = exv*9.80665
    return exv*numpy.log((wet/dry))
