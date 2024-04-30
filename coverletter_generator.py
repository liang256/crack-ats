import openai_client
import datetime
import json


class CoverLetterGenerator:
    def generate(self, skills: dict) -> str:
        raise NotImplementedError


INSTRUCTIONS = """
You will be provided with a job description and a dictionary of the my experience.
Your task is to generate a cover letter based on the job description and my experience.
####
steps:
1. analyze the job description to find out 3 important key quaility that the employer is looking for.
2. make stories from my experience that match the 3 key quality.
3. write a cover letter that tells the stories and how my experience match the 3 key quality.
there should be a strong connection between the stories and the key quality.
there should be 4 paragraphs in the cover letter.
the first paragraph is the introduction, the second, third are the stories, and the last is the conclusion.
the cover letter should be strong and natural, not like AI generated.
the length should be at least {} characters.
4. return the cover letter as a string without any other unrelated information.
"""


class GPTCoverLetterGenerator(CoverLetterGenerator):
    def __init__(self, model) -> None:
        self.client = openai_client.get_client()
        self.model = model

    def generate(self, experience: dict, jd: str, length: int = 2048) -> str:
        message = json.dumps({"experience": experience, "job_description": jd})
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": INSTRUCTIONS.format(length)},
                {"role": "user", "content": message},
            ],
            temperature=1,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        # Log the response to a log file
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("openai.log", "a") as log_file:
            log_file.write(f"Sent message: {message}\n")
            log_file.write(f"Sent time: {current_time}\n")
            log_file.write(f"Response: {response.choices[0].message.content}\n")
        return response.choices[0].message.content


class GPT3TurboCoverLetterGenerator(GPTCoverLetterGenerator):
    def __init__(self):
        super().__init__("gpt-3.5-turbo")


class GPT4CoverLetterGenerator(GPTCoverLetterGenerator):
    def __init__(self):
        super().__init__("gpt-4")
