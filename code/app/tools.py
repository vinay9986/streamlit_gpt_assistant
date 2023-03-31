import ast
import datetime
import calendar
import json
from dateutil.relativedelta import relativedelta
import logging as log

class ToolBox:
    MAT_period: list
    YTD_period: list
    prompt: str
    globals: dict
    locals: dict
    observation_map: dict
    logger = log.getLogger(__name__)

    def _monthInMMFormat(self, month):
        if month < 10:
            return '0' + str(month)
        return str(month)
    
    def _getYearMonth(self, year, month):
        return int(str(year) + self._monthInMMFormat(month))
    
    def _getMAT(self):
        #get current closed year and month
        current_year = datetime.datetime.now().year
        current_month = datetime.datetime.now().month
        current_date = datetime.datetime.now().date()
        last_day_of_month = calendar.monthrange(current_year, current_month)[1]
        if current_date.day < last_day_of_month:
            current_month -= 1
            if current_month == 0:
                current_month = 12
                current_year -= 1
        last_day_of_month = calendar.monthrange(current_year, current_month)[1]

        #go back 12 months
        current_date = datetime.date(current_year, current_month, last_day_of_month)
        start_date = current_date - relativedelta(months=11)
        return [self._getYearMonth(start_date.year, start_date.month), self._getYearMonth(current_date.year, current_date.month)]
    
    def _getYTD(self):
        #get current closed year and month
        current_year = datetime.datetime.now().year
        current_month = datetime.datetime.now().month
        current_date = datetime.datetime.now().date()
        last_day_of_month = calendar.monthrange(current_year, current_month)[1]
        if current_date.day < last_day_of_month:
            current_month -= 1
            if current_month == 0:
                current_month = 12
                current_year -= 1
        last_day_of_month = calendar.monthrange(current_year, current_month)[1]

        #go back 12 months
        current_date = datetime.date(current_year, current_month, last_day_of_month)
        start_date = datetime.date(current_year, 1, 1)
        return [self._getYearMonth(start_date.year, start_date.month), self._getYearMonth(current_date.year, current_date.month)]

    def __init__(self, globals=None, locals=None):
        self.MAT_period = self._getMAT()
        self.YTD_period = self._getYTD()
        self.globals = globals
        self.locals = locals
        self.observation_map = {}
        self.prompt = """
        Answer the following questions as best you can.
        You are working with a pandas dataframe in Python.
        Create an efficient summary and analysis of a pandas DataFrame in Python, focusing on generating reports and aggregations.
        Kindly refrain from answering unrelated questions. 
        Provide aggregation results as the final answer where applicable.
        You have 3 dataframes: df_customers, df_sales, df_alignments. df_customers has 11 columns ('NARC', 'NAME', 'Parent_NARC', 'Parent_NAME', 'Address', 'City', 'State', 'Zip', 'Partner', 'Spec_Desc', 'ZFS') NARC is primary key of type String. df_sales has 6 columns ('NARC', 'YearMonth', 'ProdID', 'ItemID', 'Units', 'Sales') NARC is the foreign key of type string. df_sales have monthly sales per NARC, per ProdID, per ItemID, the relation between NARC, ProdID, and ItemID is 1:M:M. df_alignments has 11 columns ('NARC', 'SalesForce_ID', 'Region_ID', 'Region_Name', 'Region_Manager', 'Area_ID', 'Area_Name', 'Area_Manager', 'Territory_ID', 'Territory_Name', 'Territory_Manager') NARC and SalesForce_ID forms composite primary key, they are of type string. When you get customers by salesforce id always make sure their territory id does not contain '99' in it.
        You should use the tools below to answer the question posed of you:
            get_mat_period: Returns array containing start and end period in YYYYMM format
            get_ytd_period: Returns array containing start and end period in YYYYMM format
            exe_py_cmd: A Python shell. Use this to execute python commands. Input should be a valid python command. When using this tool, sometimes output is abbreviated - make sure it does not look abbreviated before using it in your answer.

        Use the following json format:
            Question: the input question you must answer
            {
                "action_plan": [
                    {
                        "Thought": "you should always think about what to do",
                        "Action": "the action to take, should be one of [get_mat_period, get_ytd_period, exe_py_cmd]",
                        "Action_Input": "the input to the action",
                        "Observation": "the result of the action"
                    }
                ]
            }
            
            ... (this Thought/Action/Action Input/Observation can repeat N times)

            If the question is to generate a report, then
            {
                "Thought": "I now have the final report, merge with df_customers and export it to a csv file",
                "Action": "exe_py_cmd",
                "Action_Input": "pd.merge(df_result_WIP, df_customers, on='NARC', how='left').to_csv('result.csv', index=False)",
                "Observation": "output of the action",
                "Final_Answer": "'result.csv' contains all data to the original input question"
            }
            else
            {
                "Thought": "I now know the final answer",
                "Final_Answer": "the final answer to the original input question"
            }

        DO NOT make up an answer. Only answer based on the information you have. ALWAYS RERUN ACTION AND UPDATE OBSERVATION

        Following examples are strickly for reference only. DO NOT copy paste the examples.

            Question: What is the total MAT sales for customer N767?
            {
                "action_plan":
                [
                    {
                        "Thought": "I need to get the MAT period and then get the sales for customer N767",
                        "Action": "get_mat_period",
                        "Action_Input": "",
                        "Observation": [202103, 202202]
                    },
                    {
                        "Thought": "I need to get the sales for customer N767 over MAT period and aggregate Sales column to get final answer",
                        "Action": "exe_py_cmd",
                        "Action_Input": "df_sales[(df_sales['NARC'] == 'N767') & (df_sales['YearMonth'] >= 202103) & (df_sales['YearMonth'] <= 202202)]['Sales'].sum()",
                        "Observation": 1000
                    },
                    {
                        "Thought": "I now know the final answer",
                        "Final_Answer": "MAT sales for customer 'N767' is $1000"
                    }
                ]
            }

            Question: Generate a report containing monthly sales of all customers serviced by SalesForce ID N898 over YTD period for product P090 ?
            {
                "action_plan":
                [
                    {
                        "Thought": "I need to get the YTD period and then get the customers serviced by SalesForce ID N898 and the get monthly sales for filtered customers within MAT period for product P090",
                        "Action": "get_ytd_period",
                        "Action_Input": "",
                        "Observation": [202103, 202202]
                    },
                    {
                        "Thought": "I need to get the customers serviced by SalesForce ID N898, Territory ID does not contain '99' and save the result in customer variable",
                        "Action": "exe_py_cmd",
                        "Action_Input": "customers = df_alignments[(df_alignments['SalesForce_ID'] == 'N898') & (df_alignments['Territory_ID'].str.contains('99') == False)].NARC.unique()",
                        "Observation": ""
                    },
                    {
                        "Thought": "I need to get all sales for selected customers within YTD period who has bought product P090 and save the result in a df_result_WIP dataframe",
                        "Action": "exe_py_cmd",
                        "Action_Input": "df_result_WIP = df_sales[(df_sales['NARC'].isin(customers)) & (df_sales['YearMonth'] >= 202103) & (df_sales['YearMonth'] <= 202202) & (df_sales['ProdID'] == 'P090')]",
                        "Observation": ""
                    },
                    {
                        "Thought": "I need to group by 'NARC', 'YearMonth' and aggregate 'Sales' to get monthly sales for each customer by product",
                        "Action": "exe_py_cmd",
                        "Action_Input": "df_result_WIP = df_result_WIP.groupby(['NARC', 'YearMonth'])['Sales'].sum().reset_index()",
                        "Observation": ""
                    },
                    {
                        "Thought": "I now have the final report, merge with df_customer and export it to a csv file",
                        "Action": "exe_py_cmd",
                        "Action_Input": "pd.merge(df_result_WIP, df_customers, on='NARC', how='left').to_csv('result.csv', index=False)",
                        "Observation": "",
                        "Final_Answer": "'result.csv' contains all data to the original input question"
                    }
                ]
            }

        Begin!

        Question: {input}
        """

    def _run(self, query:str):
        try:
            tree = ast.parse(query)
            module = ast.Module(tree.body[:-1], type_ignores=[])
            exec(ast.unparse(module), self.globals, self.locals)  # type: ignore
            module_end = ast.Module(tree.body[-1:], type_ignores=[])
            module_end_str = ast.unparse(module_end)  # type: ignore
            try:
                output = eval(module_end_str, self.globals, self.locals)
            except Exception:
                output = exec(module_end_str, self.globals, self.locals)
        except Exception as e:
            output = str(e)
        return output

    def _runAction(self, action, action_input):
        if action == "get_mat_period":
            return self.MAT_period
        if action == "get_ytd_period":
            return self.YTD_period
        if action == "exe_py_cmd" and action_input:
            output = self._run(action_input)
            return list(output) if isinstance(output, list) else output

    def _isvalid(self, value):
        if value is None or value == "":
            return False
        return True

    def _update_observation_map(self, madeup_observations, actual_observations):
        if self._isvalid(madeup_observations):
            if isinstance(madeup_observations, list):
                for index, madeup_observation in enumerate(madeup_observations):
                    self.observation_map[madeup_observation] = actual_observations[index] if isinstance(actual_observations, list) else None
            else:
                self.observation_map[madeup_observations] = actual_observations if actual_observations is not None else None

    def execute_plan(self, action_plan: json):
        for step in action_plan:
            keys = self.observation_map.keys()
            madeup_observations = step.get("Observation", None)
            action = step.get("Action", "")
            action_input = step.get("Action_Input", "")
            final_answer = step.get("Final_Answer", "")
            if len(keys) > 0:
                for key in keys:
                    if str(key) in action_input:
                        action_input = action_input.replace(str(key), str(self.observation_map.get(key, None)))
                    elif str(key) in final_answer:
                        final_answer = final_answer.replace(str(key), str(self.observation_map.get(key, None)))
            if self._isvalid(action):
                observations = self._runAction(action, action_input)
                self.logger.info(f"Action: {action}")
                self.logger.info(f"Action Input: {action_input}")
                self.logger.info(f"Madeup Observations: {madeup_observations}")
                self.logger.info(f"Actual Observations: {observations}")
                self.logger.info(f"observation_map: {json.dumps(self.observation_map, indent=4)}")
                self._update_observation_map(madeup_observations, observations)
        return final_answer
