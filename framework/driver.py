'''
Framework base driver
'''

import logging
from framework.parser.log_parser import LogParser
from framework.writer.writer import Writer
from framework.models.lookup_table import LookupTable

class Driver:
    
    def __init__(self, log_path, lookup_table_path):
        self.log_path = log_path
        self.lookup_table_path = lookup_table_path
        self.lookup_table = LookupTable(self.lookup_table_path)

    def run(self):
        logging.info('Processing flow log in path...')
        output = LogParser(self.log_path, self.lookup_table.table)
        Writer(output.tag_counts, output.combination_counts).write()
        logging.info('Process finished')