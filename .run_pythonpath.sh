#!/bin/bash

# Set the PYTHONPATH to the root directory of the project
export PYTHONPATH=$(dirname $(dirname $(realpath $0)))

# Run the specified Python script with any additional arguments
python "$@"

# chmod +x run_pythonpath.sh