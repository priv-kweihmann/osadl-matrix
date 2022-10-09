# SPDX-FileCopyrightText: 2022 Konrad Weihmann
# SPDX-License-Identifier: Unlicensed

import pytest

import requests


class TestUpstreamLicensing():
    def test_license(self):
        needle = 'The raw data of the OSADL Open Source License Checklists are licensed under the Creative Commons Attribution 4.0 International license (CC-BY-4.0)'
        req = requests.get(
            url='https://www.osadl.org/Access-to-raw-data.oss-compliance-raw-data-access.0.html')
        assert needle in req.text
