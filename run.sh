#!/bin/bash

# This script is used to start hypercorn.
# Hypercorn is running on port 8000 by default.

hypercorn api.main:app --bind 0.0.0.0:8000 --reload