from llm_model.models import llm_max,llm_mini,llm_reasoning
import litellm 
from litellm import completion

# llm gate fall back 

def model_cost( response):

    """  llm cost  per  input and output """
    cost=completion_cost(completion_response=)
    
