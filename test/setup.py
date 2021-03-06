# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 00:27:26 2016

@author: drsmith
"""

import unittest
import fdp


class SetupNstxu(unittest.TestCase):
    """
    Unittest setup for nstxu machine and shot attribute
    """

    def setUp(self, shotnumber=204952):
        """
        Shot 204952: Valid MPTS, CHERS, BES, EFIT01,
        Filterscopes, Neutrons, Magnetics, NBI, USXR, MSE
        """
        self.nstxu = fdp.nstx()
        self.shotnumber = shotnumber
        self.shot = getattr(self.nstxu, 's'+repr(self.shotnumber))
