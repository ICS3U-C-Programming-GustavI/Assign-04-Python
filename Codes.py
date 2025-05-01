#!/usr/bin/env python3
# # Created by: Gustav I
# # Created on: April 28, 2025
# # This is the source file for bomb defusal codes.

codes = {
    "Red": True,
    "Green": True,
    "Blue": True,
    "Yellow": True,
    "Gray": True,
    "White": True,
}

# Print available codes if you run this file directly
if __name__ == "__main__":
    print("Available codes")
    for code in codes.keys():
        print(code)
