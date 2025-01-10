import requests
import concurrent.futures
import time

# URL of the web page to test
URL = "https://mac3859.github.io/login-service/"  

# Function to simulate a single user accessing the page
def simulate_user(user_id):
    try:
        start_time = time.time()
        response = requests.get(URL)
        end_time = time.time()

        # Print the result
        if response.status_code == 200:
            print(f"User {user_id}: Success! Response time: {end_time - start_time:.2f} seconds")
        else:
            print(f"User {user_id}: Failed! Status code: {response.status_code}")
    except Exception as e:
        print(f"User {user_id}: Error - {str(e)}")

# Number of users to simulate
NUM_USERS = 100

# Run the test
if __name__ == "__main__":
    start_time = time.time()

    # Use ThreadPoolExecutor to simulate concurrent users
    with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_USERS) as executor:
        # Submit tasks for each user
        futures = [executor.submit(simulate_user, i) for i in range(NUM_USERS)]

        # Wait for all tasks to complete
        concurrent.futures.wait(futures)

    total_time = time.time() - start_time
    print(f"Total time for {NUM_USERS} users: {total_time:.2f} seconds")