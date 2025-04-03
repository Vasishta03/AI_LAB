from collections import deque
import random
import time

class BankQueue:
    def __init__(self):
        self.queue = deque()
        self.total_wait = 0
        self.cust_served = 0

    def add_cust(self, cust_id):
        arrival_time = time.time()
        self.queue.append({
            'id': cust_id, 
            'arrival_time': arrival_time
        })
        print(f"Customer {cust_id} joined the queue")

    def serve_cust(self):
        if not self.queue:
            print("No customers")
            return None
        cust = self.queue.popleft()
        wait_time = time.time() - cust['arrival_time']
        self.total_wait += wait_time
        self.cust_served += 1 
        print(f"Customer {cust['id']} served. Wait time: {wait_time:.2f} seconds")
        return cust

    def get_avg_wait_time(self):
        if self.cust_served == 0:
            return 0
        return self.total_wait / self.cust_served

def simulate(total_cust, max_wait=3):
    bank = BankQueue()
    for cust_id in range(1, total_cust + 1):
        bank.add_cust(cust_id)
        time.sleep(random.uniform(0.5, max_wait))
        bank.serve_cust()
    print("\n--- Simulation Complete ---")
    print(f"Total Customers Served: {bank.cust_served}")
    print(f"Avg Wait Time: {bank.get_avg_wait():.2f} seconds")

if __name__ == "__main__":
    simulate(total_cust=10)
