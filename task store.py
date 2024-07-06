import os


class GetData:
    def __init__(self, task, description, hour_min, day_month_yr, priority):
        self.task = task
        self.description = description
        self.hour_min = hour_min
        self.day_month_yr = day_month_yr
        self.priority = priority

    def send_data(self):
        try:
            with open(os.path.join(os.getcwd(), "database_files", "tasks_db.txt"), "r") as file:
                lines = file.readlines()
                return lines if lines else "database empty"
        except FileNotFoundError:
            return "database empty"

    def delete_data(self, task, description, time, date, priority):
        lines = self.send_data()
        with open(os.path.join(os.getcwd(), "database_files", "tasks_db.txt"), "w") as file:
            for line in lines:
                if not line.strip("\n").endswith(f";{task};{description};{time};{date};{priority}"):
                    file.write(line)
