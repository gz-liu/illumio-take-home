import argparse
import logging
import os
from framework.driver import Driver

logging.basicConfig(format="%(levelname)s | %(asctime)s | %(message)s", level="INFO")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("log_path", help="The input path to the flow log")
    parser.add_argument("lookup_table_path", help="The input path to the lookup table")
    args = parser.parse_args()

    log_path = args.log_path
    lookup_table_path = args.lookup_table_path

    logging.debug(f'Log path: {log_path}')
    logging.debug(f'Lookup table path path: {lookup_table_path}')

    if not os.path.exists(log_path):
        raise TypeError("Log path not found or doesn't exist")
    elif os.path.getsize(log_path) == 0:
        raise ValueError("Provided log file is empty")
    if not os.path.exists(lookup_table_path):
        raise TypeError("Lookup table path not found or doesn't exist")
    elif os.path.getsize(lookup_table_path) == 0:
        raise ValueError("Provided lookup table file is empty")
    
    Driver(log_path, lookup_table_path).run()