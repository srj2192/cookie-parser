import csv
import argparse
from datetime import datetime


class CookieParser:

    def __init__(self, log_dir, file, date):
        self.log_file_directory = log_dir
        self.log_file = file
        self.cookie_date = date

    def get_cookie_by_date(self):
        cookies = {}
        with open('{directory}/{file}'.format(directory=self.log_file_directory, file=self.log_file)) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                cookie_datetime = datetime.strptime(row['timestamp'], "%Y-%m-%dT%H:%M:%S%z")
                if str(cookie_datetime.date()) == self.cookie_date:
                    cookies[row['cookie']] = cookies[row['cookie']] + 1 if row['cookie'] in cookies else 1

        return [key for key, value in cookies.items() if value == max(cookies.values())]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', type=str, required=True)
    parser.add_argument('--date', '-d', type=str, required=True)
    args = parser.parse_args()
    log_file_dir = 'log'
    cookie_parser = CookieParser(log_file_dir, args.file, args.date)
    print("\n".join(cookie_parser.get_cookie_by_date()))
