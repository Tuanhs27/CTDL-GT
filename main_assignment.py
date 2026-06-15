from routing import demo_routing_shortest_path, demo_mst_network
from hashing_tools import (OrderHashTable, group_coupon_anagrams, longest_consecutive_days, count_revenue_windows, rolling_hash_search)
from promo_optimizer import (climb_stairs, build_combo_dp_table, trace_combo_from_dp, combo_knapsack_1d)

def run_menu():
    while True:
        print("\n=== POLY-SHIP SYSTEM MENU ===")
        print("1. Demo routing - shortest path")
        print("2. Demo MST - mạng kho tối thiểu")
        print("3. Demo hash table đơn hàng")
        print("4. Demo hashing (anagrams, liên tiếp, subarray sum)")
        print("5. Demo rolling hash")
        print("6. Demo DP cơ bản")
        print("7. Demo combo khuyến mãi (Knapsack 0/1)")
        print("8. Thoát")
        
        choice = input("Chọn chức năng (1-8): ")
        
        if choice == '1':
            demo_routing_shortest_path()
        elif choice == '2':
            demo_mst_network()
        elif choice == '3':
            ht = OrderHashTable()
            ht.insert("ORD01", {"item": "Laptop", "price": 1000})
            print("Get ORD01:", ht.get("ORD01"))
            ht.remove("ORD01")
            print("Get ORD01 sau khi xóa:", ht.get("ORD01"))
        elif choice == '4':
            print("Anagrams:", group_coupon_anagrams(["SAVE10", "AVES10", "10SAVE", "PROMO"]))
            print("Ngày liên tiếp:", longest_consecutive_days([100, 4, 200, 1, 3, 2]))
            print("Subarray sum (k=5):", count_revenue_windows([1, 2, 3, -1, 3], 5))
        elif choice == '5':
            print("Tìm pattern 'PROMO' trong 'ABCPROMOXYZ': index =", rolling_hash_search("ABCPROMOXYZ", "PROMO"))
        elif choice == '6':
            print("Climbing stairs (5 bậc):", climb_stairs(5), "cách")
        elif choice == '7':
            prices = [10, 20, 30]
            scores = [60, 100, 120]
            B = 50
            dp_2d = build_combo_dp_table(prices, scores, B)
            print("Các SP chọn (2D):", trace_combo_from_dp(dp_2d, prices, scores, B))
            print("Max score (1D):", combo_knapsack_1d(prices, scores, B))
        elif choice == '8':
            print("Thoát chương trình.")
            break
        else:
            print("Vui lòng chọn lại!")

if __name__ == "__main__":
    run_menu()