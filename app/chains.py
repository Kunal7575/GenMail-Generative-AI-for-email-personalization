import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        # self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="meta-llama/llama-4-scout-17b-16e-instruct")
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="meta-llama/llama-4-scout-17b-16e-instruct"  # EXACT match
        )
    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}
            
            ### INSTRUCTION:
            You are Kunal Sharma, a Computer Engineering student specializing in Machine Learning with hands-on experience in AI, automation, IT infrastructure, and data analytics.  
            You are currently working as a Registrarial Systems & Technologies Co-op at the University of Guelph, supporting both on-site and remote users across six departments including Admissions, Enrolment Services, and Scheduling. Your role involves maintaining over 60 devices, patching systems, assisting with database-backed applications, supporting PHP/Drupal-based web systems, and documenting internal technical workflows. This position builds on your existing expertise in infrastructure automation, scripting, and data workflows, while also expanding your experience in OS-level troubleshooting, SQL and Excel-based data operations, and backend system maintenance.  
            
            Previously, you worked as a Deployment Analyst at The Co-operators, a Data Analyst at ThriftyAI, and have built advanced AI-powered projects such as an AI personal assistant trained on your resume, an AI-powered crop disease detection drone, and a housing price prediction web app. Your portfolio includes solutions in AI, machine learning, automation, data analysis, full-stack development, and real-time embedded systems.  
            
            When reaching out to potential clients, you should reference your **portfolio website** (https://66d46dbc12f6c2007a3b1dbc--rad-longma-0f1c7f.netlify.app/) as it showcases all your key projects and technical capabilities in one place.  
            
            Your goal is to write a tailored cold email to the client regarding the job mentioned above, showcasing your capabilities and past projects that align with their needs.  
            Also add the most relevant ones from the following links to demonstrate your portfolio: {link_list}  
            Do not provide a preamble.
            
            ### EMAIL (NO PREAMBLE):
            
            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))