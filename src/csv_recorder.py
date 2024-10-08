import csv


class CSVRecorder:

    def __init__(self, file_path, header):
        csv_file = open(file_path, "w+", newline="")
        self.logger = csv.writer(csv_file, dialect="excel")

        self.log_to_csv("frame", header)

    def log_to_csv(self, t, data):

        row = [t]
        row.extend(data)
        self.logger.writerow(row)
