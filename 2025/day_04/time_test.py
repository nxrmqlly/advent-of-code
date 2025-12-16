import time

from main import part_two


start = time.perf_counter()
part_two()  # or part_one()
end = time.perf_counter()

print(f"Time taken: {end - start:.6f} seconds")
