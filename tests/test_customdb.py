#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2022 Henrik Sandklef
# SPDX-License-Identifier: Unlicensed

import pytest
import osadl_matrix

class TestCusotmMatrix():

    def test_supported_licenes(self):
        assert len(osadl_matrix.supported_licenses("tests/mini-matrix.csv")) == 2
