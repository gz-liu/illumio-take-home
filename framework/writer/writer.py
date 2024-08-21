import uuid
import logging

class Writer:
    
    def __init__(self, tag_counts, combination_counts):
        self.tag_counts = tag_counts
        self.combination_counts = combination_counts
        self.output_file = f"output_{uuid.uuid4()}.txt"

    def write(self):
        logging.info(f'Writing results to output file: {self.output_file}')
        with open(self.output_file, 'w') as file:
            file.write('Tag Counts:\n')
            file.write('Tag, Count\n')
            for tag, count in self.tag_counts.items():
                file.write(f'{tag}, {count}\n')

            file.write('\n\n')

            file.write('Port/Protocol Combination Counts:\n')
            file.write('Port, Protocl, Count\n')
            for (port, protocol), count in self.combination_counts.items():
                file.write(f'{port}, {protocol}, {count}\n')

            file.close() 