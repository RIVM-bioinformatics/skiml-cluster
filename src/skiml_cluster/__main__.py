# SPDX-FileCopyrightText: 2023-present boasvdp <ids-bioinformatics@rivm.nl>
#
# SPDX-License-Identifier: MIT
import sys

if __name__ == "__main__":
    from skiml_cluster.cli import skiml_cluster

    sys.exit(skiml_cluster())
