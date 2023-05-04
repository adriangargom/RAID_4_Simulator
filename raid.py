import drive as dv

class Raid:

    drives = None
    parity_drive = 2
    
    #----------------
    #**Constructor **
    def __init__(self):
        self.drives = []
        for x in range(3):
            self.drives.append(dv.Drive())


    #----------------------------------------------------
    #** Trasform data into Binary and calculate Parity **

    def add_data(self, data):
        bin_data = list(' '.join(format(c, "b") for c in bytearray(data, "utf-8")))
        bin_data.append(' ')

        print(bin_data)

        for i in range(len(bin_data) // 2):
            for x in range(2):
                self.drives[x].insert(True if bin_data[0] == "1" else False)
                bin_data = bin_data[1:]

        self.calc_parity()

    def calc_parity(self):
        for x in range(self.drives[0].get_size()):
            res = bool(self.drives[0].get_data_at_id(x)) ^ bool(self.drives[1].get_data_at_id(x))
            self.drives[self.parity_drive].insert(res)
            

    #----------------------------------------------------------
    #** Destructive and Restoring Actions to the RAID System **

    def restore_disk(self, faulty_disk_id, rec_disk_id = 0):

        if faulty_disk_id == self.parity_drive:
            self.calc_parity()
        else:
            for x in range(self.drives[self.parity_drive].get_size()):
                res = self.drives[rec_disk_id].get_data_at_id(x) ^ self.drives[self.parity_drive].get_data_at_id(x)
                self.drives[faulty_disk_id].insert(res)

        self.drives[faulty_disk_id].status = True

    def destroy_disk(self, disk_id):
        self.drives[disk_id].destroy_disk()


    #-----------------------------------
    #** Get Data from the RAID System **

    def check_disk_status(self):
        print("---------------------------------")
        for x in range(len(self.drives)):
            print(f"Drive {x} status => {self.drives[x].status}")

    def get_drives_data(self):

        data_bit_array = ""

        for x in range(self.drives[0].get_size()):
            data_bit_array += ('1' if self.drives[0].get_data_at_id(x) == True else '0')
            try:
                data_bit_array += ('1' if self.drives[1].get_data_at_id(x) == True else '0')
            except:
                data_bit_array = ""
                break

        result = ""

        while len(data_bit_array) != 0:
            result += chr(int(str(data_bit_array[0:7]),2))
            data_bit_array = data_bit_array[8:]
       
        return result

    def get_drives(self):
        print("---------------------------------")
        for x in range(len(self.drives)-1):
            print(f"Drive {x} => ", self.drives[x].arr)

        print(f"Parity drive => ", self.drives[2].arr)