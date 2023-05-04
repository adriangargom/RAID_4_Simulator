
class Drive:

    arr = None
    status = None

    def __init__(self):
        self.arr = []
        self.status = True

    def insert(self, data):
        self.arr.append(data)

    def get_size(self):
        return len(self.arr)

    def get_data_at_id(self, id):
        return self.arr[id]

    def destroy_disk(self):
        self.arr.clear()
        self.status = False
