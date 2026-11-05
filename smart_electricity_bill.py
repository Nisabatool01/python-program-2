# Program 2: Smart Electricity Bill Calculator
# Topic: for loop, range(), accumulators, and conditional statements inside loops.

# Smart Electricity Bill Calculator

print("===== ELECTRICITY BILL SYSTEM =====")

households = int(input("Enter the number of households: "))

# Improvement 1: Validate household count
if households <= 0:
    print("Invalid number of households!")

else:
    # Initialize accumulators and counters
    total_revenue = 0
    processed_households = 0
    invalid_households = 0

    # Process each household
    for household in range(1, households + 1):

        print(f"\n--- Household {household} ---")

        units = int(input("Enter electricity units consumed: "))

        # Validate electricity units
        if units < 0:
            print("Invalid units! Please enter a non-negative value.")
            invalid_households += 1
            continue

        # Calculate electricity bill
        if units <= 100:
            bill = units * 10

        elif units <= 200:
            bill = (100 * 10) + ((units - 100) * 15)

        else:
            bill = (100 * 10) + (100 * 15) + ((units - 200) * 20)

        # Display individual bill
        print(f"Units Consumed: {units}")
        print(f"Electricity Bill: Rs. {bill}")

        # Update accumulators and counters
        total_revenue += bill
        processed_households += 1

    # Display monthly revenue report
    print("\n===== MONTHLY REVENUE REPORT =====")
    print(f"Total Households: {households}")
    print(f"Successfully Processed: {processed_households}")
    print(f"Invalid Households: {invalid_households}")
    print(f"Total Revenue: Rs. {total_revenue}")