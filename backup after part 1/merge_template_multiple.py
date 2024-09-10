import json
import os

# Define paths
template_file = "template.html"
client_data_dir = "clients"  # Directory containing all the client JSON files

# Output directory to save final merged files
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Function to read file content
def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# Read the template content
template_content = read_file(template_file)

# Loop through each client JSON file in the client_data_dir
for client_file in os.listdir(client_data_dir):
    if client_file.endswith(".json"):
        # Get the full path to the client JSON file
        client_file_path = os.path.join(client_data_dir, client_file)
        
        # Read the client-specific data from JSON
        with open(client_file_path, "r", encoding="utf-8") as f:
            client_data = json.load(f)
        
        # Replace the placeholders in the template with client-specific values
        final_content = template_content.format(**client_data)
        
        # Generate the output filename based on the client's loan number (or filename)
        output_file = f"final_{client_data['loan_number']}.html"
        output_file_path = os.path.join(output_dir, output_file)
        
        # Write the final content to the output file
        with open(output_file_path, "w", encoding="utf-8") as f:
            f.write(final_content)
        
        print(f"Generated final document: {output_file_path}")
        

import json
import os

# Define paths
template_file = "template.html"
client_data_dir = "clients"  # Directory containing all the client JSON files

# Output directory to save final merged files
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Function to read file content
def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# Read the template content
template_content = read_file(template_file)

# Loop through each client JSON file in the client_data_dir
for client_file in os.listdir(client_data_dir):
    if client_file.endswith(".json"):
        print(f"Processing {client_file}...")  # Added print statement
        
        # Get the full path to the client JSON file
        client_file_path = os.path.join(client_data_dir, client_file)
        
        # Read the client-specific data from JSON
        with open(client_file_path, "r", encoding="utf-8") as f:
            client_data = json.load(f)
        
        # Replace the placeholders in the template with client-specific values
        final_content = template_content.format(**client_data)
        
        # Generate the output filename based on the client's loan number (or filename)
        output_file = f"final_{client_data['loan_number']}.html"
        output_file_path = os.path.join(output_dir, output_file)
        
        # Write the final content to the output file
        with open(output_file_path, "w", encoding="utf-8") as f:
            f.write(final_content)
        
        print(f"Generated final document: {output_file_path}")  # Added print statement