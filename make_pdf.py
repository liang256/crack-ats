from fpdf import FPDF
import os
import argparse


def convert_to_pdf(input_file, output_file):
    pdf = FPDF()
    pdf.add_page()

    with open(input_file, "r") as file:
        text = file.read()

    pdf.set_font("Arial", size=12)
    pdf.multi_cell(
        0, 5, text
    )  # Adjust the ln parameter to reduce spacing between lines

    pdf.output(output_file)
    print(f"Converted '{input_file}' to PDF and saved to '{output_file}'")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--force", action="store_true", help="Regenerate all existing PDFs"
    )
    parser.add_argument(
        "-a", "--all", action="store_true", help="Convert all source files"
    )
    parser.add_argument("file_path", nargs="?", help="Path to the input file")
    args = parser.parse_args()

    # iterate over the directories in the generated_resumes directory
    if args.all:
        for root, dirs, files in os.walk("generated_resumes"):
            for file in files:
                if file.endswith(".txt"):
                    input_file = os.path.join(root, file)
                    output_file = os.path.join(root, file.replace(".txt", ".pdf"))

                    if not args.force and os.path.exists(output_file):
                        continue
                    convert_to_pdf(input_file, output_file)
        return

    # takes a single file after command as input
    if args.file_path:
        input_file = args.file_path
        output_file = input_file.replace(".txt", ".pdf")
        convert_to_pdf(input_file, output_file)
    else:
        print("No input file specified.")


if __name__ == "__main__":
    main()
