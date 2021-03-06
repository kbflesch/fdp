# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 12:11:09 2016

@author: drsmith
"""

import fdp
    
nstxu = fdp.nstxu()

for shot in [nstxu.s140000, nstxu.s141000, nstxu.s141001, nstxu.s204620]:
    print('SHOT {}'.format(shot.shot))
    shot.bes.ch01.plot()
    shot.mpts.ne.plot()
    #shot.mpts.te.plot()
    #shot.mpts.plot()
    shot.chers.ti.plot()
    #shot.chers.spline.tis.plot()
    shot.usxr.hdown.hdown01.plot()
    #shot.usxr.hdown.plot()
    shot.magnetics.highf.plot()
    shot.magnetics.highn.highn_1.plot()