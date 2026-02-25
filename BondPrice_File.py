import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    t = np.arange(1, (ppy*m)+1)
    pv = (1 + y/ppy)**(-t)
    pvcf = couponRate * face / ppy
    pvcfsum = pvcf * pv.sum()
    bondprice = pvcfsum + face * pv[-1]
    return(bondprice)
