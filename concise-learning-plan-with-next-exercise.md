## Concise

1. Text Embeddings
https://www.deeplearning.ai/short-courses/google-cloud-vertex-ai/

2. Vector Databases
https://www.deeplearning.ai/short-courses/vector-databases-embeddings-applications/
https://www.deeplearning.ai/short-courses/building-applications-vector-databases/

3. LangChain
https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/
https://www.deeplearning.ai/short-courses/langchain-chat-with-your-data/
--> look at Gabriele's links
https://www.deeplearning.ai/short-courses/functions-tools-agents-langchain/


4. Fine-Tuning
https://www.deeplearning.ai/short-courses/finetuning-large-language-models/

5. Reinforcement Learning
https://www.deeplearning.ai/short-courses/reinforcement-learning-from-human-feedback/


- later
	+ RAG
		https://www.deeplearning.ai/short-courses/knowledge-graphs-rag/
		https://learn.deeplearning.ai/courses/building-agentic-rag-with-llamaindex/

	+ KV caching and LoRA
		https://www.deeplearning.ai/short-courses/efficiently-serving-llms/


## Exercise
	- Image and text embedding with Hugging Face
		- https://huggingface.co/blog/image-similarity
		- https://discuss.huggingface.co/t/how-to-combine-image-and-text-embedding-for-product-similarity/47761 

## GenAI Promotion

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
