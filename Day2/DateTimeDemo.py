from datetime import datetime as dt

ts = dt.now()
dob = dt(1987,12,9,17,16,16)
days = (ts - dob).days

print divmod(days, 365.25)