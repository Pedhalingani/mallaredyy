def solve():
    try:
        N = int(input("Enter number of items: "))  # Number of items
        print("Enter IDs of the items separated by spaces:")
        ids = list(map(int, input().split()))  # IDs of the items
        print("Enter costs of the items separated by spaces:")
        costs = list(map(int, input().split()))  # Costs of the items
        A = int(input("Enter budget (Amount Veda has): "))  # Budget

        if len(ids) != N or len(costs) != N:
            print("Error: The number of IDs or costs does not match the specified number of items.")
            return

        def find_free_items(current_id):
            free_items = []
            for i in range(N):
                if current_id % ids[i] == 0:  # Check divisors
                    free_items.append(i)
            return free_items

        max_items = 0
        max_worth = 0

        for i in range(N):
            cost_of_item = costs[i]

            if cost_of_item <= A:
                free_items_indices = find_free_items(ids[i])
                total_worth = sum(costs[j] for j in free_items_indices)
                num_free_items = len(free_items_indices)

                # Debugging
                print(f"Checking item {ids[i]} with cost {cost_of_item}")
                print(f"Free items: {[ids[j] for j in free_items_indices]} with total worth: {total_worth}")

                if num_free_items > max_items or (num_free_items == max_items and total_worth > max_worth):
                    max_items = num_free_items
                    max_worth = total_worth

        print(max_items, max_worth)

    except ValueError:
        print("Error: Invalid input. Please enter numbers correctly.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    solve()