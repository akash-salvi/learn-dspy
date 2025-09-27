import os
import dspy

API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY") 

llm = dspy.LM(model='gemini/gemini-2.5-flash', api_key=API_KEY)
        
# Configure DSPy to use this Language Model instance globally
dspy.configure(lm=llm)

def get_dspy_instance():
    return dspy

def get_dspy_lm_instance():
    return llm