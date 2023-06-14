# SPDX-FileCopyrightText: 2023 Henrik Sandklef
# SPDX-License-Identifier: Unlicensed

import pytest
import osadl_matrix

mini_matrix = "tests/mini-matrix.json"
mini_matrix_csv = "tests/mini-matrix.csv"

class TestCustomMatrix():

    def test_supported_licenes_size(self):
        assert len(osadl_matrix.supported_licenses(mini_matrix)) == 3

    def test_supported_licenes_size_csv(self):
        assert len(osadl_matrix.supported_licenses(mini_matrix_csv)) == 3

    def test_supported_licenses(self):
        supported = osadl_matrix.supported_licenses(mini_matrix)
        assert "BSD-3-Clause" in supported
        assert "Dummy" in supported
        assert "GPL-2.0-OR-LATER" not in supported
    
    def test_supported_licenses_csv(self):
        supported = osadl_matrix.supported_licenses(mini_matrix_csv)
        assert "BSD-3-Clause" in supported
        assert "Dummy" in supported
        assert "GPL-2.0-OR-LATER" not in supported
        
    def test_compats(self):
        assert osadl_matrix.is_compatible("BSD-3-Clause", "BSD-3-Clause", mini_matrix)
        assert osadl_matrix.is_compatible("BSD-3-Clause", "Dummy", mini_matrix)
        assert osadl_matrix.is_compatible("GPL-2.0-or-later", "BSD-3-Clause", mini_matrix)
        assert osadl_matrix.is_compatible("BSD-3-Clause", "BSD-3-Clause", mini_matrix)
        assert osadl_matrix.is_compatible("BSD-3-Clause", "Dummy", mini_matrix)
        assert osadl_matrix.is_compatible("GPL-2.0-or-later", "BSD-3-Clause", mini_matrix)
        
    def test_not_compats(self):
        assert not osadl_matrix.is_compatible("BSD-3-Clause", "GPL-2.0-or-later", mini_matrix)
        assert not osadl_matrix.is_compatible("Dummy", "BSD-3-Clause", mini_matrix)
        
    def test_not_supported(self):
        assert not osadl_matrix.is_compatible("Dummy", "Donkey", mini_matrix)
        assert not osadl_matrix.is_compatible("Donkey", "Dummy", mini_matrix)
        assert not osadl_matrix.is_compatible("Monkey", "Donkey", mini_matrix)

    def test_get_compat(self):
        assert osadl_matrix.get_compatibility("GPL-2.0-or-later", "BSD-3-Clause", mini_matrix) == osadl_matrix.OSADLCompatibility.YES
        assert osadl_matrix.get_compatibility("BSD-3-Clause", "GPL-2.0-or-later", mini_matrix) == osadl_matrix.OSADLCompatibility.NO
        assert osadl_matrix.get_compatibility("GPL-2.0-or-later", "Not-existing-license", mini_matrix) == osadl_matrix.OSADLCompatibility.UNDEF
        
