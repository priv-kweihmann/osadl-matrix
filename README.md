# osadl-matrix

This is a CSV version of the [OSADL license compatibility matrix](https://www.osadl.org/fileadmin/checklists/matrix.html) as a python library.

## License

This module is licensed under [Unlicensed](LICENSE.Unlicensed) license. Feel free to do whatever you want with it.
The data is licensed under [CC-BY-4.0](LICENSE.ccby40)

## Usage

### Using builtin functions

```python
import osadl_matrix

result = osadl_matrix.is_compatible("BSD-3-Clause", "MIT")
# result is either
# osadl_matrix.OSADLCompatibility.YES - licenses are compatible
# osadl_matrix.OSADLCompatibility.NO - licenses are *NOT* compatible
# osadl_matrix.OSADLCompatibility.UNDEF - no data available on compatibility
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
