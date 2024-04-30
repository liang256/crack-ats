# crack-ats

crack-ats is an application designed to generate resumes that are optimized to beat Applicant Tracking Systems (ATS). 

## Features

- Generate ATS-friendly resumes
- Customize resume templates
- Export resumes in various formats
- Generate cover letter

## Installation

To install crack-ats, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/crack-ats.git`
2. Navigate to the project directory: `cd crack-ats`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage

To use crack-ats, run the following command:


## Usage

To use crack-ats, follow these steps:

1. Parse job descriptions from `src_jds/`:
    ```bash
    make parse
    ```

2. Generate resumes based on parsed job descriptions and `experience.json`:
    ```bash
    make generate
    ```

3. Convert generated resumes to PDF:
    ```bash
    make pdf
    ```

4. Generate cover letter based on given job description and `experience.json`:
    ```bash
    make cl /path/to/the/job-description
    ```
