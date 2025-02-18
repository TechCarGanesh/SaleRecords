# Name: Ganesh Kumar
# Date: 02/17/2025
# Instructor: Professor Andres Calle
# Course: CIST-005B-34571 Advanced Python
# Project Information:
# Imagine you work for a retail company that needs to process sales records. Each record contains:
#
# A unique sale ID.
# A sale date.
# The amount of the sale.
# The product name sold.
# Your program will offer the options to:
#
# Load in sales data (reading from a CSV or database).
# Retrieve the latest sale
# Compute the total revenue
# Check for duplicate sale IDs
# Search for a sale by its ID
# You will measure the performance of these operations and compare them against their theoretical Big O time complexity.
import re
import csv
import random
import time
import matplotlib.pyplot as plt

products = ["Pizza", "Popcorn", "Sandwich", "Spaghetti", "Chicken Nuggets", "Fries",
            "Salad", "Cookie", "Breadsticks", "Soda", "Water"]
prices = [150.00, 200.50, 99.99, 250.75, 49.45, 25.99, 69.99, 134.99, 20.55, 30.60, 110.99]
class genSalesRecords:
    # Instance variables
    _date = ""
    _amount = 0.0
    _productName = ""
    _numRecords = 0
    MAX_RECORDS = 10
    _salesRecords = {}
    start_time = []
    end_time = []

    # This is a default constructor, which initializes everything.
    def __init__(self):
        self._date = ""
        self._amount = 0.0
        self._productName = ""
        self._numRecords = self.MAX_RECORDS
        self._salesRecords = {}

    # This is the constructor to constructor a given number of records.
    def __init__(self, nRecords):
        self._numRecords = nRecords
        self._date = ""
        self._amount = 0.0
        self._productName = ""
        self._salesRecords = {}

    # The generateRecords method generates the random sales records
    # and writes them in the SalesRecords.csv file.
    def generateRecords(self):
        index = 0
        try:
            with open("SalesRecords.csv", 'w') as recfile:
                recfile.write("sale_id,sale_date,amount,product\n")

                # The for loop executes n times each time writing one record to the file.
                # The time complexity is O(n) where n is the number of records.
                for index in range(0, self._numRecords):
                    saleID = random.randint(0, self._numRecords)
                    saleItem = random.randint(0, len(products) - 1)
                    year = random.randint(2020, 2025)
                    month = random.randint(1, 12)
                    day = random.randint(1, 31)
                    recfile.write(f"{saleID},{year}-{month}-{day}, "
                                  f"{prices[saleItem]},{products[saleItem]}" + "\n")
        except IOError:
            print("Exception: Error openingd file.")
        else:
            recfile.close()
        finally:
            print("Created records. Closed the file...")

    # loadSalesData method reads the file from the SalesRecords.csv file
    # and creates a dictionary.
    def loadSalesData(self):
        # index = 0
        print("Loading sales data...")
        try:
            with open("SalesRecords.csv", 'r') as infile:
                # Read first title line and discard it
                infile.readline()
                # Read all the entries until the end of the file.
                while True:
                    # Read one line at a time and store it in the item.
                    # This program executes num_record times. The time complexity is O(n).
                    item = infile.readline()

                    # If it reaches the end of the file, then quit.
                    if not item:
                        break

                    # Splitting the items using the commas and storing it in a list.
                    split_items = item.strip().split(',')

                    # Extract the sales record into id_num, date, price, and product_name.
                    id_num = int(split_items[0])
                    date = split_items[1]
                    price = float(split_items[2])
                    product_name = str(split_items[3])
                    # Create a dictionary entry for salesRecords.
                    self._salesRecords[id_num] = [date, price, product_name]

                    # index += 1
                # print("Sales records:", self._salesRecords)
        except IOError:
            print("Error opening file.")
        else:
            infile.close()
        finally:
            print("File closed...")

    # latestSale method searches the latest sale items in the dictionary.
    def latestSale(self):
        latest_month = -1
        latest_day = -1
        latest_year = -1
        # The for loop gets executed numRecords times looking in the dictionary
        # for the latest sale item. The time complexity is O(n).
        for items in self._salesRecords.values():
            split_items = items[0].strip().split('-')
            year = int(split_items[0])
            month = int(split_items[1])
            day = int(split_items[2])
            # If year is greater than the latest_year, store the new latest year.
            if year > latest_year:
                # If month is greater than the latest_month, store the new latest month.
                if month > latest_month:
                    # If day is greater than the latest_day, store the new latest day.
                    if day > latest_day:
                        # If latest year is not equal to -1, store the first entry
                        # and make it the latest year.
                        if latest_year != -1:
                            latest_year = year
                            latest_month = month
                            latest_day = day
                            print("Latest sale items", items)
                        else:
                            latest_year = year
                            latest_month = month
                            latest_day = day

    # totalRevenue method calculates the total revenue of all the sales items.
    def totalRevenue(self):
        total_revenue = 0.0
        # Loop through the dictionary numRecords times and retrieve each record and
        # add the sale item price to the total revenue.
        # The loop executes numRecords times and the time complexity is O(n).
        for items in self._salesRecords.values():
            total_revenue += items[1]
        print(f"The total revenue is: {total_revenue:.2f}")


    # duplicateSalesID method creates a duplicateSales list by reading each sale records data and searches
    # it in the salesRecords dictionary. The time complexity of this algorithm is O(n).
    def duplicateSalesID(self):
        duplicateSales = []
        try:
            with open("SalesRecords.csv", 'r') as infile:
                # Read first title line and discard it
                infile.readline()
                index = 0
                # Read every line from the file and split the items using commas.
                # If the item is duplicated, then add the item to the duplicateSales list.
                # The loop executes numRecords times and the time complexity is O(n^2).
                while True:
                    item = infile.readline()

                    if not item:
                        break

                    split_items = item.strip().split(',')
                    # print("Splitting items ", split_items)

                    id_num = int(split_items[0])
                    # Search the id number in salesRecords dictionary.
                    # If it is duplicate, then add it to the duplicateSales list.
                    # The time complexity is O(n).
                    if id_num in self._salesRecords:
                        duplicateSales.append(item)
                # print("The duplicate list is", duplicateSales)

        except IOError:
            print("Error opening file.")
        else:
            infile.close()
        finally:
            print("File closed...")


    # getsaleID method searches for the sale ID in the salesRecords dictionary.
    def getsaleID(self):
        # print("Sale ID between 0 and ", self._numRecords)
        # id = int(input("Please input the sale ID:"))
        id = random.randint(0, self._numRecords)
        # id = int(input(print("Sale ID between 0 and ", self._numRecords)))
        # If id is in salesRecords dictionary, then it prints the sales records, otherwise it
        # will print that the sales record is not found.
        # The time complexity is O(n).
        if id in self._salesRecords:
            print("Sales Records = ", self._salesRecords.get(id))
        else:
            print("Sales record not found!")


