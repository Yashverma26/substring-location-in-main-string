import time
def find_substring(main_string, substring):
    return main_string.find(substring)
def time_find_substring(main_string, substring):
    start_time = time.time()
    index = find_substring(main_string, substring)
    end_time = time.time()
    time_taken = end_time - start_time
    return index, time_taken
main_string = "hello boys and girls, lets start the new chapter of DSA."
substring = "lets"
index, time_taken = time_find_substring(main_string, substring)
if index != -1:
    print(f"Substring found at index: {index}")
else:
    print("Substring not found.")
print(f"Time taken to find the substring: {time_taken} seconds")
