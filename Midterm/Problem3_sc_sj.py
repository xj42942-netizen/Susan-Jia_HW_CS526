def max_items_selected(categories):
    n = len(categories)
    max_items = 0
    
    for start in range(n):
        baskets = {}
        
        for end in range(start, n):
            category = categories[end]
            baskets[category] = baskets.get(category, 0) + 1
            
            if len(baskets) > 2:
                break
            
            items_count = end - start + 1
            max_items = max(max_items, items_count)
    
    return max_items

files = ['sc_input1.txt', 'sc_input2.txt']
results = []

for filename in files:
    with open(filename, 'r') as f:
        lines = f.read().strip().split('\n')
    
    num_aisles = int(lines[0])
    categories = lines[1].strip().split(',')
    
    result = max_items_selected(categories)
    results.append(f"Testing {filename}: {result} items were selected")

for r in results:
    print(r)

# Save to file
with open('shopping_cart_output.txt', 'w') as f:
    f.write('\n'.join(results))
