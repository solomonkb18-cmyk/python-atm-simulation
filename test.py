correct_name = "solomonthang"
namelist = ["bobo", "mgmg", "solomon", "thang","admin", "solomonthang"]
print("--- Automated Brute Forcing Started ---")

for guess in namelist:
    print(f"\nTesting username: {'*' * len(guess)}")
    if guess == correct_name:
        print(f"\n[!] Success! Username found: {guess}")
        print("Welcome " + correct_name)
        break  
    else:
        print("    Wait...Access Denied. Trying next entry...")

print("--- Attack Completed ---")