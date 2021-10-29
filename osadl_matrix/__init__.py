# SPDX-FileCopyrightText: 2021 Konrad Weihmann
# SPDX-License-Identifier: Unlicensed

import csv
import os
from enum import Enum

OSADL_MATRIX = os.path.join(os.path.dirname(__file__), 'osadl-matrix.csv')
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


def __read_db():
    global __osadl_db
    with open(OSADL_MATRIX) as i:
        _reader = csv.DictReader(i, delimiter=',', quotechar='"')
        for row in _reader:
            key = row['Compatibility*']
            for k, v in row.items():
                if k == key:
                    continue
                __osadl_db[(key, k)] = OSADLCompatibility.from_text(v)


def is_compatible(a, b):
    """checks if license 'a' is compatible to license 'b'

    Args:
        a (string): SPDX ID
        b (string): SPDX ID

    Returns:
        [OSADLCompatibility]: Either yes, no or undefined
    """
    if not __osadl_db:
        __read_db()
    if a == b:
        return OSADLCompatibility.YES
    return __osadl_db.get((a, b), OSADLCompatibility.UNDEF)
