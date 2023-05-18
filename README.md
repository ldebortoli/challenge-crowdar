# challenge-crowdar

Runs in Linux. Not tested on Windows / Mac but maybe works in those OS.

# Install

1. Clone the repository locally
2. Install Google Chrome and Firefox
3. Install python
4. Install pip (https://pip.pypa.io/en/stable/installation/)
5. Install pipenv: $ pip install pipenv
6. Install packages: $ pipenv install
7. Set up environment variables:
    
    Linux:

    export SAUCEDEMO_STANDARD_USERNAME=
    
    export SAUCEDEMO_STANDARD_PASSWORD=

    export SAUCEDEMO_LOCKED_USERNAME=
    
    export SAUCEDEMO_LOCKED_PASSWORD=

    export SAUCEDEMO_PROBLEM_USERNAME=
    
    export SAUCEDEMO_PROBLEM_PASSWORD=

    export SAUCEDEMO_PERFORMANCE_USERNAME=
    
    export SAUCEDEMO_PERFORMANCE_PASSWORD=
  
After the "=" place the corresponding value according to those that appear on the page (https://www.saucedemo.com/).

In windows or mac, place the variables with their corresponding values following the same names that are used here.

On Linux, if you add the variables in the ~/.bashrc file, don't forget to run the command

    $ source ~/.bashrc

before continuing.


# Run

To run the ui tests in chrome and firefox and the api testing write the following command that will run a bash script that is responsible for performing three different test runs, one for each browser and another one for the api testing:

    $ bash run.sh -b "chrome firefox" --apitesting

For each browser (and for the api), all the test cases will be executed in parallel using as maximum concurrency value the number of logical cores available by the CPU (internally the script adds "-n logical" to the command that runs pytest so that it takes care of it automatically of calculating it on the PC it's on, this can be higher than the number of physical cores which increases efficiency)


To run the default version with chrome only write the following command:

    $ pipenv run python -m pytest -m ui --html=reports/report-browser.html --self-contained-html

To run the default version for api testing write the following command:

    $ pipenv run python -m pytest -m api --html=reports/report-api.html --self-contained-html


# Reports and Screenshots

The html reports will be generated in the reports folder, and will include screenshots that are saved inside the screenshot folder.
