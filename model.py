from typing import List, Tuple


class AbstractJDParser:
    def parse(jd_str: str) -> List[Tuple[str, str, int]]:
        """
        Parses a job description string and returns a list of keywords.

        Args:
            jd_str (str): The job description string to be parsed.

        Returns:
            List[Tuple[str, str, int]]: A list of tuples containing the keywords found in the job description.
                Each tuple consists of three elements: the keyword itself, the category it belongs to, and its frequency.

        Raises:
            NotImplementedError: This function is not implemented yet.
        """
        raise NotImplementedError
