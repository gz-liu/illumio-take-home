import logging

class LookupTable:

    def __init__(self, lookup_table_path):
        self.lookup_table_path = lookup_table_path
        self.table = {}
        self.load_table()

    def load_table(self):
        try:
            logging.info("Parsing lookup table...")
            with open(self.lookup_table_path, 'r') as file:
                next(file)  # skip headers

                for line in file:
                    record = line.strip().split(',')
                    dstport, protocol, tag = record[0], record[1], record[2]
                    self.table[(dstport, protocol)] = tag
                file.close()
        except:
            raise Exception(f"ERROR: Unable to parse lookup table from {self.lookup_table_path}")