from langchain.llms import OpenAI
llm = OpenAI(moedl_name="gpt-3.5-turbo", open_api_key="YOUR_API_KEY")
response = llm("Tell ME A JOKE")
print(response)