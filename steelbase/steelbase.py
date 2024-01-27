import pickle

class SteelBase:
    def __init__(self, filename="steelbase.steelbase"):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError):
            return {}

    def save_data(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self.data, file, protocol=pickle.HIGHEST_PROTOCOL)

    def create_table(self, table_name):
        if table_name not in self.data:
            self.data[table_name] = {}

    def add_record(self, table_name, record_id, record_data):
        if table_name in self.data:
            self.data[table_name][record_id] = record_data
        else:
            print(f"Table '{table_name}' does not exist.")

    def get_record(self, table_name, record_id):
        if table_name in self.data and record_id in self.data[table_name]:
            return self.data[table_name][record_id]
        else:
            print(f"Record '{record_id}' not found in table '{table_name}'.")

    def show_tables(self):
        return list(self.data.keys())

    def show_records(self, table_name):
        if table_name in self.data:
            return list(self.data[table_name].items())
        else:
            print(f"Table '{table_name}' does not exist.")