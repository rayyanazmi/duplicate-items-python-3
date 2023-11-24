# Duplicate Item Detector

The Duplicate Item Detector is a Python 3 script designed to identify and report duplicate items within a list. This simple yet effective tool helps users quickly find and manage duplicate elements in their datasets.

## How to Use

1. **Clone the Repository:**
   ```
   git clone https://github.com/rayyanazmi/duplicate-item-detector.git
   ```

2. **Navigate to the Project Directory:**
   ```
   cd duplicate-item-detector
   ```

3. **Run the Script:**
   ```
   python duplicate_detector.py
   ```

4. **Review Duplicate Items:**
   - The script will iterate through the list and print any duplicate items it detects.

## Code Explanation

The core functionality is implemented in a concise Python script:

```python
nums = [1, 2, 3, 4, 4, 5]
n = len(nums)

for i in range(n - 1):
    if nums[i] == nums[i + 1]:
        print(nums[i])
```

The script utilizes a straightforward loop to compare each item in the list with its adjacent one. If a duplicate is found, it's printed to the console.

## Features and Benefits

- **Simplicity:** The script is easy to understand and use, making it accessible for users of all levels.
- **Flexibility:** Easily adaptable to different datasets and scenarios.
- **Quick Identification:** Rapidly highlights duplicate items within the list.

Feel free to integrate this tool into your Python projects or adapt it to suit your specific needs.

Happy detecting!
