import sys

# Default numbers already included
default_scores = [10, 20, 30, 40, 50]

def convert_to_float(values):
    converted = []
    for v in values:
        try:
            converted.append(float(v))
        except ValueError:
            print(f"Warning: '{v}' is not a number. Ignoring it.")
    return converted

if len(sys.argv) > 1:
    scores = convert_to_float(sys.argv[1:])
    if not scores:  # If all arguments were invalid
        print("No valid numbers provided. Using default scores.")
        scores = default_scores
else:
    print("Using default scores:", default_scores)
    scores = default_scores

total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("Sum:", total)
print("Average:", average)
print("Max:", maximum)
print("Min:", minimum)
