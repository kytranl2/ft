import datetime


def read_last_data(filename):
    """Read the last recorded data from the file."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    if lines:
        last_date = lines[-2].strip().split(": ")[-1]
        last_data = eval(lines[-1].strip().split(": ")[-1])
        return last_date, last_data
    return None, None
    
def write_data(filename, date, data):
    """Write data to the file."""
    with open(filename, 'a') as file:
        file.write(f"Date: {date}\n")
        file.write(f"Data: {data}\n")
stockDict = {'AAPL': '2950521683968', 'TSLA': '742563905536'}
filename = 'market_cap_data.txt'
last_date, last_market_cap = read_last_data(filename)

if last_market_cap:
    differences = {company: int(stockDict.get(company, 0)) - last_market_cap for company in stockDict}
    print(f"Differences from {last_date}: {differences}")

# Write current data to file with date
current_date = datetime.datetime.now().strftime("%Y-%m-%d")
write_data(filename, current_date, stockDict)
