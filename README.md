### Introduction
- This is the week 9 homework repository of ERMC K5455 (Applied Coding for Risk Mgmt) at Columbia University. 
- Please refer to Canvas for the homework deadline.

<hr>

### How to submit the homework

1. Create a class called `BankAccount` with the following attributes and methods:
   - Attributes: 
     - name (string): the name of the owner
     - balance (number): the balance of the account, default equal to `0`
   - Methods:
     - `__init__(self, name, balance)`: initialize a BankAccount object with a string and a number.
     - `deposit(self, n)`: add n to the balance
     - `withdraw(self, n)`: subtract n from the balance, if n > balance, `raise ValueError("You don't have enough money!")`
     - `check_balance`: return the remaining balance of the account as a string following the format below: `'Your current balance is <balance>'`
2. Write SQL queries to do the following:
   - Find all the employees who earn more than the average salary from the `employees` table and return `employee_id`,	`first_name`, `last_name` columns.
   - Find all the customers who have ordered lettuce(id=3) and return `customer_id`, `first_name`, `last_name` columns.
3. We will be using the same Titanic dataset, but we will train a Random Forest model this time
   - Follow the same preprocessing steps as HW3
   - Split the data into training and testing set (80/20) and use a random seed of 42.
   - For `n_estimators` in `range(10, 500, 40)`, find the optimal value that gives you the best score on the test set.
   - Return the random forest model fitted on the training set with the optimal value you found in the previous step and along with the predictions made on the test set. Make sure you use `np.random.seed(42)` when you select the `n_estimators`.
4. Define a function called `word_count` that takes a string and an optional parameter called `number` as the input.
   - The `number` parameter is set to `False` by default. You should count numbers in the input string if `number` is equal to `True`.
   - Hint: make sure you are **NOT** counting duplicates of the same word, i.e. `It` and `it` should be considered as the same word.
   - You can use the convenient `Counter()` data type from the `collections` module. See the details [here](https://docs.python.org/3/library/collections.html#collections.Counter). 
   - Return the `Counter` object at the end of the function.
