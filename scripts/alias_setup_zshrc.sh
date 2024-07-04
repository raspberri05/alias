# Define the content to add to ~/.zshrc
content='for file in $HOME/alias/aliases/*.sh; do
    if [ -r "$file" ]; then
        source "$file"
    fi
done'

# Check if ~/.zshrc exists and is writable
zshrc_file="$HOME/.zshrc"
if [ -f "$zshrc_file" ] && [ -w "$zshrc_file" ]; then
    # Add the content to the top of ~/.zshrc
    temp_file=$(mktemp)
    echo "$content" | cat - "$zshrc_file" > "$temp_file" && mv "$temp_file" "$zshrc_file"
    echo "Updated $zshrc_file successfully."
else
    echo "Error: $zshrc_file does not exist or is not writable."
    exit 1
fi
