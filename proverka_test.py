from datetime import datetime, timezone


scheduled_time = datetime.now(timezone.utc)
scheduled = datetime.now()

print(scheduled_time)
print(scheduled)