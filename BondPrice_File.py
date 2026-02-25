import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    t = np.arange(1, (ppy*m)+1)
    pv = (1 + y/ppy)**(-t)
    cf = couponRate * face / ppy
    pvcf = pv * cf
    pvcfsum = pvcf.sum()
    bondprice = pvcfsum + face * pv[-1]
    return(bondprice)
