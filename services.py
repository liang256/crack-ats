from typing import Dict
import jd_parser
import resume_generator


def parse_jd(parser: jd_parser.AbstractJDParser, jd_str: str) -> Dict[str, int]:
    """
    Parses a job description string and returns a dictionary of keywords.

    Args:
        jd_str (str): The job description string to be parsed.

    Returns:
        Dict[str, int]: A dictionary containing the keywords found in the job description and their frequency.
    """
    return parser.parse(jd_str)


def generate_resume(
    experience: Dict[str, int],
    required_skills: Dict[str, int],
    generator: resume_generator.AbstractResumeGenerator,
) -> str:
    """
    Generates a resume based on the given skills and source experience.

    Args:
        skills (Dict[str, int]): A dictionary of skill keywords extracted from a job description and their frequency.
        src_experience (Dict[str, int]): A dictionary of the source experience.

    Returns:
        str: The generated resume text.
    """
    return generator.generate(experience, required_skills)
