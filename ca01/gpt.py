'''
Demo code for interacting with GPT-3 in Python.

To run this you need to 
* first visit openai.com and get an APIkey, 
* which you export into the environment as shown in the shell code below.
* next create a folder and put this file in the folder as gpt.py
* finally run the following commands in that folder

On Mac
% pip3 install openai
% export APIKEY="......."  # in bash
% python3 gpt.py

On Windows:
% pip install openai
% $env:APIKEY="....." # in powershell
% python gpt.py
'''
from mistune import markdown
import openai


class GPT():
    ''' make queries to gpt from a given API '''
    def __init__(self,apikey):
        ''' store the apikey in an instance variable '''
        self.apikey=apikey
        # Set up the OpenAI API client
        openai.api_key = apikey #os.environ.get('APIKEY')

        # Set up the model and prompt
        self.model_engine = "text-davinci-003"

    def getResponse(self,prompt):
        ''' Generate a GPT response '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response
    
    # Trista's demo
    def tristaDemo(self, birthday):
        full_prompt = f"What happened on the month and day of {birthday} in history, response the event only happend before 2020? "
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=full_prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )
        response = completion.choices[0].text
        return response
    def trista_catImage(self):
        full_prompt = f"Send me just a photo of a cute cat, write it in Markdown without backticks and without using a code block. Use the Unsplash API (https://source.unsplash.com/1600x900/?<PUT YOUR QUERY HERE>). Your response will only contain the image, do not mention Unsplash in your response, do not contain any '.' "
        catPhoto = openai.Completion.create(
            engine=self.model_engine,
            prompt=full_prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )
        #get the markdown
        markdown_text = catPhoto.choices[0].text
        response = markdown(markdown_text)
        return response
    
    #Ran's demo
    def ranDemo(self, birthday, birthtime, birthlocation):
        full_prompt = f"Do a detailed BaZi fortun telling for a person born on {birthday} {birthtime} at {birthlocation}. "
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=full_prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )
        response = completion.choices[0].text
        return response

if __name__=='__main__':
    '''
    '''
    import os
    g = GPT(os.environ.get("APIKEY"))
    print(g.getResponse("what does openai's GPT stand for?"))
    