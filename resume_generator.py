import openai_client
import datetime
import json


class AbstractResumeGenerator:
    def generate(self, skills: dict) -> str:
        raise NotImplementedError


INSTRUCTIONS = """
You will be provided with a dictionary of required skills extracted from a job description and a dictionary of the source experience. Your task is to generate a resume based on the given skills and experience. 
- paragraph: base info, working experience, education, skills
- You should create strong experiences that matched to the required skills. 
- Rewrite some experience to enhance the strength if you think needed
- use bullet points
- at least 80 percent of required skills be used in the resume. 
- at least 2048 characters totally. 
- Pick the best title for each working experience
- Consider you are a HR and ensure the result resume is strong and nature and not like AI generated.
Return only the result resume as a string.
"""


class ResumeGenerator(AbstractResumeGenerator):
    def __init__(self) -> None:
        self.client = openai_client.get_client()

    def generate(self, experience: dict, required_skills: dict) -> str:
        message = json.dumps(
            {"experience": experience, "required_skills": required_skills}
        )
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": INSTRUCTIONS},
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
