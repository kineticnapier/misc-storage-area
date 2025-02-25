def replace_strings_in_file(file_path, replacements, encode='utf-8'):
    """
    Reads a file, replaces specified strings, and writes back to the same file.
    
    :param file_path: Path to the file.
    :param replacements: Dictionary where keys are target strings and values are replacement strings.
    :param encode: Encoding to use when reading and writing files. Default is UTF-8.
    """

    # example usage
    #
    # file_path = "test.txt"
    # replacements = {
    #     "old_string": "new_string",
    #     "another_old_string": "another_new_string"
    # }
    # replace_strings_in_file(file_path, replacements)

    try:
        # Read the file content
        with open(file_path, 'r', encoding=encode) as file:
            content = file.read()
        
        # Perform the replacements
        for old, new in replacements.items():
            content = content.replace(old, new)
        
        # Write the modified content back to the file
        with open(file_path, 'w', encoding=encode) as file:
            file.write(content)
        
        print(f"Replacements completed successfully in {file_path}")
    except Exception as e:
        print(f"Error processing file: {e}")