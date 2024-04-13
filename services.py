from typing import Dict
import jd_parser


def parse_jd(parser: jd_parser.AbstractJDParser, jd_str: str) -> Dict[str, int]:
    """
    Parses a job description string and returns a dictionary of keywords.

    Args:
        jd_str (str): The job description string to be parsed.

    Returns:
        Dict[str, int]: A dictionary containing the keywords found in the job description and their frequency.
    """
    return parser.parse(jd_str)
