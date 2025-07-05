import langchain
from langchain_community.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
import os


os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
llm = GoogleGenerativeAI(model="gemini-2.0-flash")

def summary_generator(URL):
    loader = YoutubeLoader.from_youtube_url(youtube_url=URL, add_video_info=False)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=4000,
        chunk_overlap=200
    )

    split_docs = text_splitter.split_documents(docs)

    prompt_template = PromptTemplate.from_template(
        """
    You are an expert in Summarizing the transcription of youtube videos.

    You will be given the transcription of a youtube video which is splitted into different chunks with a bit of overall using the langchain text_splitter module.

    Your job is to give me a summary of this what happened in the video by sequentially going through the chunks of data given to you.

    Make sure the summary:
    - Covers important topics mentioned in the video.
    - Is crisp but detailed and easy to understand.

    This is the data : {data}

    The ouput should be only text. Don't generate anything other than text.
    """
    )

    prompt = prompt_template.format(data=split_docs)
    response = llm.invoke(prompt)
    return response
