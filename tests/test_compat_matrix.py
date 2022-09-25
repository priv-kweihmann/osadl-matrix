# SPDX-FileCopyrightText: 2021 Konrad Weihmann
# SPDX-FileCopyrightText: 2022 Henrik Sandklef
# SPDX-License-Identifier: Unlicensed

import pytest
import osadl_matrix

class TestMatrix():
    def test_1(self):        
        assert osadl_matrix.is_compatible("MIT", "BSD-3-Clause")

    def test_2(self):
        assert osadl_matrix.is_compatible("BSD-3-Clause", "MIT")

    def test_3(self):
        assert osadl_matrix.is_compatible("GPL-2.0-only", "BSD-3-Clause")

    def test_4(self):
        assert not osadl_matrix.is_compatible("BSD-3-Clause", "GPL-2.0-only")

    def test_5(self):
        assert osadl_matrix.is_compatible("GPL-2.0-only", "LGPL-2.1-only")

    def test_6(self):
        assert osadl_matrix.is_compatible("GPL-2.0-only", "GPL-2.0-only")

    def test_7(self):
        assert not osadl_matrix.is_compatible("My-Fairy-Little-License", "LGPL-2.1-only")

    def test_8(self):
        assert osadl_matrix.is_compatible("zlib-acknowledgement", "zlib-acknowledgement")

    def test_9(self):
        assert not osadl_matrix.is_compatible("LGPL-2.1-only", "GPL-2.0-only")

    def test_10(self):
        assert not osadl_matrix.is_compatible("MPL-2.0", "APL-2.0")

    def test_11(self):
        assert osadl_matrix.get_compatibility("MPL-2.0", "AFL-2.0")  == osadl_matrix.OSADLCompatibility.UNKNOWN

    def test_12(self):
        assert osadl_matrix.get_compatibility("GPL-2.0-only", "EPL-2.0")  == osadl_matrix.OSADLCompatibility.CHECKDEP

    def test_13(self):
        assert osadl_matrix.get_compatibility("Unfairy-license", "EPL-2.0")  == osadl_matrix.OSADLCompatibility.UNDEF

    def test_14(self):
        assert osadl_matrix.get_compatibility("A", "A")  == osadl_matrix.OSADLCompatibility.UNDEF

