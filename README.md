# RAID_4_Simulator

#### Table of contents

 - [Explanation](#explanation)
 - [Dependencies](#dependencies)
 - [Project Setup](#project-setup)
 - [Commands](#commands)


## Explanation

The following project consists of a RAID 4 Simulator, where we can manage a RAID 4 System with 3 drives, insert data into the drives, and perform diverse actions over the drives.

The actions we can perform are the following :
1. Insert data into the drives (the data can be inserted as a text string word without spaces)
2. Drop the data from the drives
3. Recover the data from the drives

## Dependencies

No dependencies are needed, just pytho 3.10.6 or latest!

## Project Setup

1. Install python in your computer

2. First clone the repo and cd into the project folder : 
```bash
git clone https://github.com/adriangargom/RAID_4_Simulator.git

cd RAID_4_Simulator
```

3. Run the following command to start the application :
```bash
python main.py
```

4. The application is ready to be used



## Commands
    
    The following list include all the commands available to use in the simulator

    Status Actions
    0. Get the actual mounted Drives in the RAID system
    1. Check the Disk status
    2. Get the actual data from the drives

    Data Add Actions
    3. Add data into the drives as a string

    Destructive Actions
    4. Destroy / Clear the data from a Drive
    5. Restore a faulty Drive

    Others
    6. Commands help
    7. Clear Console
    8. Exit Application

