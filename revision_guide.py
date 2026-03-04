"""
Python Revision Guide
Covers: Core Syntax, OOP, NumPy, Matplotlib, File Handling
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import csv

# =====================================================================
# 1. CORE PYTHON SYNTAX & FILE HANDLING
# =====================================================================
print("--- 1. Core Syntax & File Handling ---")

# Let's write some data to a file and read it back
sample_data = [
    {"day": "Monday", "sales": 120},
    {"day": "Tuesday", "sales": 150},
    {"day": "Wednesday", "sales": 130}
]

file_name = "sample_data_temp.csv"

# Writing to a file
with open(file_name, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["day", "sales"])
    writer.writeheader()
    writer.writerows(sample_data)
    print(f"Wrote dummy data to {file_name}")

# Reading from a file (List comprehension & basic types)
read_sales = []
with open(file_name, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        read_sales.append(int(row["sales"]))
        
print(f"Read sales data: {read_sales}")

# =====================================================================
# 2. OBJECT-ORIENTED PROGRAMMING (OOP)
# =====================================================================
print("\n--- 2. Object-Oriented Programming ---")

# --- Functions vs. Methods in OOP ---
# 1. Standalone Function: Defined outside a class. Operates independently.
def standalone_function():
    print("I am a standalone function. I don't belong to any class.")

class SalesReport:
    """
    A class to encapsulate sales data logic.
    Demonstrates classes, `__init__`, methods, and properties.
    """
    # Class attribute (shared across all instances)
    report_type = "Financial"

    def __init__(self, brand_name, sales_data):
        self.brand_name = brand_name
        self._sales_data = sales_data  # Protected attribute (encapsulation)
        
    @property
    def total_sales(self):
        """Calculate total sales using core Python syntax"""
        return sum(self._sales_data)
        
    # 2. Member Method (Instance Method): 
    # Takes 'self' as the first parameter.
    # Operates on a specific instance of the class and can access instance attributes.
    def display_summary(self):
        print(f"Brand: {self.brand_name} ({self.report_type})")
        print(f"Total Sales: {self.total_sales}")
        print(f"Average Sales: {self.total_sales / len(self._sales_data):.2f}")

    # 3. Class Method:
    # Takes 'cls' as the first parameter. 
    # Operates on the class itself, not on instances. Often used as alternative constructors.
    @classmethod
    def change_report_type(cls, new_type):
        cls.report_type = new_type
        print(f"Report type changed to: {cls.report_type}")

    # 4. Static Method:
    # Doesn't take 'self' or 'cls'. 
    # Behaves like a normal function but belongs to the class namespace. 
    # Useful for utility functions that relate to the class but don't need its data.
    @staticmethod
    def is_valid_sales_data(data):
        return isinstance(data, list) and all(isinstance(x, (int, float)) for x in data)

# Demonstrating Functions vs Methods:
print("\n[Functions vs Methods Demo]")
standalone_function()  # Calling standalone

# Calling member method
report = SalesReport("LuxyLenz", read_sales)
report.display_summary()

# Calling class method
SalesReport.change_report_type("Annual Financial")

# Calling static method
is_valid = SalesReport.is_valid_sales_data(read_sales)
print(f"Is read_sales valid? {is_valid}")

# =====================================================================
# 3. NUMPY: FAST NUMERICAL OPERATIONS
# =====================================================================
print("\n--- 3. NumPy ---")

class AdvancedSalesReport(SalesReport):
    """
    Inheriting from SalesReport to add advanced NumPy capabilities.
    Demonstrates OOP Inheritance.
    """
    def __init__(self, brand_name, sales_data):
        super().__init__(brand_name, sales_data)
        # Convert list to a NumPy array for vectorized operations
        self.sales_array = np.array(self._sales_data)
        
    def calculate_metrics(self):
        # NumPy makes statistical calculations easy and fast
        mean_sales = np.mean(self.sales_array)
        max_sales = np.max(self.sales_array)
        min_sales = np.min(self.sales_array)
        std_dev = np.std(self.sales_array)
        
        print(f"Min Sales:   {min_sales}")
        print(f"Max Sales:   {max_sales}")
        print(f"Mean Sales:  {mean_sales:.2f}")
        print(f"Std Dev:     {std_dev:.2f}")

    def apply_tax(self, tax_rate=0.15):
        # Vectorized operation: multiplies every element without a for-loop!
        sales_with_tax = self.sales_array * (1 + tax_rate)
        print(f"Sales post-tax (15%): {sales_with_tax}")

adv_report = AdvancedSalesReport("LuxyLenz Pro", read_sales)
adv_report.calculate_metrics()
adv_report.apply_tax()

# =====================================================================
# 4. MATPLOTLIB: DATA VISUALIZATION
# =====================================================================
print("\n--- 4. Matplotlib ---")

def plot_sales_trend(sales_array):
    """
    Demonstrates how to tie the NumPy array into a Matplotlib visualization.
    """
    days = np.array(["Mon", "Tue", "Wed"])
    
    # Create the figure and axis
    plt.figure(figsize=(8, 4))
    
    # Plot data
    plt.plot(days, sales_array, marker='o', linestyle='-', color='b', label='Daily Sales')
    plt.bar(days, sales_array, alpha=0.3, color='c', label='Bar View')
    
    # Customize the chart
    plt.title("Weekly Sales Trend")
    plt.xlabel("Days")
    plt.ylabel("Sales ($)")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    
    # Save the plot to a file
    plot_file = "sales_plot_demo.png"
    plt.savefig(plot_file)
    print(f"Plot saved to {plot_file}")
    
    # To view the plot while running interactively, uncomment below:
    # plt.show()

# Calling the visualization function using our OOP/NumPy processed data
plot_sales_trend(adv_report.sales_array)

# =====================================================================
# CLEANUP (Optional)
# =====================================================================
# Removing the generated dummy file from section 1 to keep things clean
if os.path.exists(file_name):
    os.remove(file_name)
    print(f"\nCleaned up temporary file: {file_name}")
