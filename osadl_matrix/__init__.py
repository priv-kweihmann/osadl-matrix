# SPDX-FileCopyrightText: 2021 Konrad Weihmann
# SPDX-License-Identifier: Unlicensed

import csv
import os
from enum import Enum

OSADL_MATRIX = os.path.join(os.path.dirname(__file__), 'osadl-matrix.csv')
OSADL_MATRIX_JSON = os.path.join(os.path.dirname(__file__), 'osadl-matrix.json')
__osadl_db = {}


class OSADLCompatibility(Enum):
    YES = True
    NO = False
    UNDEF = False

    @staticmethod
    def from_text(_in):
        if _in == 'Yes':
            return OSADLCompatibility.YES
        if _in == 'No':
            return OSADLCompatibility.NO
        return OSADLCompatibility.UNDEF


def __read_db(customdb=None):
    global __osadl_db
    with open(customdb or OSADL_MATRIX) as i:
        _reader = csv.DictReader(i, delimiter=',', quotechar='"')
        for row in _reader:
            key = row['Compatibility*']
            for k, v in row.items():
                if k == key:
                    continue
                __osadl_db[(key, k)] = OSADLCompatibility.from_text(v)


def is_compatible(outbound, inbound, customdb=None):
    """checks if the 'outbound' license is compatible with the 'inbound' license

    Args:
        outbound (string): SPDX ID for an outbound license, e.g. the license used for distribution of an application
        inbound (string): SPDX ID for an inbound license, e.g. the license used for a dependency of the application

    Returns:
        [OSADLCompatibility]: Either yes, no or undefined
    """
    if not __osadl_db:
        __read_db(customdb=customdb)
    if outbound == inbound:
        return OSADLCompatibility.YES
    return __osadl_db.get((outbound, inbound), OSADLCompatibility.UNDEF)
