#!/bin/bash
# Only status code
curl --write-out '%{response_code}' --head --silent --output /dev/null "$1"
