import unittest
from pathlib import Path
from framework.parser.log_parser import LogParser

class TestParseFiles(unittest.TestCase):

    def setUp(self):
        self.log_path = Path("test/sample_data/test_sample_flow_log.txt")
        self.lookup_table = {
            ('25', 'tcp'): 'sv_P1',
            ('68', 'udp'): 'sv_P2',
            ('110', 'tcp'): 'email'
        }

    def test_parse_files(self):
        parser = LogParser(self.log_path, self.lookup_table)
        expected_tag_counts = {'sv_P1': 1, 'untagged': 15, 'email': 1}
        self.assertEqual(parser.tag_counts, expected_tag_counts)

        expected_combination_counts = {('49153', 'tcp'): 3, 
                                       ('49154', 'tcp'): 1, 
                                       ('49155', 'tcp'): 1,
                                       ('49156', 'udp'): 1,
                                       ('49157', 'udp'): 1,
                                       ('49158', 'udp'): 1,
                                       ('80', 'tcp'): 1,
                                       ('1024', 'tcp'): 1,
                                       ('443', 'udp'): 1,
                                       ('23', 'tcp'): 1,
                                       ('25', 'tcp'): 1,
                                       ('110', 'tcp'): 1,
                                       ('993', 'tcp'): 1,
                                       ('143', 'tcp'): 1,
                                       ('0', 'icmp'): 1}
        
        self.assertEqual(parser.combination_counts, expected_combination_counts)