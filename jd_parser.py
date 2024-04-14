from typing import List, Tuple
import json
import openai_client
import datetime


class AbstractJDParser:
    def parse(self, jd_str: str) -> List[Tuple[str, str, int]]:
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


class JDParser(AbstractJDParser):
    def __init__(self) -> None:
        self.client = openai_client.get_client()

    def parse(self, jd_str: str):
        json_key_words = self.ask_gpt(jd_str)
        try:
            return json.loads(json_key_words)
        except json.decoder.JSONDecodeError:
            json_key_words += "}"
            return json.loads(json_key_words)

    def ask_gpt(self, content: str):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = {"role": "user", "content": content}
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": 'You will be provided with a text of job description, and your task is to extract a list of hard skill" keywords and their frequency from it. The keywords should be sorted by word frequency. The output is JSON. example output: {"skill":freq,"skill":freq"}',
                },
                message,
            ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        # Log the response to a log file
        with open("openai.log", "a") as log_file:
            log_file.write(f"Sent message: {message}\n")
            log_file.write(f"Sent time: {current_time}\n")
            log_file.write(f"Response: {response.choices[0].message.content}\n")
        return response.choices[0].message.content
