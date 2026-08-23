### 1. Encapsulation
Encapsulation can be used in the sari-sari store system by organizing the code into distinct "Objects," such as a product object, which bundle related functions and variables. By grouping these elements together, the inventory data is kept secure and structured. This greatly improves the program's design by preventing a mess, ensuring that a single change to a product doesn't accidentally break the rest of the application.

### 2. Abstraction
Abstraction provides cleaner code and easier usage when managing the store's inventory, especially as the system grows large and maintaining it becomes a hassle. It involves hiding the complex background operations of a specific function so the user only interacts with what is strictly necessary. This improves the organization of the program by reducing the impact of change; modifying the internal details of one product's function will not negatively affect or break other parts of the code.

### 3. Inheritance
Inheritance optimizes the inventory system by allowing specific store items to "inherit" traits from one original, primary code block. Instead of manually creating redundant variables and properties for every single new product, new item objects can automatically take on the baseline traits. This improves the program's design by easily shrinking the total amount of code down, preventing redundancy, and making the coding process significantly faster.

### 4. Polymorphism
Polymorphism allows the store's objects to hold their own abilities and perform tasks independently without being heavily reliant on external objects. When processing transactions, these objects only require necessary data, like basic inputs and outputs, to function correctly. This improves the design by making the objects much more independent and self-sufficient, allowing for times when they do not require external code to run smoothly.

## Reflection
Among the four pillars, I believe inheritance will be the most useful for improving the sari-sari store inventory system. Instead of assigning one separate variable for each individual item, new items will instead inherit a value and name directly from the main inventory. By allowing products to automatically adopt what is currently in stock at the sari-sari store, it prevents redundancy and makes the system far more efficient than the previous procedural one.