class LogParser:

    def __init__(self, log_path, lookup_table):
        self.log_path = log_path
        self.lookup_table = lookup_table
        self.tag_counts = {}
        self.combination_counts = {}
        self.parse_files()

    def parse_files(self):
        try:
            with open(self.log_path, "r") as log:
                for line in log:
                    record = line.split(' ')

                    # hardcoding the columns where dstport and protocol should be in the log
                    dstport = record[6]
                    protocol = record[7].lower()
                    self.aggregate(dstport, protocol)
                log.close()
        except:
            raise Exception("ERROR: Unable to parse log files")
        
    def aggregate(self, dstport, protocol):
        self.aggregate_tag_counts(dstport, protocol)
        self.aggregate_combination_counts(dstport, protocol)
        
    def aggregate_tag_counts(self, dstport, protocol):
        if (dstport, protocol) in self.lookup_table:
            tag = self.lookup_table[(dstport, protocol)]

            if tag not in self.tag_counts:
                self.tag_counts[tag] = 1
            else:
                self.tag_counts[tag] += 1
        else:
            if 'untagged' not in self.tag_counts:
                self.tag_counts['untagged'] = 1
            else:
                self.tag_counts['untagged'] += 1
    
    def aggregate_combination_counts(self, dstport, protocol):
        if (dstport, protocol) not in self.combination_counts:
            self.combination_counts[(dstport, protocol)] = 1
        else:
            self.combination_counts[(dstport, protocol)] += 1
    