test_dat = """
987654321111111
811111111111119
234234234234278
818181911112111
"""

def load_input(test: bool = False) -> list[str]:
    if test:
        return test_dat.strip().split("\n") 
    with open("./2025/input/day_4.txt") as f:
        banks = f.read().strip().split("\n")
        
    return banks
