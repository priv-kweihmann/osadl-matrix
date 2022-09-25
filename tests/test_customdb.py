#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2022 Henrik Sandklef
# SPDX-License-Identifier: Unlicensed

import pytest
import osadl_matrix

class TestCustomMatrix():

    def test_supported_licenes_size(self):
        assert len(osadl_matrix.supported_licenses("tests/mini-matrix.csv")) == 2

    def test_supported_content(self):
        supported = osadl_matrix.supported_licenses("tests/mini-matrix.csv")
        assert "0BSD" in supported
        assert "AFL-2.0" in supported
        assert "MIT" not in supported
        assert osadl_matrix.is_compatible("AFL-2.0", "0BSD")
        assert not osadl_matrix.is_compatible("0BSD", "AFL-2.0")
