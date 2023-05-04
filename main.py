import raid as rd

raid_sys = rd.Raid()
running = True
commands = open("commands.txt", "r")
commands_data = commands.read()

while running:

    selected_option = input("\nOption > ")

    match int(selected_option):
        case 0:
            raid_sys.get_drives()

        case 1:
            raid_sys.check_disk_status()

        case 2:
            print("\n---------------------------------")
            print(f"Actual Stored data in the drives => {raid_sys.get_drives_data()}")

        case 3:
            raid_sys.add_data(input("Data to Insert > "))

        case 4:
            raid_sys.destroy_disk(int(input("ID of the drive to destroy > ")))
        
        case 5:
            raid_sys.restore_disk(int(input("Faulty Drive ID > ")), int(input("Recover Drive > ")))

        case 6:
            print(commands_data)

        case 7:
            print("\033[H\033[J", end="")

        case 8:
            print("Bye ;D")
            running = False

    print("\n---------------------------------")

