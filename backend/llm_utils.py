# # # from transformers import pipeline

# # # # Initialize the conversational pipeline
# # # chat_pipeline = pipeline("conversational", model="facebook/blenderbot-400M-distill")

# # # def get_llm_response(user_input):
# # #     response = chat_pipeline(user_input)
# # #     return str(response)
# # from transformers import pipeline

# # # Use "text-generation" instead if "conversational" is not available
# # chat_pipeline = pipeline("text-generation", model="facebook/blenderbot-400M-distill")

# # def get_llm_response(user_input):
# #     response = chat_pipeline(user_input, max_length=100, num_return_sequences=1)
# #     return response[0]['generated_text']

# # # from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, Conversation, ConversationalPipeline

# # # model = AutoModelForSeq2SeqLM.from_pretrained("facebook/blenderbot-400M-distill")
# # # tokenizer = AutoTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
# # # chat_pipeline = ConversationalPipeline(model=model, tokenizer=tokenizer)

# # # def get_llm_response(user_input):
# # #     conversation = Conversation(user_input)
# # #     response = chat_pipeline([conversation])
# # #     return str(response)
# from transformers import pipeline
# import logging

# # Configure logging
# logging.basicConfig(level=logging.INFO)

# try:
#     # Initialize the conversational pipeline with a fallback option if 'conversational' is not available
#     chat_pipeline = pipeline("text-generation", model="facebook/blenderbot-400M-distill")
#     logging.info("LLM pipeline initialized successfully.")
# except Exception as e:
#     logging.error("Failed to initialize LLM pipeline: %s", str(e))
#     chat_pipeline = None

# def get_llm_response(user_input):
#     if chat_pipeline is None:
#         logging.error("LLM pipeline is not initialized.")
#         return "Error: LLM pipeline not available."
#     try:
#         response = chat_pipeline(user_input, max_length=100, num_return_sequences=1)
#         return response[0]['generated_text']
#     except Exception as e:
#         logging.error("Error during LLM response generation: %s", str(e))
#         return "Error: Failed to generate response."
from transformers import pipeline
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

try:
    # Initialize the pipeline for text generation
    chat_pipeline = pipeline("text-generation", model="facebook/blenderbot-400M-distill")
    logging.info("LLM pipeline initialized successfully.")
except Exception as e:
    logging.error("Failed to initialize LLM pipeline: %s", str(e))
    chat_pipeline = None

# def get_llm_response(user_input):
#     if chat_pipeline is None:
#         logging.error("LLM pipeline is not initialized.")
#         return "Error: LLM pipeline not available."
#     try:
#         response = chat_pipeline(user_input, max_length=100, num_return_sequences=1)
#         return response[0]['generated_text']
#     except Exception as e:
#         logging.error("Error during LLM response generation: %s", str(e))
#         return "Error: Failed to generate response."
def get_llm_response(user_input):
    if chat_pipeline is None:
        logging.error("LLM pipeline is not initialized.")
        return "Error: LLM pipeline not available."
    try:
        # Add truncation=True to the tokenizer call to suppress the warning
        response = chat_pipeline(user_input, max_length=100, num_return_sequences=1, truncation=True)
        return response[0]['generated_text']
    except Exception as e:
        logging.error("Error during LLM response generation: %s", str(e))
        return "Error: Failed to generate response."
