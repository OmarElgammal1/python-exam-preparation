# Mini-Projects: Implementation Hints & Architecture Guide

This document contains step-by-step guidance, architectural tips, and edge-case warnings for the two revision mini-projects.

## Project 1: Eyewear E-commerce Sales Tracker
**Goal:** Process a CSV of daily eyewear sales (e.g., LuxyLenz), use OOP to model inventory and sales, apply NumPy for revenue metrics, and use Matplotlib for graphing trends.

### Step-by-Step Hints
1. **File Handling (The Input):** Start by opening `sales_data.csv` using Python's built-in `csv` module (specifically `csv.DictReader` works great). Extract the dates, product names, units sold, and prices.
2. **OOP (The Architecture):**
   - Create a `SalesRecord` class to hold individual row data (date, product_id, product_name, units_sold, price).
   - Create a `StoreManager` class that holds a list of these objects. This manager class should be responsible for parsing the CSV file and populating its list.
3. **NumPy (The Math):** 
   - Add a method in `StoreManager` (e.g., `calculate_daily_revenue()`) that extracts the raw numbers.
   - Convert units sold and prices into NumPy arrays: `units_array = np.array([...])` and `price_array = np.array([...])`.
   - Use vectorized multiplication (`units_array * price_array`) to calculate total revenue per transaction without writing a loop.
4. **Matplotlib (The Visuals):**
   - Extract unique dates and calculate total revenue aggregated per day.
   - Use Matplotlib to plot `plt.plot(dates, daily_revenues)`. 
   - Consider adding a `plt.xticks(rotation=45)` so the dates don't overlap on the X-axis.

### Edge-Case Warnings & Tips
- **Warning:** `csv` reads everything as strings. Remember to explicitly cast `units_sold` to `int` and `price_per_unit` to `float` before doing math!
- **Warning:** Dates might be out of order in a real-world file (though our dummy data is ordered). Sorting by date before plotting is a strong defensive programming habit.
- **Tip:** When plotting overlapping lines or multiple products, use different colors, markers, and a legend to distinguish them.

---

## Project 2: Smart Traffic Log Analyzer
**Goal:** Parse a text log file (`traffic_logs.txt`), process vehicle detections with NumPy, and plot peak congestion times with Matplotlib.

### Step-by-Step Hints
1. **File Handling (The Parsing):** open `traffic_logs.txt`. You'll notice the first line starts with `#`. This means it's a comment or header metadata. Read the file line-by-line using a `for` loop, and use an `if not line.startswith('#'):` check to skip comments.
2. **String Manipulation:** For valid lines, use `line.split('|')` to separate the timestamp, count, speed, and congestion level. Strip away any extra whitespace using `.strip()`.
3. **NumPy (Data Aggregation):**
   - Extract the vehicle counts and speeds into lists, then convert them into NumPy arrays (`np.array()`).
   - Use NumPy statistical functions: `np.mean()`, `np.max()`, and `np.min()` to find the peak traffic volume and average speed across the day.
   - *Challenge*: Create a boolean mask in NumPy (e.g., `high_traffic = counts > 100`) to quickly find out how many hours experienced severe congestion.
4. **Matplotlib (Peak Times Visualization):**
   - You want to highlight the correlation between the time of day and the volume of traffic.
   - Extract just the hour from the timestamp (e.g., `17` from `2023-10-10 17:00:00`) to use on the X-axis.
   - Create a dual-axis plot (using `ax1.twinx()`), or two subplots (`plt.subplots(2, 1)`): One showing vehicle volume, and the other showing average speed dropping when volume peaks.

### Edge-Case Warnings & Tips
- **Warning:** A text file split with `|` leaves spaces at the ends of the extracted strings (e.g., `" 120 "`). Always run `.strip()` on extracted parts.
- **Warning:** Missing data. What if a line looks like `2023-10-10 14:00:00 |  |  | `? Consider writing a `try-except` block or an `if` statement to skip malformed lines so your script doesn't crash on `int("")`.
- **Tip:** Use Matplotlib's `plt.axhline()` to draw a horizontal red "threshold" line on your chart (e.g., at 100 vehicles) to visually indicate where the "High Congestion" zone begins.
