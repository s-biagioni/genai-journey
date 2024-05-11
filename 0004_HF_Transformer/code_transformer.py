# https://discuss.huggingface.co/t/using-hugging-face-models-with-private-company-data/56403/2

# https://huggingface.co/docs/transformers/main/en/model_doc/codegen
from transformers import AutoModelForCausalLM, AutoTokenizer

# The format is: Salesforce/codegen-{size}-{data}, where
# size: 350M, 2B, 6B, 16B (number of parameters/learnable weights)
# data:
# nl: Pre-trained on the Pile
# multi: Initialized with nl, then further pre-trained on multiple programming languages data
# mono: Initialized with multi, then further pre-trained on Python data

# Load the model and tokenizer
checkpoint = "Salesforce/codegen-2B-multi"
model = AutoModelForCausalLM.from_pretrained(checkpoint)
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

text = """
fn helloWorld() {
"""

# UserWarning: Using the model-agnostic default `max_length` (=20) to control the generation length. 
# We recommend setting `max_new_tokens` to control the maximum length of the generation.
completion = model.generate(**tokenizer(text, return_tensors="pt"), max_new_tokens=150)

print(tokenizer.decode(completion[0]))