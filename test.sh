#!/bin/bash

cat coordinates.csv | python map.py | python reduce.py


