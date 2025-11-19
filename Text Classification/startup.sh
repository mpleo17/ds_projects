#!/bin/bash
conda create --yes --name midas_env python=3.12 pip
conda activate midas_env

pip install -r requirements.txt

conda deactivate
conda env remove --all --yes --name midas_env