# skiml-cluster

[![PyPI - Version](https://img.shields.io/pypi/v/skiml-cluster.svg)](https://pypi.org/project/skiml-cluster)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/skiml-cluster.svg)](https://pypi.org/project/skiml-cluster)

-----

**Table of Contents**

- [Quickstart](#quickstart)
- [Installation](#installation)
- [License](#license)

## Quickstart

For RIVM users, the best approach is to run `skiml-cluster` on a computing node of the HPC, instead of on the home node.

Step by step:

1. Run apollo-mapping on the samples you want to cluster, or find the apollo-mapping results of these samples.
2. Copy all **SNP** VCFs (`<APOLLO-MAPPING-OUTPUT>/variants/snps/*.vcf`) for the relevant samples to a single directory.
3. Run skiml-cluster as follows on the SNP VCF directory, which will submit a job to the HPC: 
```console
bsub -M 10G skiml-cluster run --input <INPUT FOLDER> --output <OUTPUT FOLDER>
```


It is also possible to run `skiml-cluster` locally (without submitting to the HPC):
```console
skiml-cluster run --input <INPUT FOLDER> --output <OUTPUT FOLDER>
```
However, please do this with care as some steps might require a lot of resources if you're running a lot of samples.


## Installation

### Container (e.g. using Singularity)

A container is available for skiml-cluster. Read more about containers here: https://docs.sylabs.io/guides/latest/user-guide/.

```console
singularity pull "docker://ghcr.io/rivm-bioinformatics/skiml-cluster:0.0.3"
```

When running the container, make sure you are binding paths, because the container otherwise doesn't have access to your file system:

```console
singularity exec --bind /home/user/project1:/home/user/project1 skiml-cluster_0.0.3.sif skiml-cluster run --input /home/user/project1/input_data --output /home/user/project1/output_data
```

### PyPI

```console
pip install --user skiml-cluster
```

To update `skiml-cluster` to the most recent version, run:
```console
pip install --user --upgrade skiml-cluster
```

## Troubleshooting

Q: I get this error:
```
ValueError in file /home/boas/mambaforge/lib/python3.10/site-packages/skiml_cluster/workflow/Snakefile, line 16:
No VCF files found in input directory.
```
A: `skiml-cluster` looks for files ending in `.vcf` in the input folder. If zero files can be found with this **exact** extension, the pipeline will not run. Please make sure there are valid VCF files (preferably from `apollo-mapping`) in the input folder with the extension `.vcf`.

Q: I get this error:
```
ValueError in file /home/boas/mambaforge/lib/python3.10/site-packages/skiml_cluster/workflow/Snakefile, line 11:
Input directory does not exist.
```
A: The input directory cannot be found. Please make sure there are no typos in the `skiml-cluster` command.

## Methodology

`skiml-cluster` does a couple of things, which is managed by Snakemake.

1. SNP VCF files are compressed and indexed (required for other analyses).
2. All indexed VCF files are merged into a multi-sample VCF.
3. A UPGMA tree is generated from the multi-sample VCF using `vcfkit`.
4. A Fasta pseudo-alignment is generated from the multi-sample VCF using `vcfkit`.
5. SNP distances are calculated from the pseudo-alignment using `snp-dists`.

A command line interface of the Snakemake pipeline has been generated using [`snk`](https://snk.wytamma.com/).

## License

`skiml-cluster` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
