import numpy as np

def getBondDuration(y, face, couponRate, m, ppy = 1):
    t = np.arrange(1, (m*ppy)+1)
    pv = (1 + y/ppy)**(-t)
    cf = couponRate * face / ppy
    pvcf = pv * cf
    pvcfsum = pvcf.sum()
    dpvcfsum = (t * pvcf).sum()
    bondprice = pvcfsum + pv[-1] * face
    dbondprice = dpvcfsum + m*ppy * pv[-1] * face
    return ((dbondprice / bondprice) / ppy)
