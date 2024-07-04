import yaml
import glob
import os

# Delete all existing .sh files in the aliases directory
for filename in glob.glob('../aliases/*.sh'):
    os.remove(filename)

# Load the YAML content from the file
with open('../site/aliases.yml', 'r') as file:
    data = yaml.safe_load(file)

# Iterate through each section
for section in data['sections']:
    section_name = section['section']
    # Create/open a file named <section_name>.sh in the aliases directory
    with open(f'../aliases/{section_name}.sh', 'w') as script_file:
        # Iterate through each command in the section
        for command in section['commands']:
            # Write the alias command to the file
            script_file.write(f'alias {command["alias"]}="{command["name"]}"\n')