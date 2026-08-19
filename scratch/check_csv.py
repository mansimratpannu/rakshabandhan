import csv

csv_path = r"c:\Users\mansi\OneDrive\Desktop\Projects for fun\rakshabandhan\setup\products.csv"

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header count:", len(header))
    print("Header fields:", header)
    
    for i, row in enumerate(reader, start=2):
        if len(row) != len(header):
            print(f"Row {i} has mismatch! Expected {len(header)} but got {len(row)}: {row}")
        else:
            # Check fields
            # Variant Price is at index 9 (0-indexed)
            price = row[9]
            compare_at = row[10]
            published = row[6]
            print(f"Row {i}: Title='{row[1]}', Price='{price}', CompareAt='{compare_at}', Published='{published}'")
