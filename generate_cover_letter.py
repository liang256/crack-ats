import coverletter_generator
import argparse
import json
import os

GENERATOR = coverletter_generator.GPT4CoverLetterGenerator()

with open("experience.json", "r") as file:
    EXPERIENCE = json.load(file)

parser = argparse.ArgumentParser()
# add an argument to accept text length
parser.add_argument(
    "-l",
    "--length",
    type=int,
    default=2048,
    help="Minimum length of the cover letter",
)
parser.add_argument("file_path", nargs="?", help="Path to the job description file")
args = parser.parse_args()

if not args.file_path:
    print("Please provide the path to the job description file.")
    exit()

with open(args.file_path, "r") as file:
    job_description = file.read()
cover_letter = GENERATOR.generate(EXPERIENCE, job_description)
print(cover_letter)

# get current directory
curr_dir = os.getcwd()

dir = os.path.join(
    curr_dir,
    "generated_resumes",
    os.path.basename(args.file_path).replace(".txt", ""),
)

if not os.path.exists(dir):
    os.makedirs(dir)

output_path = os.path.join(dir, "cover_letter_{}.txt".format(args.length))

with open(output_path, "w") as output_file:
    output_file.write(cover_letter)
