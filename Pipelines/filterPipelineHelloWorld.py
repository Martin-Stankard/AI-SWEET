"""
title: Filter Pipeline Helloworld
author: MPS
date: 2025-01-01
version: 1.1
license: MIT
description: Example of a filter pipeline that can be used to edit the form data before it is sent to the OpenAI API.
requirements: requests
"""

from typing import List, Optional
from pydantic import BaseModel
from schemas import OpenAIChatMessage


class Pipeline:
    class Valves(BaseModel):
        # List target pipeline ids (models) that this filter will be connected to.
        
        # If you want to connect this filter to all pipelines, you can set pipelines to ["*"] in next method
        pipelines: List[str] = []
        priority: int = 0 #lower the better, neg???

        # Add your custom parameters/configuration here e.g. API_KEY that you want user to configure etc.
        # this is all you see in the open web-ui>admin settings>pipelines AFTER you load this file as a pipeline.
        pass

    def __init__(self):
        # Pipeline filters are only compatible with Open WebUI
        # You can think of filter pipeline as a middleware that can be used to edit the form data before it is sent to the OpenAI API.
        self.type = "filter"
        
        # Optionally, you can set the id and name of the pipeline.
        # Best practice is to not specify the id so that it can be automatically inferred from the filename, so that users can install multiple versions of the same pipeline.
        # The identifier must be unique across all pipelines.
        # The identifier must be an alphanumeric string that can include underscores or hyphens. It cannot contain spaces, special characters, slashes, or backslashes.
        # self.id = "filter_pipeline" # YAY, big stupid descriptive file names instead of this id.
        self.name = "Filter"

        # TODO, understand why pipelines is being set here, and priority is not...maybe unnecessary if the pipelines is set above
        # official has self.valves = self.Valves(**{"pipelines": ["llama3:latest"]})
        self.valves = self.Valves(**{"pipelines": ["*"]})
        
        print(f"init:{__name__}")

        pass

    async def on_startup(self):
        # This function is called when the server is started.
        print(f"on_startup:{__name__}")
        pass

    async def on_shutdown(self):
        # This function is called when the server is stopped.
        print(f"on_shutdown:{__name__}")
        pass

    async def inlet(self, body: dict, user: Optional[dict] = None) -> dict:
        # This filter is applied to the form data BEFORE it is sent to the LLM API.
        print(f"inlet:{__name__}")

        # # If you'd like to check for title generation, you can add the following check
        # if body.get("title", False):
        #     print("Title Generation Request, inlet")

        # print(body)
        # print(user)

        return body
        
    async def outlet(self, body: dict, user: Optional[dict] = None) -> dict:
    	#This filter is applied to the form data AFTER it is sent to the LLM API.
        print(f"outlet:{__name__}")
        print(body)
        
        
        # if there is a body.messages and it is a list
        if 'messages' in body and isinstance(body['messages'], list):
            # foreach object, if there is a role == assistant
            for obj in body['messages']:
                if obj.get('role') == 'assistant':
                    # for that object, if there is "content" and it is a string
                    if 'content' in obj and isinstance(obj['content'], str):
                        # concat "some hello world junk" to the end of that content.
                        obj['content'] += " some hello world junk"
        
                        
        return body
        