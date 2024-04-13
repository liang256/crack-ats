import os
import glob
import json
import services
import jd_parser

PARSER = jd_parser.JDParser()


def parse_files():
    # Create the parsed_jds/ directory if it doesn't exist
    os.makedirs("parsed_jds", exist_ok=True)

    # Get the list of files in the src_jds/ directory
    file_list = glob.glob("src_jds/*.txt")

    for file_path in file_list:
        # Get the file name without the directory path
        file_name = os.path.basename(file_path)

        # Create the output file path in the parsed_jds/ directory
        output_file_path = os.path.join(
            "parsed_jds", file_name.replace(".txt", ".json")
        )

        # if the output file already exists, skip this file
        if os.path.exists(output_file_path):
            continue

        # Read the contents of the file
        with open(file_path, "r") as file:
            content = file.read()

        # Parse the file content (replace this with your parsing logic)
        parsed_content = services.parse_jd(PARSER, content)

        # Write the parsed content to the output file
        with open(output_file_path, "w") as output_file:
            output_file.write(json.dumps(parsed_content))

        print(f"File '{file_name}' parsed and saved to '{output_file_path}'")


if __name__ == "__main__":
    parse_files()
