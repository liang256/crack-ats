import os
import glob
import json
import services
import resume_generator

GENERATOR = resume_generator.ResumeGenerator()

with open("experience.json", "r") as file:
    EXPERIENCE = json.load(file)


def read_job_title(jd_file_path):
    with open(jd_file_path, "r") as file:
        job_title = file.readline().strip()

    job_title = job_title.replace(" ", "_")
    job_title = job_title.replace("(", "")
    job_title = job_title.replace(")", "")
    job_title = job_title.replace("|", "")
    return job_title.strip()


def parse_files():
    # Create the parsed_jds/ directory if it doesn't exist
    os.makedirs("parsed_jds", exist_ok=True)

    # Get the list of files in the src_jds/ directory
    file_list = glob.glob("parsed_jds/*.json")

    for file_path in file_list:
        # Get the file name without the directory path
        file_name = os.path.basename(file_path)

        # Output directory
        output_dir = os.path.join("generated_resumes", file_name.replace(".json", ""))

        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Create the output file path in the parsed_jds/ directory
        output_file_path = os.path.join(output_dir, "software_developer.txt")

        # if the output file already exists, skip this file
        if os.path.exists(output_file_path):
            continue

        # Read the contents of the file
        with open(file_path, "r") as f:
            required_skills = json.loads(f.read())

        # Parse the file content (replace this with your parsing logic)
        new_resume = services.generate_resume(EXPERIENCE, required_skills, GENERATOR)

        # Write the parsed content to the output file
        with open(output_file_path, "w") as output_file:
            output_file.write(new_resume)

        print(f"New resume '{file_name}' created and saved to '{output_file_path}'")


if __name__ == "__main__":
    parse_files()
