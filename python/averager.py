#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2015 RadioGIS.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

class averager(gr.sync_block):
    """
    Toma vector de entrada que mide N (Vector size) y lo promedia n veces (Averager size)
    """
    def __init__(self, N, n):
        self.N = N
        self.n = n
        gr.sync_block.__init__(self,
            name="averager",
            in_sig=[(numpy.float32, N * n)],
            out_sig=[(numpy.float32, N)])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        out[:] = numpy.average([in0[:,x:x+self.N] for x in range(0, out.shape[1], self.N)], 0)
        return len(output_items[0])

