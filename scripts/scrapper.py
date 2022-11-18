#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2021 Konrad Weihmann
# SPDX-License-Identifier: Unlicensed

import csv
import json
import os

import urllib3

_URL = 'https://www.osadl.org/fileadmin/checklists/matrix.json'
_DUMP_CSV = os.path.join(os.path.dirname(__file__), '..', 'osadl_matrix', 'osadl-matrix.csv')
_DUMP_JSON = os.path.join(os.path.dirname(__file__), '..', 'osadl_matrix', 'osadl-matrix.json')


def _get_document():
    http = urllib3.PoolManager()
    resp = http.request('GET', _URL)
    return json.loads(resp.data.decode('utf-8'))

def _create_matrix(raw):
    # dump to json
    with open(_DUMP_JSON, 'w') as jsonfile:
        json.dump(raw, jsonfile, sort_keys=True)

    # create a csv

    raw = { k:v for k, v in raw.items() if isinstance(v, dict)}

    _csv = [
        ['Compatibility*'] + sorted(raw.keys())
    ]

    for key in sorted(raw.keys()):
        _line = [key]
        for key2 in sorted(raw.keys()):
            _line.append(raw[key][key2])
        _csv.append(_line)

    with open(_DUMP_CSV, 'w') as csvfile:
        cwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for line in _csv:
            if len(line) < 3:
                continue
            cwriter.writerow(line)

_create_matrix(_get_document())
