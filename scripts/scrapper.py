#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2021 Konrad Weihmann
# SPDX-License-Identifier: Unlicensed

import csv
import os

import urllib3
from bs4 import BeautifulSoup

_URL = 'https://www.osadl.org/fileadmin/checklists/matrix.html'
_DUMP = os.path.join(os.path.dirname(__file__), '..', 'osadl_matrix', 'osadl-matrix.csv')


def _get_document():
    http = urllib3.PoolManager()
    resp = http.request('GET', _URL)
    return BeautifulSoup(resp.data.decode('utf-8'), 'html.parser')

def _create_matrix(html):
    _csv = []
    table = html.find('table', {'id': 'compat-matrix'})
    for row in table.find_all('tr'):
        _csv.append([(''.join(col.find_all(text=True))).encode('ascii', 'ignore').decode('utf-8') for col in row.find_all('td')])


    with open(_DUMP, 'w') as csvfile:
        cwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for line in _csv[:-1]:
            if len(line) < 3:
                continue
            cwriter.writerow(line)

_create_matrix(_get_document())
