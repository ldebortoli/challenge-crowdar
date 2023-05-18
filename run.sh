#!/bin/bash

browsers="default";
headless="false";
apitesting="false"

# Get command line params
while getopts e:b:c:m:-: flag
do 
    case "${flag}" in
        -)
            case "${OPTARG}" in
                apitesting) apitesting="true";;
            esac;;

        b) browsers=${OPTARG};;
    esac
done

# Print params
echo -e "\n\n------ INPUTS ------\n";
echo "Browsers: ${browsers}";
echo "APItesting: ${apitesting}";

# Get OS
OS="$(uname -s)";
if [[ "$OS" == "Darwin" ]]; then OS="MAC"; fi

# Run the automation code for specific browser
for browser in $browsers; do

    # Run the tests with the params
    echo -e "\n\n------ START TESGING ON ${OS} USGING ${browser} BROWSER ------\n\n" | tr a-z A-Z;
    pipenv run python3 -m pytest -n logical -m ui --html=reports/report-${browser}.html --self-contained-html --browser=${browser}
    echo -e "\n\n------ TESTING ON ${OS} USING ${browser} BROWSER FINISHED ------" | tr a-z A-Z;

done

if [[ "$apitesting" == "true" ]]
then
    echo -e "\n\n------ START API TESGING ------\n\n"
    pipenv run python3 -m pytest -n logical -m api --html=reports/report-api.html --self-contained-html
    echo -e "\n\n------ API TESGING FINISHED ------\n\n"
fi

echo -e "\n\nAll tests finished\n";


