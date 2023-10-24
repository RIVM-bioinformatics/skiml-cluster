# SPDX-FileCopyrightText: 2023-present boasvdp <ids-bioinformatics@rivm.nl>
#
# SPDX-License-Identifier: MIT
from pathlib import Path

from snk.cli import CLI

pipeline_name = CLI(pipeline_dir_path=Path(__file__).parent.parent)