# saleRecordsTimes method measures the start and the end times for each method and returns the list of
# start and end times.
def saleRecordsTimes(numRecords):
    start_time = []
    end_time = []
    salesRecords = genSalesRecords(numRecords)
    start_time.append(time.perf_counter())
    salesRecords.generateRecords()
    end_time.append(time.perf_counter())
    start_time.append(time.perf_counter())
    salesRecords.loadSalesData()
    end_time.append(time.perf_counter())
    start_time.append(time.perf_counter())
    salesRecords.totalRevenue()
    end_time.append(time.perf_counter())
    start_time.append(time.perf_counter())
    salesRecords.duplicateSalesID()
    end_time.append(time.perf_counter())
    start_time.append(time.perf_counter())
    salesRecords.latestSale()
    end_time.append(time.perf_counter())
    start_time.append(time.perf_counter())
    salesRecords.getsaleID()
    end_time.append(time.perf_counter())
    start_time.append(time.perf_counter())
    return start_time, end_time


def main():
    # Data points
    numRecords = [100, 1000, 10000, 100000]
    start_time = []
    end_time = []
    genRecordsTime = []
    loadRecordTime = []
    revenueRecordTime = []
    duplicateSalesRecordTime = []
    latestSaleRecordTime = []
    getSaleIdRecordTime = []
    start_time, end_time = saleRecordsTimes(100)
    genRecordsTime.append(end_time[0] - start_time[0])
    loadRecordTime.append(end_time[1] - start_time[1])
    revenueRecordTime.append(end_time[2] - start_time[2])
    duplicateSalesRecordTime.append(end_time[3] - start_time[3])
    latestSaleRecordTime.append(end_time[4] - start_time[4])
    getSaleIdRecordTime.append(end_time[5] - start_time[5])
    start_time, end_time = saleRecordsTimes(1000)
    genRecordsTime.append(end_time[0] - start_time[0])
    loadRecordTime.append(end_time[1] - start_time[1])
    revenueRecordTime.append(end_time[2] - start_time[2])
    duplicateSalesRecordTime.append(end_time[3] - start_time[3])
    latestSaleRecordTime.append(end_time[4] - start_time[4])
    getSaleIdRecordTime.append(end_time[5] - start_time[5])
    start_time, end_time = saleRecordsTimes(10000)
    genRecordsTime.append(end_time[0] - start_time[0])
    loadRecordTime.append(end_time[1] - start_time[1])
    revenueRecordTime.append(end_time[2] - start_time[2])
    duplicateSalesRecordTime.append(end_time[3] - start_time[3])
    latestSaleRecordTime.append(end_time[4] - start_time[4])
    getSaleIdRecordTime.append(end_time[5] - start_time[5])
    start_time, end_time = saleRecordsTimes(100000)
    genRecordsTime.append(end_time[0] - start_time[0])
    loadRecordTime.append(end_time[1] - start_time[1])
    revenueRecordTime.append(end_time[2] - start_time[2])
    duplicateSalesRecordTime.append(end_time[3] - start_time[3])
    latestSaleRecordTime.append(end_time[4] - start_time[4])
    getSaleIdRecordTime.append(end_time[5] - start_time[5])

    # Create the plot
    plt.plot(numRecords, genRecordsTime)

    # Add title and labels
    plt.title('Generate Records Graph')
    plt.xlabel('numRecords')
    plt.ylabel('Time')

    # Display the plot
    plt.show()

    # Create the plot
    plt.plot(numRecords, loadRecordTime)

    # Add title and labels
    plt.title('Load Records Graph')
    plt.xlabel('numRecords')
    plt.ylabel('Time')

    # Display the plot
    plt.show()

    plt.plot(numRecords, revenueRecordTime)

    # Add title and labels
    plt.title('Revenue Records Graph')
    plt.xlabel('numRecords')
    plt.ylabel('Time')

    # Display the plot
    plt.show()

    plt.plot(numRecords, duplicateSalesRecordTime)

    # Add title and labels
    plt.title('Duplicate Sales Record Graph')
    plt.xlabel('numRecords')
    plt.ylabel('Time')

    # Display the plot
    plt.show()

    plt.plot(numRecords, latestSaleRecordTime)

    # Add title and labels
    plt.title('Latest Sales Record Graph')
    plt.xlabel('numRecords')
    plt.ylabel('Time')

    # Display the plot
    plt.show()

    plt.plot(numRecords, getSaleIdRecordTime)

    # Add title and labels
    plt.title('Get Sale ID Record Graph')
    plt.xlabel('numRecords')
    plt.ylabel('Time')

    # Display the plot
    plt.show()
if __name__=="__main__":
    main()
