import os

# Define paths for boilerplate and client files
boiler1_path = "Boiler1.html"
boiler2_path = "Boiler2.html"
client_files = ["Client1A.html", "Client1B.html"]

# Output directory to save final merged files
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Function to read file content
def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# Read Boiler1 and Boiler2
boiler1_content = read_file(boiler1_path)
boiler2_content = read_file(boiler2_path)

# Loop through each client file and merge it with Boiler1 and Boiler2
for client_file in client_files:
    client_content = read_file(client_file)
    
    # Create final merged content
    final_content = boiler1_content + "\n" + client_content + "\n" + boiler2_content
    
    # Define the output file path
    output_file_path = os.path.join(output_dir, f"final_{client_file}")
    
    # Write the merged content to the output file
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(final_content)
    
    print(f"Generated final document for {client_file} at {output_file_path}")