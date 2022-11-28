# people.py 

from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

PEOPLE = {
    "K-Pop": {
        "fname": "Jisoo",
        "lname": "Kim",
        "timestamp": get_timestamp(),
    },
    "Latin": {
        "fname": "Bad",
        "lname": "Bunny",
        "timestamp": get_timestamp(),
    },
    "Psy": {
        "fname": "Henrique",
        "lname": "Camacho",
        "timestamp": get_timestamp(),
    }
}

def read_all():
    return(list(PEOPLE.values()))
