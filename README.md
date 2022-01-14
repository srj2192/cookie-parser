# Cookie Parser
Application to retrieve most active cookie from log file

## Project setup steps
- `make build` will install dependencies and run the unit tests
- `make setup` to simply install the dependencies
- `make test` to run the unit test

## Running Instructions

- `main.py` is the entrypoint for the parser
- execute command `python main.py -f cookie_log.csv -d 2018-12-09` with arguments -f or --file for log filename and
  -d or --date for date
- log files are served from `log` directory please ensure the file you're providing exists in log directory and 
  please include it if not. 


#### Note: Install Python 3 on your local machine before running make command