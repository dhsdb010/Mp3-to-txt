from datetime import datetime

def get_time():
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d")
    return formatted_date
print(get_time())