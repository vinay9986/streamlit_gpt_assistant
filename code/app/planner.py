import pandas as pd
import openai
import json
from tools import ToolBox
from base_data import BaseData

class Planner:
    data: BaseData
    tools: ToolBox
    
    def __init__(self, api_key: str):
        self.data = BaseData()
        self.tools = ToolBox(locals={"df_customers": self.data.customers, "df_sales": self.data.sales, "df_alignments": self.data.alignments, "pd": pd})
        openai.api_key = api_key

    def generate_report(self, query: str) -> str:
        prompt = self.tools.prompt.replace("{input}", query)
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [{"role": "system", "content": prompt}],
            temperature = 0
        )
        json_response = json.loads(response['choices'][0]['message']['content'])
        return self.tools.execute_plan(json_response.get('action_plan'))