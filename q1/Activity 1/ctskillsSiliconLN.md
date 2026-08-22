Annex A
Computational Thinking Exercise: "Smart School Canteen Queue"

Section: ______________9-Silicon______________ Score:____________

C# / Name:_______________Ivan Adelf I. Corporal________________ Date: ____8/20/2026______


Scenario

The PSHS school canteen is small and often gets crowded during lunch break. Students line up to buy food, but the process is slow because:

Some students take too long to decide what to order.
The cashier has to manually calculate totals and give change.
There is no system to track which food items are running out.
Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

Step 1: Identify the Big Problem

Main Problem: 
# The PSHS school canteen experiences severe crowding and long wait times during lunch break due to inefficient, manual service and inventory processes.

Step 2: Identify three to four Sub-Problems
Please list possible sub-problems:

1. # Students spend too much time choosing items at the register because they cannot view the menu or stock availability in advance.

2. # Cashiers waste time manually computing item totals and calculating cash change for every customer.

3. # There is no real-time system to monitor remaining stock, causing confusion when items run out unexpectedly.

4. # A lack of structured queue ordering or status updates creates congestion and physical overcrowding in the canteen space.

Step 3: Define Computational Thinking Approaches
For each sub-problem, apply CT skills:

# Step 3 Answers

# Sub Problem:             CT Skill:             Solution:
# [Number 1]              Abstraction         Display only essential menu details on a pre-order board.
# [Number 2]            Algorithm Design      Automate price totals and change calculation.
# [Number 3]           Pattern Recognition    Auto-subtract sold items to alert when items run low.
# [Number 4]             Decomposition        Split the line into distinct, ordering, payment, and pickup stations.


Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem

# Step 4: (Pseudocode)
START
    // 1. Display Menu (Abstraction)
    FOR EACH item IN Menu WHERE stock > 0
        DISPLAY item.name, item.price
    END FOR

    // 2. Process Order & Update Stock (Pattern Recognition)
    total = 0
    FOR EACH item IN SelectedItems
        total = total + item.price
        item.stock = item.stock - 1
    END FOR

    // 3. Calculate Payment (Algorithm Design)
    DISPLAY "Total: ", total
    INPUT cash
    change = cash - total
    DISPLAY "Change: ", change

    // 4. Direct to Pickup (Decomposition)
    DISPLAY "Order Complete. Proceed to Pickup Station."
END

