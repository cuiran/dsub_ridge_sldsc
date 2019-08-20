#!/bin/bash

dsub \
    --provider google-v2 \
    --project finucane-dp5 \
    --zones "us-east1-b" \
    --disk-size 100 \
    --logging gs://regularized_sldsc/logging/ridge_sldsc/ \
    --machine-type n1-standard-4 \
    --image "gcr.io/finucane-dp5/ridge-sldsc" \
    --script "run_ridge_sldsc_cts.py" \
    --task "submit_cts.tsv"
