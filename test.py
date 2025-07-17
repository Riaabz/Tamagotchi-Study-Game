import time
from datetime import datetime, timedelta
print(datetime.now())

input("Press Enter to start a study session")
start = time.time()
input("Press Enter to end the study session")
end = time.time()
duration = (end - start) / 60
print(f"You studied for {int(duration)} minutes.")

print(datetime.now() - timedelta(days=1))
