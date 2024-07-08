import yaml
import glob
import os

# Delete all existing .sh files in the aliases directory
for filename in glob.glob('aliases/*.sh'):
    os.remove(filename)

# Load the YAML content from the file
with open('site/_data/aliases.yml', 'r') as file:
    data = yaml.safe_load(file)

# Iterate through each section
for section in data['sections']:
    section_name = section['section']
    # Create/open a file named <section_name>.sh in the aliases directory
    with open(f'aliases/{section_name.lower()}.sh', 'w') as script_file:
        # Iterate through each command in the section
        for command in section['commands']:
            # Write the alias command to the file
            script_file.write(f'alias {command["alias"]}="{command["name"]}"\n')


# Load the YAML file
with open('site/_data/aliases.yml', 'r') as file:
    data = yaml.safe_load(file)

# Ensure the output directory exists
output_dir = 'site'
os.makedirs(output_dir, exist_ok=True)

# Delete all .md files in the output directory except for index.md
for filename in os.listdir(output_dir):
    if filename.endswith('.md') and filename != 'index.md':
        os.remove(os.path.join(output_dir, filename))

# Iterate through each section
for section in data['sections']:
    section_name = section['section']
    # Replace spaces with underscores and make lowercase for the filename
    filename = f"{section_name.replace(' ', '_').lower()}.md"
    filepath = os.path.join(output_dir, filename)
    
    # Write to the Markdown file for this section
    with open(filepath, 'w') as md_file:
        md_file.write(f"---\ntitle: {section_name}\nlayout: home\n---\n\n")
        md_file.write(f"# {section_name}\n\n")
        
        for command in section['commands']:
            md_file.write(f"## {command['alias']} -> {command['name']}\n\n")
            md_file.write(f"{command['description']}\n\n")
            md_file.write(f"required parameters: {command['params']}\n\n")
            
print("Pages generated successfully.")