#!/bin/bash

for var in {1..223}
do
  python run.py --model bsds500 --in ./leonardovinci/targets/$var.jpg --out ./leonardovinci_edges/$var.png
done
