# Python Project: Quantitative Trading & Analytics Engine

## Objective
The goal of this project is to build a high-performance quantitative trading simulator. You will use **NumPy** for robust array-based mathematical analytics, **Matplotlib** for comprehensive data visualization, and **Advanced Object-Oriented Programming (OOP)** to construct and manage the financial ecosystem. You will not use Pandas, forcing you to develop the fundamental pipelines from scratch.

## Project Requirements
1. **Allowed Imports**: `csv`, `numpy` (as `np`), `matplotlib.pyplot` (as `plt`), and built-in Python modules (like `datetime`, `math`). Do not use Pandas.
2. **Master-Level OOP**: You must utilize private attributes (name mangling like `__attr`), properties (`@property` getters and setters), inheritance, magic methods (e.g., `__add__`, `__len__`, `__str__`), as well as explicit `@classmethod` and `@staticmethod` decorators.
3. **Data Handling**: Lists must be converted to NumPy arrays for heavy numerical computation.
4. **Exception Handling**: Validate inputs and handle errors gracefully (e.g., trying to read a missing file, fetching an invalid stock, withdrawing more money than available).

## Architecture & File Responsibility
- `file_handler.py` ➔ CSV reading/writing for historical data and exporting logs.
- `instruments.py` ➔ Defining tradable financial assets with very strict encapsulation (OOP Inheritance).
- `portfolio.py` ➔ Managing positions, calculating total value, and executing trades (Advanced OOP).
- `analytics.py` ➔ Pure NumPy-heavy module for statistical computations.
- `visualizer.py` ➔ Matplotlib plotting functions.
- `main.py` ➔ Orchestrator that pipes data between files.

---

## Module Breakdown & Detailed Instructions

### Module 1: `instruments.py` (OOP Mastery)
*This module contains the strict representation of tradable assets.*

**1⃣ Class `FinancialInstrument` (Base Class)**
- **Private Attributes**: `__symbol` (str), `__price_history` (1D NumPy array).
- **Properties**: 
  - Getter for `symbol`.
  - Setter for `symbol` that validates it is strictly an uppercase string between 3 and 5 characters.
  - Getter for `current_price` (returns the last element of the price history array).
- **Abstract Method**: `calculate_risk(self)` (Just raise a `NotImplementedError` inside it).
- **Magic Methods**: 
  - `__str__`: Returns cleanly formatted symbol name and current price.
  - `__len__`: Returns the number of price data points in the history.

**2⃣ Class `Stock` (inherits from `FinancialInstrument`)**
- **Additional Private Attributes**: `__company_name`, `__sector`.
- **Static Method**: `@staticmethod is_market_open(time_str)`: takes a string like `"10:30"` and returns `True` if it sits between `"09:30"` and `"16:00"`, otherwise `False`. (A static method does not require access to `self` or `cls`).
- **Overridden Method**: `calculate_risk(self)`: Converts `__price_history` to a numpy array, calculates and returns the standard deviation (`np.std`).

**3⃣ Class `Crypto` (inherits from `FinancialInstrument`)**
- **Additional Private Attributes**: `__network_fee`.
- **Class Attribute**: `TOTAL_CRYPTO_ASSETS = 0` (Increment this inside `__init__` whenever a new crypto is instantiated).
- **Class Method**: `@classmethod get_total_assets(cls)` returns the total number of crypto objects created.

---

### Module 2: `portfolio.py` (Advanced OOP)
*Manages positions and executes trades.*

**4⃣ Class `Portfolio`**
- **Private Attributes**: `__owner_name`, `__balance` (float), `__holdings` (dict mapping symbol to quantity).
- **Property**: Getter `balance` and a setter that raises a `ValueError` if the balance falls below `0`. 
- **Class Method**: `@classmethod from_csv(cls, file_path)`: Factory method that uses `file_handler.py` to read an account balance from a CSV snippet, initializes the Portfolio with it, and returns the Portfolio instance. (This demonstrates using class methods as alternative constructors).
- **Static Method**: `@staticmethod calculate_transaction_fee(amount, transaction_type)`: If type is `"BUY"`, fee is `1%`. If `"SELL"`, fee is `2%`. Returns the fee.
- **Member Methods**:
  - `buy_instrument(self, instrument, quantity)`: Checks if there is enough balance, deducts the cost + fee (calling the static method), and updates the `__holdings` dictionary.
  - `get_portfolio_value(self, current_prices_dict)`: Calculates the total value of holdings + cash balance.
- **Magic Method**: `__add__(self, other)`: Overload the `+` operator. Combining two Portfolios should return a *new* Portfolio instance spanning the sum of their balances and a merged dictionary of their holdings.

---

### Module 3: `file_handler.py` (File Handling Focus)

**5⃣ `load_market_data(file_path)`**
- Opens and reads a CSV file containing columns for `Date` and various asset prices (e.g. `AAPL`, `BTC`).
- Use `csv.reader` or `csv.DictReader`. Skip the header.
- Create a dictionary where the keys are the symbols and the values are lists of floats.
- Handle `FileNotFoundError` explicitly.

**6⃣ `export_trade_log(file_path, logs)`**
- Write a list of transaction dictionaries (keys: `"Datetime", "Action", "Symbol", "Quantity", "Price"`) to a CSV file using `csv.DictWriter`.

---

### Module 4: `analytics.py` (NumPy Focus)
*You will pass pure Python lists to these functions, immediately convert them to NumPy arrays, and perform vectorized operations.*

**7⃣ `calculate_daily_returns(price_list)`**
- Convert to NumPy array.
- Calculate percentage change day-over-day: `(prices[1:] - prices[:-1]) / prices[:-1]`. 

**8⃣ `generate_correlation_matrix(*price_lists)`**
- Convert multiple 1D target lists to arrays.
- Combine them vertically using `np.vstack()`.
- Compute and return the correlation matrix using `np.corrcoef()`.

**9⃣ `get_volatility_spikes(price_list, percentage_threshold)`**
- Calculate daily returns.
- Use **Boolean Indexing** (e.g., `returns[np.abs(returns) > threshold]`) to extract and return an array of returns that exceeded the threshold spike/drop.

---

### Module 5: `visualizer.py` (Matplotlib Focus)
*Generating comprehensive dashboards.*

**🔟 `plot_financial_dashboard(dates, price_list)`**
- Convert `price_list` to a NumPy array.
- Use `fig, ax = plt.subplots(2, 1, figsize=(10, 8))` to create two stacked distinct charts.
- **Top Subplot (Index 0)**: 
  - Line plot mapping `dates` vs `price_list`. 
  - Add a horizontal dashed line (`ax.axhline`) showing the **Mean** price computed via Numpy.
  - Add title, legends, grid, and colored markers.
- **Bottom Subplot (Index 1)**: 
  - Calculate the daily returns via `analytics.py`.
  - Plot a Histogram (`ax.hist`) of the returns with `bins=20` to view the volatility distribution.
- Use `fig.subplots_adjust()` to fix any overlap and `plt.savefig()` to export to `dashboard.png`.
- Do not forget `plt.close()` at the end so plots don't pile up in memory.

---

### Recommended Workflow
1. Scaffold all classes and decorators without logic (`pass`). Ensure your class hierarchies are defined.
2. Program the `file_handler.py` to get raw data flowing.
3. Build the core NumPy formulas in `analytics.py`. 
4. Bring it all together in `Portfolio` by simulating some buying and selling.
5. Finish up by plugging values into Matplotlib. Ensure you refer heavily to the `cheatsheet.md`!
