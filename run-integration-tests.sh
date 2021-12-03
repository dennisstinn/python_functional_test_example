#!/bin/bash
# script that will run the tests

usage() {
    echo "Usage: $0 [options]"
            echo "   [-e] Accepts 'stage' or 'prod'"
    echo
}


while getopts e:l option; do
    case "${option}" in
        e  ) export ENV=${OPTARG} ;;
        *  ) usage >&1;
            exit 1 ;;
    esac
done



if [ "$ENV" == "prod" ] || [ "$ENV" == "stage" ]; then
    python3 -m pytest -s ./tests/integration
else
    usage
    exit
fi
