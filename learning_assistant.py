import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.5,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

def learning_help(question):
    """Provide learning assistance"""
    
    prompt = ChatPromptTemplate.from_template(
        """You are a helpful learning assistant for students. Answer this question in an educational way:

Question: {question}

Provide:
1. A clear, simple explanation
2. Examples if applicable
3. Key takeaways
4. What to learn next related to this topic

Keep it beginner-friendly and encouraging."""
    )
    
    chain = prompt | llm
    result = chain.invoke({"question": question})
    
    return result.content