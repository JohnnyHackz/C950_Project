# Student:Jakob Berentsen
# Student ID: 001068769
# Title: WGUPS ROUTING PROGRAM - C950

import csv
import datetime
import Truck
from builtins import ValueError

from Hashtable import HashMap
from Packages import Packages

# The following will read the file named DistanceData.
with open("DistanceData.csv") as csvfile:
    DistanceData_CSV = csv.reader(csvfile)
    DistanceData_CSV = list(DistanceData_CSV)

# The following will read the file named AddressName_data.
with open("AddressName_data.csv") as csvfile1:
    AddressData_CSV = csv.reader(csvfile1)
    AddressData_CSV = list(AddressData_CSV)

# The following will read the file named Package_file.
with open("Package_file.csv") as csvfile2:
    PackageFile_CSV = csv.reader(csvfile2)
    PackageFile_CSV = list(PackageFile_CSV)


# The following method will create/load package objects from the Package CVS file into the hash table named 'hashTable_packages'.
def loadPackageInfo(filename, hashTable_packages):
    with open(filename) as pck_Info:
        pck_Data = csv.reader(pck_Info)
        for package in pck_Data:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZipcode = package[4]
            pDeadline_time = package[5]
            pWeight = package[6]
            pStatus = "At Hub"

            # This is the package object represented using 'p'.
            p = Packages(pID, pAddress, pCity, pState, pZipcode, pDeadline_time, pWeight, pStatus)

            # This will insert data into the hash table named 'hashTable_packages'.
            hashTable_packages.insert(pID, p)


# The following method will access the DistanceData_CSV file and find distances between two addresses(x, y).
def distance_between_values(x_value, y_value):
    distance = DistanceData_CSV[x_value][y_value]
    if distance == '':
        distance = DistanceData_CSV[y_value][x_value]

    return float(distance)


# The following method will retrieve the address number from the string literal address.
def address_extraction(address):
    for row in AddressData_CSV:
        if address in row[2]:
            return int(row[0])


# The following will create the truck object named 'first_truck'.
first_truck = Truck.Truck(16, 18, None, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East",
                       datetime.timedelta(hours=8))

# The following will create the truck object named 'second_truck'.
second_truck = Truck.Truck(16, 18, None, [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

# The following will create the truck object named 'third_truck'.
third_truck = Truck.Truck(16, 18, None, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=9, minutes=5))

# The following will create the hash table named 'hashTable_packages'.
hashTable_packages = HashMap()

# The following will load the packages into the hash table named 'hashTable_packages'.
loadPackageInfo("Package_file.csv", hashTable_packages)

# The following method will sort packages within a specific truck using the nearest neighbor algorithm.
# Additionally, this method will calculate the distance that the specific truck drives after packages have been sorted.
def delivery_of_packages(trucks):
    # The following will place all packages into an 'undelived' array.
    undelivered = []
    for packageID in trucks.truck_packages:
        package = hashTable_packages.lookup(packageID)
        undelivered.append(package)
    # The following will clear the package list for a specific truck so that the packages will be resorted back into the truck in an order based on the nearest neighbor.
    trucks.truck_packages.clear()

    # The following will loop through the 'undelivered list' until there are no remaining items in the list.
    # The following will individually add the nearest package to the truck.truck_packages list.
    while len(undelivered) > 0:
        next_address = 2000
        next_package = None
        for package in undelivered:
            if distance_between_values(address_extraction(trucks.truck_address), address_extraction(package.package_address)) <= next_address:
                next_address = distance_between_values(address_extraction(trucks.truck_address), address_extraction(package.package_address))
                next_package = package
        # The following will add the next nearest package to the truck_packages list.
        trucks.truck_packages.append(next_package.package_ID)
        # The following will then remove the above noted package from the 'undelivered' list.
        undelivered.remove(next_package)
        # The following will place the distance in miles driven to the package into the truck_mileage attribute.
        trucks.truck_mileage += next_address
        # The following will update the current address attribute of the truck to the package that it drove to.
        trucks.truck_address = next_package.package_address
        # The following will update the amount of time taken for the truck to drive to the nearest package.
        trucks.time += datetime.timedelta(hours=next_address / 18)
        next_package.delivery_time = trucks.time
        next_package.departure_time = trucks.depart_time


# The following will account for the process of loading the trucks.
delivery_of_packages(first_truck)
delivery_of_packages(second_truck)
#The following will prevent the third truck from leaving until both the first and second trucks have finished delivering their packages.
third_truck.depart_time = min(first_truck.time, second_truck.time)
delivery_of_packages(third_truck)


class Main:
   # User Interface
   # The following message will appear when the program is iniciated.
   print("Welcome to Western Governors University Parcel Service")
   print("The total route mileage is: ", first_truck.truck_mileage + second_truck.truck_mileage + third_truck.truck_mileage)

   # The user will be prompted to enter the word 'status' in order to start the program.
   response = input("If you would like to check the status of your package, please type 'status': ")
   if response == "status":
       inquiry_time = input("Please enter a time to check status of package(s) in the format HH:MM:SS ")
       (h, m, s) = inquiry_time.split(":")
       convert_timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=(int(s)))
       second_response = input("To check the status of a single package, enter 'single'. To check all packages, enter 'all': ")
       # The user will be asked if they want to see the status of a single package or of all packages
       if second_response == "single":
           try:
               single_input = input("Enter the package ID(1-40): ")
               package = hashTable_packages.lookup(int(single_input))
               package.update_status(convert_timedelta)
               print(str(package))
           except ValueError:
               print("Invalid response. Please try again.")
               exit()
       elif second_response == "all":
           try:
               for packageID in range(1, 41):
                   package = hashTable_packages.lookup(packageID)
                   package.update_status(convert_timedelta)
                   print(str(package))
           except ValueError:
               print("Invalid response. Please try again.")
               exit()
       else:
           exit()
   else:
       print("Invalid response. Please try again.")
       exit()
