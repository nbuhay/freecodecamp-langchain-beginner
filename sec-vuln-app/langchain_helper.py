from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

def gen_vulnerabilitiy_fix(vulnerability: str) -> str:
    # prompt is a list of List[Tuple(role, content)]
    #   role describes who is saying something
    #   content describes what was said
    # https://python.langchain.com/docs/modules/model_io/concepts#messages
    sec_vuln_prompt = \
'''
Writing Prompt: Cybersecurity Expert Assistance

You are a cybersecurity expert tasked with providing recommendations to a developer who has identified a specific security vulnerability. Your goal is to guide the developer in fixing the vulnerability while adhering to security best practices. Please generate a response that includes:

Description: Clearly describe the identified security vulnerability, explaining its nature and potential risks.

Considerations: Provide comprehensive considerations for addressing the vulnerability. Include relevant security best practices that the developer should follow to ensure a robust fix.

Working Code: Present a sample or template of working code that demonstrates how the developer can implement the recommended fix. The code should be concise, easy to understand, and showcase security-conscious programming practices.
'''
    prompt = ChatPromptTemplate.from_messages([
        ("system", sec_vuln_prompt),
        ("user", "The identified vulnerability I need to fix is {input}.")
    ])

    # temp is like a creativity slider
    #   0 for least creative, most accurate
    #   1 for most creative, but less accurate
    llm = ChatOpenAI(temperature = 0.7)

    # final output of chain is a string
    output_parser = StrOutputParser()
    
    # setup prompt chain - like Linux pipes
    chain = prompt | llm | output_parser
    
    # invoke executes chain, passing in vulnerability
    #   'input' is inserted into the prompt
    return chain.invoke({"input": vulnerability})

if __name__ == "__main__":
    # heartbleed - https://heartbleed.com/
    # log4j - https://www.cisa.gov/news-events/news/apache-log4j-vulnerability-guidance
    famous_vulnerabilities = [
        "CVE-2014-0160", # heartbleed
        "CVE-2021-44228" # log4J 
    ]
    for i, vulnerability in enumerate(famous_vulnerabilities):
        print('{}: Name: {}'.format(i, vulnerability))
        print(gen_vulnerabilitiy_fix(vulnerability))