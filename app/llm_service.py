import os

from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI

from app.models import PersonInfo, Recommendation

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")


class LLMService:
    def __init__(self):
        self.llm = GoogleGenerativeAI(model="gemini-2.5-flash", api_key=google_api_key)
        self.parser = PydanticOutputParser(pydantic_object=Recommendation)
        self.prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are an AI medical assistant specialized in initial patient triage. "
                    "Given the patient's information, recommend the single most suitable medical department for their initial consultation. "
                    "You must respond in valid JSON format as specified in the format instructions. "
                    "If user provide invalid symptoms, you must return 'Invalid symptoms' in the response."
                    "Consider symptoms invalid if they are:\n"
                    "- Non-medical text or random text\n"
                    "- Empty or missing symptom\n"
                    "- Clearly not health-related concerns\n"
                    "{format_instruction}",
                ),
                (
                    "human",
                    "Patient Info:\n"
                    "Gender: {gender}\n"
                    "Age: {age}\n"
                    "Symptoms: {symptoms}\n\n"
                    "Please provide your recommendation in the required JSON format:",
                ),
            ]
        ).partial(format_instruction=self.parser.get_format_instructions())

        self.chain = self.prompt | self.llm | self.parser

    async def recommend_department(self, person_info: PersonInfo) -> Recommendation:
        try:
            result = await self.chain.ainvoke(dict(person_info))
            return result
        except Exception as e:
            raise ValueError(
                f"An error occurred while processing the request: {str(e)}"
            )
