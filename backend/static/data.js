const levelData = {
  1: {
    title: "Game: XOR Madness – Challenge 1 (Port 9011)",
    category: "Cryptography",
    goal: "Crack the strange scroll. It’s base64, but cursed with XOR magic.",
    description: "Folder: challenges/vortex/level_01_xor\nHow to play: Ask the server on port 9011 for the scroll, decode it, then try different 3-letter keys until the hidden flag reveals itself.",
    commands: ["curl http://localhost:9011/ > out.txt", "base64 -d out.txt > decoded", ""],
    hint: "The right key makes the message readable.",
    solved: false
  },
  2: {
    title: "Game: Bad RSA – Challenge 2 (Port 9012)",
    category: "Cryptography",
    goal: "Break the wizard’s weak lock.",
    description: "Folder: challenges/vortex/level_02_rsa\nHow to play: Grab the public key and ciphertext from port 9012. Factor the lock (the modulus), craft the secret key, and read the hidden flag.",
    commands: ["curl http://localhost:9012/pubkey -o pubkey.pem", "python3 RsaCtfTool.py ..."],
    hint: "The lock shares a secret factor. Split it apart!",
    solved: false
  },
  3: {
    title: "Game: ECB Oracle – Challenge 3 (Port 9013)",
    category: "Cryptography",
    goal: "Trick the oracle of blocks.",
    description: "Folder: challenges/vortex/level_03_ecb_oracle\nHow to play: Connect to port 9013. Feed the oracle chosen words and watch the blocks. Use patterns to uncover the hidden phrase one byte at a time.",
    commands: ["nc localhost 9013", "python3 ecb_oracle_exploit.py"],
    hint: "Same words create the same blocks.",
    solved: false
  },
  4: {
    title: "Game: Custom Hash Hell – Challenge 4 (Port 9014)",
    category: "Cryptography",
    goal: "Defeat the goblin’s fake hash spell.",
    description: "Folder: challenges/vortex/level_04_custom_hash\nHow to play: Visit port 9014. The goblin gives you a hash. Brute-force until you find the word that makes the same hash, and the flag is yours.",
    commands: ["nc localhost 9014", "python3 hash_crack.py"],
    hint: "The spell is weak. Brute force wins.",
    solved: false
  },
  5: {
    title: "Game: Timing Leak HMAC – Challenge 5 (Port 9015)",
    category: "Cryptography",
    goal: "Outsmart the timekeeper.",
    description: "Folder: challenges/vortex/level_05_timing_hmac\nHow to play: Ask port 9015 to check HMACs. Watch carefully: the more right characters you guess, the slower it responds. Piece together the full code for the flag.",
    commands: ["python3 timing_attack.py http://localhost:9015/check"],
    hint: "Speed tells you which guess is closer.",
    solved: false
  },
  6: {
    title: "Game: Stack Overflow – Challenge 6 (Port 9016)",
    category: "Binary Exploitation",
    goal: "Overflow the hero’s backpack.",
    description: "Folder: challenges/vortex/level_06_stack_overflow\nHow to play: Connect to port 9016. Stuff more items into the buffer than it can hold. Overwrite the return path and jump straight into the treasure function that prints the flag.",
    commands: ["gdb ./vuln", "python3 exploit.py | nc localhost 9016"],
    hint: "Find the right spot to overwrite.",
    solved: false
  },
  7: {
    title: "Game: Format String Fun – Challenge 7 (Port 9017)",
    category: "Binary Exploitation",
    goal: "Bend printf to your will.",
    description: "Folder: challenges/vortex/level_07_fmt\nHow to play: Talk to port 9017. Use magic format codes (%x, %n) to peek into memory. Leak what you need, then write into GOT to change destiny and grab the flag.",
    commands: ["./vuln '%p %p %p'", "nc localhost 9017"],
    hint: "puts@GOT and exit@GOT are weak spots.",
    solved: false
  },
  8: {
    title: "Game: ROP Me Baby – Challenge 8 (Port 9018)",
    category: "Binary Exploitation",
    goal: "Build the chain of gadgets.",
    description: "Folder: challenges/vortex/level_08_rop\nHow to play: Gather gadgets from the binary. Forge a chain that calls system('/bin/sh'). Send it to port 9018 to spawn a shell and read the flag.",
    commands: ["ROPgadget --binary vuln", "python3 exploit.py | nc localhost 9018"],
    hint: "Look for 'pop rdi; ret'.",
    solved: false
  },
  9: {
    title: "Game: LD_PRELOAD Hijack – Challenge 9 (Port 9019)",
    category: "Binary Exploitation",
    goal: "Swap the library with your own.",
    description: "Folder: challenges/vortex/level_09_ldpreload\nHow to play: Forge an evil library. Preload it so your code runs instead of printf. Make it spit out the flag when the game calls a function.",
    commands: ["gcc -shared -fPIC preload.c -o evil.so", "LD_PRELOAD=./evil.so ./vuln"],
    hint: "Hijack printf or fopen.",
    solved: false
  },
  10: {
    title: "Game: Predictable PRNG – Challenge 10 (Port 9020)",
    category: "Reverse Engineering",
    goal: "Predict the fortune teller’s numbers.",
    description: "Folder: challenges/vortex/level_10_random\nHow to play: Connect to port 9020. The seer gives you 20 numbers. Rebuild the same generator locally, guess the seed, and return it to win the flag.",
    commands: ["nc localhost 9020"],
    hint: "It uses time(NULL) as seed.",
    solved: false
  },
  11: {
    title: "Game: Bomb Defusal – Challenge 11 (Port 9021)",
    category: "Binary Exploitation",
    goal: "Defuse the bomb in time!",
    description: "Folder: challenges/vortex/level_11_fmt2root\nHow to play: Run the program or connect to port 9021. Quickly exploit the format string to take control before the timer runs out. Change exit() into system('/bin/sh') and claim the flag.",
    commands: ["python3 fmt_exploit.py | nc localhost 9021"],
    hint: "Leaking libc gives you the right address.",
    solved: false
  },
  12: {
    title: "Game: Signal Puzzle – Challenge 12 (Port 9022)",
    category: "Binary / RE",
    goal: "Send the right signal at the right time.",
    description: "Folder: challenges/vortex/level_12_signal\nHow to play: Start the binary or connect to port 9022. When the game is ready, fire SIGUSR1 at it. Do it too early or too late, and it explodes. Hit the timing and the flag appears.",
    commands: ["./vuln &", "kill -USR1 <pid>"],
    hint: "Trace system calls to know the window.",
    solved: false
  },
  13: {
    title: "Game: Base64 Socket Trap – Challenge 13 (Port 9023)",
    category: "Networking / RE",
    goal: "Send the magic phrase in base64.",
    description: "Folder: challenges/vortex/level_13_socket_base64\nHow to play: Connect to port 9023. The gate only opens if you give it the right base64 phrase. Reverse the check and feed it the secret to earn the flag.",
    commands: ["echo 'c3VwZXJfc2VjcmV0X3BocmFzZQ==' | nc localhost 9023"],
    hint: "Decode and adjust until accepted.",
    solved: false
  }
};