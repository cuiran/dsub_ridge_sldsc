#!/usr/bin/env python

import subprocess
import os

#assign variables
SUMSTAT = os.environ['SUMSTAT']
BASELINE = os.environ['BASELINE']
OUT = os.environ['OUT']
WEIGHT = os.environ['WEIGHT']
ANNOT = os.environ['ANNOT']

#make directories
subprocess.call(['mkdir','/mnt/data/annot/'])
subprocess.call(['mkdir','/mnt/data/baseline/'])
subprocess.call(['mkdir','/mnt/data/weights/'])
subprocess.call(['mkdir','/mnt/data/ss/'])
subprocess.call(['mkdir','/mnt/data/result/'])

#copy data
annot_name = ANNOT.split('/')[-1]
subprocess.call(['gsutil','-m','cp','gs://regularized_sldsc/data/annot_and_ldscore/EUR/Vivian/'+annot_name+'*','/mnt/data/annot/'])
subprocess.call(['gsutil','-m','cp','gs://regularized_sldsc/data/annot_and_ldscore/EUR/baseline/baseline.*','/mnt/data/baseline/'])
subprocess.call(['gsutil','-m','cp','gs://regularized_sldsc/data/annot_and_ldscore/EUR/weights/*.ldscore.gz','/mnt/data/weights/'])
ss_name = SUMSTAT.split('/')[-1]
subprocess.call(['gsutil','-m','cp','gs://regularized_sldsc/data/sumstats/EUR/'+ss_name,'/mnt/data/ss/'])

#run script
subprocess.call(['python','/home/ldscore/ldsc.py',
    '--h2',SUMSTAT,
    '--ref-ld-chr',BASELINE+','+ANNOT,
    '--out',OUT,
    '--ridge',
    '--w-ld-chr',WEIGHT])

subprocess.call(['gsutil','-m','cp','/mnt/data/result/*','gs://regularized_sldsc/results/ridge_sldsc/Vivian_annots_1000GEUR_cts/'])
