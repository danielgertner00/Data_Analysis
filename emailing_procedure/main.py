import time
from datetime import datetime

import save_system

participants = save_system.load()

target_time = datetime.now().replace(hour=11, minute=37)

while datetime.now() < target_time:
    remaining = target_time - datetime.now()
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f'\rTime remaining: {hours:02d}:{minutes:02d}:{seconds:02d}', end='', flush=True)
    time.sleep(1)

print()
for part in participants:
    part.send_email()
    # print(part)


save_system.save(participants)
