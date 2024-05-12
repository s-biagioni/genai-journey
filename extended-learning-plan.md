1. [X] Text Embeddings
https://www.deeplearning.ai/short-courses/google-cloud-vertex-ai/
	- embedding of a strings
	- distance among strings
	- Exercises:
		+ https://github.com/s-biagioni/genai-journey/tree/main/0001_embeddings

2. [X] Vector Databases
https://www.deeplearning.ai/short-courses/vector-databases-embeddings-applications/
	- https://learn.deeplearning.ai/courses/vector-databases-embeddings-applications/lesson/2/how-to-obtain-vector-representations-of-data
		+ vector representation of pictures
		+ training a model to recognise them
		+ computing the distances among different pictures
	- https://learn.deeplearning.ai/courses/vector-databases-embeddings-applications/lesson/3/search-for-similar-vectors
	  https://learn.deeplearning.ai/courses/vector-databases-embeddings-applications/lesson/4/approximate-nearest-neighbours	
		+ KNN vs. ANN
			- ANN and distances using Weaviate open source vector db
	- https://www.deeplearning.ai/short-courses/building-applications-vector-databases/
		+ CRUD for vector embedding of
			- question/answer dataset
			- objects
	- https://learn.deeplearning.ai/courses/vector-databases-embeddings-applications/lesson/6/sparse,-dense,-and-hybrid-search
		+ comparing Sparse, Dense and Hybrid search  using Weaviate
	- https://learn.deeplearning.ai/courses/vector-databases-embeddings-applications/lesson/7/application---multilingual-search
		+ Weaviate (multilingual vector db search) + Cohere (RAG)
	- Exercises
		+ https://github.com/s-biagioni/genai-journey/tree/main/0002_Image_Embeddings

3. [ ] LangChain
https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/
	+ Models, Prompts and Parsers
		- OpenAI ChatGPT 3 turbo through LangChain wrapper
			- prompt formatting
		- LangChain LLM's output parsing to Python dictionary
			e.g., Thought, Action, Observation (Chain-of-Thought Reasoning – ReAct)
			- LangChain StructuredOutputParser
	+ Memory
		- ConversationBufferMemory
		- ConversationBufferWindowMemory --> you state how many conversational exchanges it should remember
		- ConversationTokenBufferMemory	 --> limits the number of tokens saved
		- ConversationSummaryMemory
	+ Chains
		- LLMChain = llm + prompt
		- Sequential Chains
			- SimpleSequentialChain = single input, single output LLMChains concatenated
			- SequentialChain = multiple input, multiple output LLMChains concatenated
		- Router Chain = conditional usage of specific LLMChains on the basis of the input
	+ Q&A over Documents
		- VectorstoreIndexCreator( DocArrayInMemorySearch ) + OpenAIEmbeddings to embed the documents
	+ LangChain evaluation
			1. creating query+answer examples with QAGenerateChain.from_llm(ChatOpenAI)
		- Manual evaluation (and debuging)
			2.1 manually evaluate happens under the hood when running qa.run(examples[0]["query]) by setting langchain.debug = True
		- LLM-assisted evaluation 
			2.2 use QAEvalChain to have a model evaluate the answers from the model
		- LangChain evaluation platform
			- LangChain evaluation platform:  https://www.langchain.plus/
	+ Agents
		- Using built in LangChain agents
			- Calculator
			- Wikipedia
			- Python
		- Defining your own tools
 https://www.deeplearning.ai/short-courses/langchain-chat-with-your-data/
 --> look at Gabriele's links
 https://www.deeplearning.ai/short-courses/functions-tools-agents-langchain/

4. [ ] Fine-Tuning
https://www.deeplearning.ai/short-courses/finetuning-large-language-models/

5. [ ] Reinforcement Learning
https://www.deeplearning.ai/short-courses/reinforcement-learning-from-human-feedback/


- [ ] later
	+ RAG
		https://www.deeplearning.ai/short-courses/knowledge-graphs-rag/
		https://learn.deeplearning.ai/courses/building-agentic-rag-with-llamaindex/

	+ KV caching and LoRA
		https://www.deeplearning.ai/short-courses/efficiently-serving-llms/
