import random
import string
import datetime

def generate_name():
    first = ["Alice", "Bob", "Charlie", "Diana"]
    last = ["Smith", "Johnson", "Lee", "Nguyen"]
    return f"{random.choice(first)} {random.choice(last)}"

def generate_email():
    domains = ["test.com", "mail.org", "demo.net"]
    user = ''.join(random.choices(string.ascii_lowercase, k=8))
    return f"{user}@{random.choice(domains)}"

def generate_date():
    start = datetime.date(2020, 1, 1)
    end = datetime.date.today()
    delta = (end - start).days
    return str(start + datetime.timedelta(days=random.randint(0, delta)))

def generate_boolean():
    return random.choice([True, False])

# maps schema field types to generator functions
FIELD_MAP = {
    "name": generate_name,
    "email": generate_email,
    "date": generate_date,
    "boolean": generate_boolean
}
