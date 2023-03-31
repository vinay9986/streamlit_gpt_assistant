import streamlit as st
import openai
from streamlit_chat import message
from planner import Planner

openai.api_key = st.secrets['OPENAI_API_KEY']
planner = Planner(st.secrets['OPENAI_API_KEY'])

def update_messages(role, text):
    st.session_state.messages.append({"role": role, "content": text})

def generate_response(user_input):
    update_messages("user", user_input)
    if user_input.startswith("Q:"):
        user_input = user_input[2:].strip()
        output = planner.generate_report(user_input)
        update_messages("assistant", output)
        if 'result.csv' in output:
            with open('/Users/pazuzu/workDock/result.csv') as f:
                st.download_button(
                    label="Download report",
                    data=f,
                    file_name="result.csv",
                    mime="text/csv",
                )
        return output
    else:
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = st.session_state.messages,
            temperature = 0,
        )
        return_text = response['choices'][0]['message']['content']
        update_messages("assistant", return_text)
        return return_text

def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text

def initiate_content():
    messages = [
                {"role": "system", "content": "You are helpful database describer. You cannot tell jokes or socialize."},
                {"role": "system", "content": "Kindly refrain from answering unrelated questions."},
                {"role": "system", "content": "MAT stands for Moving Annual Total. It is the sum of the last 12 completed months of sales."},
                {"role": "system", "content": "YTD stands for Year To Date. It is the sum of all sales from the beginning of the year till latest closed month."},
                {"role": "system", "content": """You are aware of 3 tables: Customers, Sales, Alignments. Customers table has 11 columns ('NARC', 'NAME', 'Parent_NARC', 'Parent_NAME', 'Address', 'City', 'State', 'Zip', 'Partner', 'Spec_Desc', 'ZFS') NARC is primary key of type String. Sales has 6 columns ('NARC', 'YearMonth', 'ProdID', 'ItemID', 'Units', 'Sales') NARC is the foreign key of type string. Sales has monthly sales by NARC, by ProdID, by ItemID, the relation between NARC, ProdID, and ItemID is 1:M:M. Alignments has 11 columns ('NARC', 'SalesForce_ID', 'Region_ID', 'Region_Name', 'Region_Manager', 'Area_ID', 'Area_Name', 'Area_Manager', 'Territory_ID', 'Territory_Name', 'Territory_Manager') NARC and SalesForce_ID forms composite primary key, they are of type string."""}
            ]
    return messages

st.title("BA assistant")
st.sidebar.header("Instructions")
st.sidebar.info('''
    This assistant will help you generate your daily reports. You specify your request and the assistant will generate a report for you.
    Always start your report/analysis request with 'Q:', not required for other questions.
    Being specific is the key to success.

    The bot is aware of the following reports:
    1. Sales report
    2. Alignment report
    3. Target list and Execlusion list

    Few example requests:
    1. 'Q: Generate MAT sales report per customer for 'Apoquel' by SalesForce '100' and the report must contain the following details: YearMonth, NARC, Parent, Name, Address, City, State, Zip, product, territory, NetAmnt'
    2. 'Q: Generate YTD sales report per customer by month for 'Biologicals' therapeutic and the report must contain the following details: YearMonth, NARC, Parent, Name, Address, City, State, Zip, product, NetAmnt, NetUnits, Sales'

    General questions:
    1. 'What is MAT?'
    2. 'What data is available?'
    3. 'Describe customers table?'
''')

#storing the chat
if 'generated' not in st.session_state:
    st.session_state.generated = []

if 'past' not in st.session_state:
    st.session_state.past = []

if 'messages' not in st.session_state:
    st.session_state.messages = initiate_content()

user_input = get_text()
if user_input:
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.button('Clear chat'):
    st.session_state.generated = []
    st.session_state.past = []
    st.session_state.messages = initiate_content()
    del(message)

if st.session_state.generated:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
