import time
from datetime import datetime

# Get the current date and time
now = datetime.now()

# Get the seconds since January 1, 1970
seconds = time.time()

# Format the seconds as a string with commas and scientific notation
seconds_formatted = "{:,.4f}".format(seconds) + " or {:.2e}".format(seconds)

# Format the date as "Oct 21 2022"
date_formatted = now.strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {seconds_formatted}")
print(f"{date_formatted}")
print("$>")