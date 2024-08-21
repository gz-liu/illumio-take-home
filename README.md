# illumio-take-home

# Assumptions
 1. Logs are in .txt format and lookup table is in .csv
 2. Records are structured in a way that all defined columns have a value (including NULL)
 3. Flow logs follow the default version 2 format as documented in AWS and follow the same structure as the examples provided in the email
 4. Input logs and lookup table files are assumed to be mostly validated already, so I'm not doing many quality checks when parsing them. To elaborate, this is also assuming records within both files are standardized, so dstport will always be a number, and all the records in the log file will follow the same structure and positions even though it's a txt file

# Running the Program
No external libraries are used. There are two positional arguments, the first is the path to the sample flow log and the second is the path to the lookup table. There's a sample input log and a sample lookup table under /test/sample_data.

For my Windows machine, running this locally with the sample data looks like: "py .\main.py .\test\sample_data\test_sample_flow_log.txt .\test\sample_data\test_lookup_table.csv"

There's a test case using the sample data with the default unittest module, running that locally looks like: "py -m unittest"

Mostly I just tested the program with the sample data under the test folder for the sake of time. I structured those sample files the same way as the examples shown in the email.

# Improvements
I'm also storing the outputs in memory which shouldn't be an issue for outputs of this size, but something to consider in the future if they ever get too big to store in memory (hopefully not for logs).

Also I'm hardcoding where the dstport and protocol columns are expected to be, it would probably be better to pass some sort of schema or the csv headers alongside with the log to be able to support custom formats and to find those columns based on those details.

I'd like to flesh out logging and exception handling too in the framework, as well as an actual test suite with both positive and negative cases. I have some validations for the input files but they're not extensive. I appended a UUID to the logs for uniqueness, but it might be better to append a more useful identifier like a timestamp.

Everything is being done in native Python, but assuming the flow logs are already coming in cleaned and structured, I would rather put these logs into a relational database table and process them with SQL. Logs tend to be far more readable and easier to parse through a database. SQL also tends to be faster then Python in my experience for basic aggregations and relatively small datasets. Or it could go through a feature-rich logging system like an Elastic ELK stack.

# Future Scalability
The main bottleneck for this is volume, assuming the 10 MB cap for the log still holds. If this were to be productionized, I would like the upstream service to send these logs through a message broker like Kafka or Pub/Sub, and process them in batches/micro-batches depending on the volume of the logs. If it was an API endpoint instead for pushing the logs, it can be rate-limited. I don't think these aggregations need real-time streaming which makes it easier to manage and scale. In any case, we could push this to an proper ETL pipeline if needed for scalability.

I've chosen this project structure for this framework with the intention of keeping it modular and making future maintainability and enhancements easy. It's a similar structure to other frameworks I've seen and contributed in.
