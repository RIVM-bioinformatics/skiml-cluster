FROM condaforge/mambaforge

LABEL dockerfile.version="1"
LABEL software="skiml-cluster"

COPY environment.yml .
RUN /bin/bash -c "mamba env update -n base -f environment.yml"

RUN mkdir /variants && touch /variants/sampleA.vcf && touch /variants/sampleB.vcf && skiml-cluster run --input /variants --output /variants_output --conda-create-envs-only && rm -rf /variants
