#!/bin/python3

# SPDX-FileCopyrightText: 2021 Henrik Sandklef
#
# SPDX-License-Identifier: GPL-3.0-or-later

import pytest

import osadl_matrix

class TestInput():
    def test_json(self):
        import json
        import osadl_matrix

        with open(osadl_matrix.OSADL_MATRIX_JSON) as i:
            assert any(json.load(i).keys())

    def test_csv(self):
        import csv
        import osadl_matrix

        with open(osadl_matrix.OSADL_MATRIX) as csvinput:
            creader = csv.reader(csvinput, delimiter=',', quotechar='"')
            assert any(creader)

    def test_values(self):
        import json
        import osadl_matrix

        _values = set()
        with open(osadl_matrix.OSADL_MATRIX_JSON) as i:
            for _,v in json.load(i).items():
                _values.update(v.values())

        assert sorted(_values) == sorted(['Check dependency', 'Same', 'Yes', 'No', 'Unknown'])
