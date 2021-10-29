#!/bin/python3

# SPDX-FileCopyrightText: 2021 Henrik Sandklef
#
# SPDX-License-Identifier: GPL-3.0-or-later

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

import osadl_matrix

class TestMatrix(unittest.TestCase):
    def test_1(self):
        self.assertEqual(osadl_matrix.is_compatible("MIT", "BSD-3-Clause"), osadl_matrix.OSADLCompatibility.YES)

    def test_2(self):
        self.assertEqual(osadl_matrix.is_compatible("BSD-3-Clause", "MIT"), osadl_matrix.OSADLCompatibility.YES)

    def test_3(self):
        self.assertEqual(osadl_matrix.is_compatible("GPL-2.0-only", "BSD-3-Clause"), osadl_matrix.OSADLCompatibility.YES)

    def test_4(self):
        self.assertEqual(osadl_matrix.is_compatible("BSD-3-Clause", "GPL-2.0-only"), osadl_matrix.OSADLCompatibility.NO)

    def test_5(self):
        self.assertEqual(osadl_matrix.is_compatible("GPL-2.0-only", "LGPL-2.1-only"), osadl_matrix.OSADLCompatibility.YES)

    def test_6(self):
        self.assertEqual(osadl_matrix.is_compatible("GPL-2.0-only", "GPL-2.0-only"), osadl_matrix.OSADLCompatibility.YES)

    def test_7(self):
        self.assertEqual(osadl_matrix.is_compatible("My-Fairy-Little-License", "LGPL-2.1-only"), osadl_matrix.OSADLCompatibility.UNDEF)
        
if __name__ == '__main__':
    unittest.main()
