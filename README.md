# osadl-matrix

This is a machine readable version of the [OSADL license compatibility matrix](https://www.osadl.org/Access-to-raw-data.oss-compliance-raw-data-access.0.html) as a python library.

## License

This module is licensed under [Unlicensed](LICENSE.Unlicensed) license. Feel free to do whatever you want with it.

### Data license

The raw data of the OSADL Open Source License Checklists are licensed under the Creative Commons Attribution 4.0 International license (CC-BY-4.0), https://creativecommons.org/licenses/by/4.0/.

© 2017 - 2021 Open Source Automation Development Lab (OSADL) eG and contributors, info@osadl.org

Further information can be found [here](https://www.osadl.org/Access-to-raw-data.oss-compliance-raw-data-access.0.html)
A copy of the CC-BY-4.0 text can be found [here](LICENSE.ccby40)

## Disclaimer

We are not affiliated, associated, endorsed by, or in any way officially connected with the Open Source Automation Development Lab (OSADL) eG, or any of its subsidiaries or its affiliates. The official OSADL website can be found at https://www.osadl.org.

## Usage

### Using builtin functions

```python
import osadl_matrix

result = osadl_matrix.is_compatible("BSD-3-Clause", "MIT")
# result is either
# True - licenses are compatible
# False - licenses are *NOT* compatible

result = osadl_matrix.get_compatibility("GPL-2.0-only", "MIT")
# result is either
# osadl_matrix.OSADLCompatibility.YES - licenses are compatible
# osadl_matrix.OSADLCompatibility.NO - licenses are *NOT* compatible
# osadl_matrix.OSADLCompatibility.UNKNOWN - license compatibility is uncertain
# osadl_matrix.OSADLCompatibility.CHECKDEP - compatibility has depencies that need to be checked
# osadl_matrix.OSADLCompatibility.UNDEF - at least one of the licenses are not present in the OSADL matrix

result = osadl_matrix.supported_licenses()
# result is a set of supported license (identifiers)
```

### Using the raw data

```python
import csv

import osadl_matrix

with open(osadl_matrix.OSADL_MATRIX) as csvinput:
    creader = csv.reader(csvinput, delimiter=',', quotechar='"')
    for row in creader:
        print(row)
```

or as json

```python
import json

import osadl_matrix

with open(osadl_matrix.OSADL_MATRIX_JSON) as jsoninput:
    cnt = json.read(jsoninput)
    print(cnt)
```
