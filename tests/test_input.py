# SPDX-FileCopyrightText: 2022 Konrad Weihmann
# SPDX-License-Identifier: Unlicensed

import pytest

import osadl_matrix

class TestInput():
    def test_json(self):
        import json

        with open(osadl_matrix.OSADL_MATRIX_JSON) as i:
            assert any(json.load(i).keys())

    def test_csv(self):
        import csv

        with open(osadl_matrix.OSADL_MATRIX) as csvinput:
            creader = csv.reader(csvinput, delimiter=',', quotechar='"')
            assert any(creader)

    def test_values(self):
        import json

        _values = set()
        with open(osadl_matrix.OSADL_MATRIX_JSON) as i:
            for _,v in json.load(i).items():
                if not isinstance(v, dict):
                    continue
                _values.update(v.values())

        assert sorted(_values) == sorted(['Check dependency', 'Same', 'Yes', 'No', 'Unknown'])
