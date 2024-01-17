from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

def gen_orchestral_arrangement(song_name: str) -> str:
    # prompt is a list of List[Tuple(role, content)]
    #   role describes who is saying something
    #   content describes what was said
    # https://python.langchain.com/docs/modules/model_io/concepts#messages
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a world class musician."),
        ("user", "What chords are in the song {input}")
    ])

    # temp is like a creativity slider
    #   0 for least creative, most accurate
    #   1 for most creative, but less accurate
    llm = ChatOpenAI(temperature = 0.7)

    # final output of chain is a string
    output_parser = StrOutputParser()
    
    # setup prompt chain - like Linux pipes
    chain = prompt | llm | output_parser
    
    # invoke executes chain, passing in song_name
    #   'input' is inserted into the prompt
    return chain.invoke({"input": song_name})

if __name__ == "__main__":
    song_names = [
        "It Won't Be Long",
        "Songs for the Deaf",
        "Is This It?" 
    ]
    for i, song in enumerate(song_names):
        print('{}: Name: {}'.format(i, song))
        print(gen_orchestral_arrangement(song))