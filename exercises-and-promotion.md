## Exercise
	- Streamlit app where you get info from Wikipedia starting from a query
		- https://python.langchain.com/v0.2/docs/integrations/retrievers/wikipedia/
		- https://python.langchain.com/v0.2/docs/integrations/providers/wikipedia/
		- https://www.shakudo.io/blog/building-confluence-kb-qanda-app-langchain-chatgpt
	
	
	- Image and text embedding with Hugging Face
		- https://huggingface.co/blog/image-similarity
		- https://discuss.huggingface.co/t/how-to-combine-image-and-text-embedding-for-product-similarity/47761 
		
	- Shelved Kept - Digital Family Valut

## GenAI Promotion

	0. Documentation navigator
		- https://learn.deeplearning.ai/courses/langchain-chat-with-your-data/
		- https://www.shakudo.io/blog/building-confluence-kb-qanda-app-langchain-chatgpt
	1. Boilerplate code generator
		- https://www.shakudo.io/blog/building-confluence-kb-qanda-app-langchain-chatgpt
	2. Bug fixing/prevention/analysis	
		- https://www.deeplearning.ai/the-batch/github-previews-copilot-workspace-for-end-to-end-software-development/  
________________________________________
	+ Using HF models with private company data
		- https://discuss.huggingface.co/t/using-hugging-face-models-with-private-company-data/56403
			- https://huggingface.co/docs/transformers/main/en/installation
				+ models are here: https://huggingface.co/docs/transformers/index
					+ use a light model that 
						- can run on a laptop
						- is suited to code, e.g., llama, codegen
							- few shot learning, adjust the prompt engineering, experiment a bit, understand how far you can push it 
								- then fine tuning
								- RAG chain?
	+ use Rivet to evaluate your chain/RAG
	+ create some mock up code to be used with chatgpt and show GenAI capabilities
		- once they are convinced the might give you more resources
	+ private Azure endpoint
		https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/tools-reference/llm-tool?view=azureml-api-2
		--> [link: Create Azure OpenAI resources with these instructions] 
			https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?view=azureml-api-2&pivots=web-portal
	+ prompt flow [same as Rivet but on Azure]
	  https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/tools-reference/python-tool?view=azureml-api-2

	


## GenAI Promotion Inspo

- LLM Hints (email)

"Google is still my best friend, and I like to apply my mind but if AI can enrich my work experience, then I am open to it, understanding our business and clients is still very important and that AI cannot do for me :)"

"I like the idea of Copilot and similar tools patch up my descriptions/comments throughout the code, though! Hope its grammar is better than mine :)"

"I would like that at least some of us have chance to use and evaluate it in our workplace. It's not mean some low quality but at least it would help automate some manual work like created Reader/Writer/Entity/Mapper when we have new DB schema. So we can focus our time one real business and code logic."

"ChatGPT is quite useful tool when you need to check how to do certain things, like smarter documentation search and for some basic boilerplate generation."

"And it can give very useful examples of how to use the API, which is very useful because some documentation does not have any examples, just tells you what it is supposed to do and that is all."

"I believe the real potential for LLMs in our case is to feed our code base to it, so it can respond questions about the code itself. That would be really nice to have."
