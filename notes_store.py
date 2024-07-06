import os


class GetNotes:
    def __init__(self, text, current_date_time):
        self.text = text
        self.current_date_time = current_date_time

    def getdata(self):
        with open(
            os.path.join(os.getcwd(), "database_files", "notes_db.txt"), "r"
        ) as db0:
            self.data_lines = db0.readlines()
        with open(
            os.path.join(os.getcwd(), "database_files", "notes_db.txt"), "r"
        ) as db00:
            self.content = db00.read()
        self.storedata()

    def storedata(self):
        self.descision = []
        with open(
            os.path.join(os.getcwd(), "database_files", "notes_db.txt"), "a+"
        ) as db1:
            if self.content.strip() != "":
                if len(self.data_lines) > 0:
                    last_line = self.data_lines[-1].strip()
                    try:
                        last_id = int(last_line.split(">")[0].split(":")[1])
                        self.idd = str(last_id + 1)
                    except ValueError:
                        self.idd = "1"
                else:
                    self.idd = "1"
            else:
                self.idd = "1"

            if len(self.data_lines) != 0:
                for line in self.data_lines:
                    line = line[5:].strip()
                    if line == f"{self.text};{self.current_date_time}":
                        self.descision.append(1)
                    elif line != f"{self.text};{self.current_date_time}":
                        pass
                if len(self.descision) == 0:
                    db1.write(f"ID:{self.idd}>{self.text};{self.current_date_time}\n")
                else:
                    pass
            if len(self.data_lines) == 0:
                db1.write(f"ID:{self.idd}>{self.text};{self.current_date_time}\n")

    def senddata(self):
        with open(
            os.path.join(os.getcwd(), "database_files", "notes_db.txt"), "r"
        ) as db2:
            self.data_lines2 = db2.readlines()
            if len(self.data_lines2) == 0:
                return "database empty"
            else:
                self.data_lines2 = [line.strip() for line in self.data_lines2]
                return self.data_lines2

    def deletedata(self, text, current_date_time):
        self.text = text
        self.current_date_time = current_date_time
        self.victim = f"{self.text};{self.current_date_time}"
        self.the_lines = []

        with open(
            os.path.join(os.getcwd(), "database_files", "notes_db.txt"), "r"
        ) as target:
            self.lista = target.readlines()

        for one in self.lista:
            self.the_lines.append(one[5:].strip())

        self.the_lines = [line for line in self.the_lines if line != self.victim]

        with open(
            os.path.join(os.getcwd(), "database_files", "notes_db.txt"), "w"
        ) as target1:
            target1.write("")

        with open(
            os.path.join(os.getcwd(), "database_files", "notes_db.txt"), "w+"
        ) as target2:
            for num, the_line in enumerate(self.the_lines):
                target2.write(f"ID:{num + 1}>{the_line}\n")


# Example usage:
if __name__ == "__main__":
    # Initialize GetNotes object
    notes_manager = GetNotes("Example note", "2024-07-06 15:30:00")

    # Retrieve data
    notes_manager.getdata()

    # Delete data (example)
    notes_manager.deletedata("Example note", "2024-07-06 15:30:00")

    # Send data (example)
    print(notes_manager.senddata())
