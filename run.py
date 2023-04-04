import yaml
from dotenv import load_dotenv
import urllib.request
import os
import openai
import logging
import argparse
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
logging.basicConfig(filename="log.txt", level=logging.DEBUG)

parser.add_argument('--template','-t', type=str, default="example")
parser.add_argument('--outfile','-o', type=str, default="output.txt")


class Template:

    def __init__(self, template="example"):
        self.config = yaml.safe_load(open(f'{template}.yaml','r'))
        self.completion = None

    def run(self):
        self.completion = openai.ChatCompletion.create(**config)
        logging.debug("Completion: "+ str(self.completion))
        return self.completion.choices[0]['message']['content']

def __main__():
    print("Running ChatGpt Yaml")
    args = parser.parse_args()
    template = Template(args.template)
    output = template.run()
    print(output)
    # write output to file
    with open(args.outfile, 'w') as f:
        f.write(output)

if __name__ == "__main__":
    __main__()
