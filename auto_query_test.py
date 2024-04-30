import logging
import sys
from queries import Query
from scenarios import query_and_preserve

# Check if the URL is provided as an argument
if len(sys.argv) < 2:
    # logging.fatal('No URL provided. Usage: python3 auto_query_test.py http://10.10.10.201:31966')
    # logging.fatal('No URL provided. Usage: python3 auto_query_test.py http://10.107.91.15:30729')
    logging.fatal('No URL provided. Usage: python3 auto_query_test.py http://10.10.10.201:32075')
    sys.exit(1)  # Exit the script with an error code

# First command line argument is the URL
url = sys.argv[1]

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Log in to the train-ticket system and store the cookies
q = Query(url)
if not q.login():
    logging.fatal('Login failed')
    sys.exit(1)  # Exit the script with an error code

# Execute scenario on current user
query_and_preserve(q)

# Or execute query directly
q.query_high_speed_ticket()