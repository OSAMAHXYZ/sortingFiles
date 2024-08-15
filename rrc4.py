import os
import shutil

# Define the path to the directory you want to organize
directory = "E:\sendi backup\sendi downloads"


# Define the subdirectories for different file types
pdf_folder = os.path.join(directory, "PDFs")
excel_folder = os.path.join(directory, "Excel")
other_folder = os.path.join(directory, "Others")

# Create the folders if they don't exist
os.makedirs(pdf_folder, exist_ok=True)
os.makedirs(excel_folder, exist_ok=True)
os.makedirs(other_folder, exist_ok=True)

# Loop through all the files in the directory
for filename in os.listdir(directory):
    # Skip directories
    if os.path.isdir(os.path.join(directory, filename)):
        continue

    # Check the file extension and move the file to the corresponding folder
    if filename.lower().endswith(".pdf"):
        shutil.move(os.path.join(directory, filename), os.path.join(pdf_folder, filename))
    elif filename.lower().endswith((".xls", ".xlsx")):
        shutil.move(os.path.join(directory, filename), os.path.join(excel_folder, filename))
    else:
        shutil.move(os.path.join(directory, filename), os.path.join(other_folder, filename))

print("Files have been organized.")


