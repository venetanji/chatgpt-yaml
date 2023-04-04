import yaml
from dotenv import load_dotenv
import urllib.request
import os
import openai
import logging
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
logging.basicConfig(filename="log.txt", level=logging.DEBUG)

class Template:

    def __init__(self, template="example"):
        self.config = yaml.safe_load(open(f'{template}.yaml','r'))
        self.completion = None

    def run(self):
        self.completion = openai.ChatCompletion.create(**config)
        logging.debug("Completion: "+ str(self.completion))
        return self.completion.choices[0]['message']['content']

template = Template()
print(template.run())
