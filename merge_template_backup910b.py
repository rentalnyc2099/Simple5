import json
import os
from jinja2 import Environment, FileSystemLoader

# Define paths
template_dir = os.getcwd()  # Current directory where the template is located
template_file = "cx36_template.html"
client_data_dir = "clients"
output_dir = "output"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader(template_dir))

# Function to generate the final document
def generate_document(template, client_data, output_file_path):
    # Ensure company_name exists in client data
    if 'company_name' not in client_data:
        raise ValueError(f"Missing 'company_name' field for client: {client_data['loan_number']}")
    
    print("Processing client data:", client_data)  # Debugging print
    
    # Render the template with client data
    final_content = template.render(client_data)i
    
    # Debug: Print the generated content to check if it looks correct
    print("Generated content:\n", final_content)  # Debugging print

    # Write the final document
    print(f"Writing final document to: {output_file_path}")  # Debugging print
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(final_content)
    print(f"Generated: {output_file_path}")

# Load the Jinja2 template
template = env.get_template(template_file)

# Loop through all client JSON files
for client_file in os.listdir(client_data_dir):
    if client_file.endswith(".json"):
        client_file_path = os.path.join(client_data_dir, client_file)
        
        # Print the client file being processed
        print(f"Processing client file: {client_file}")  # Debugging print
        
        # Read the client-specific data
        with open(client_file_path, "r", encoding="utf-8") as f:
            client_data = json.load(f)
        
        # Check if company_name exists in the client data
        if 'company_name' not in client_data:
            print(f"Warning: 'company_name' not found for {client_file}. Skipping.")
            continue
        
        # Generate output filename
        output_file = f"final_{client_data['loan_number']}.html"
        output_file_path = os.path.join(output_dir, output_file)
        
        # Generate the document
        generate_document(template, client_data, output_file_path)

print("Script execution completed.")
