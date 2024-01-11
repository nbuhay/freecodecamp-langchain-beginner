from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name() -> str:
    llm = ChatOpenAI(temperature = 0.7)
    prompt = "I have a dog pet and I want a cool name for it. Suggest me five cool names for my pet."
    name = llm.invoke(prompt)
    return name.content

if __name__ == "__main__":
    num_names = 5
    for i in range(num_names):
        print('Request {}'.format(i))
        print(generate_pet_name())