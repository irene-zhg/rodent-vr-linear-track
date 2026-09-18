# Converts sav data to CSV

import os

# check file exists in given path
while True:
    file_in = input("Enter input file name: ")
    # replace X with input path
    input_path = f"X/{file_in}.sav"

    if os.path.exists(input_path):
        break
    print("ERROR: File not found. Please try again.")

# replace Y with output path
output_path = f"Y/{file_in}_converted.csv"

# ensure only timestamp, x, y, z, yaw, and displacement strings are appended
def looks_like_csv_row(text):
    parts = text.split(",")
    if len(parts) != 6:
        return False
    try:
        for value in parts:
            if value == "MARKER":
                continue
            float(value)
        return True
    except ValueError:
        return False

with open(input_path, "rb") as f:
    raw_data = f.read()

# extract string values out of Unreal's binary format
text_segments = raw_data.split(b"\x00")
clean_rows = []

for row in text_segments:
    text = row.decode("utf-8", errors="ignore").strip()
    if looks_like_csv_row(text):
        clean_rows.append(text)

# save formatted rows directly to analytical CSV SHEET
with open(output_path, "w") as out:
    out.write(f"Telemetry Data of {file_in} (distance in cm)\n")
    out.write("Timestamp_Sec,Player_X,Player_Y,Player_Z,Player_Yaw,Displacement\n")
    for row in clean_rows:
        if row[0].isdigit() or row.startswith("-"):
            out.write(row + "\n")

print(f"SUCCESS: File has been saved to {output_path}")
