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


## Extended


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

3. [X] LangChain
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
	+ Document Loading
		- PDFs
		- YouTube
		- Urls
	+ Document Splitting
		- CharacterTextSplitter 
			- changing the separator 
		- RecursiveCharacterTextSplitter
			- used different kinds of separators (\n, space, \n\n " ", "", "\.")
		- TokenTextSplitter
		- MarkdownHeaderTextSplitter
			- splits a markdown on the basis of the header
	+ Vectorstores and embedding
		- Embeddings
			- OpenAIEmbeddings
				- numpy.dot(embedding1, embedding2)
		- Vectorstores
			- Chroma
				- similarity search on PyPDFLoader  --> RecursiveCharacterTextSplitter
					- question = "is there an email i can ask for help"
					  docs = vectordb.similarity_search(question,k=3)
	+ Retrieval
		- vectordb = Chroma()
			+ MMR (fosters diversity in a top-k search)
				- vectordb.max_marginal_relevance_search(question,k=3)
			+ SelfQuery
				- from langchain.retrievers.self_query.base import SelfQueryRetriever
			+ Compression
				- from langchain.retrievers import ContextualCompressionRetriever
				- from langchain.retrievers.document_compressors import LLMChainExtractor
	+ Question Answering
		- RetrievalQA Chain
			- from langchain.chains import RetrievalQA
		- RetrievalQA chain types
			- stuff(default),
			- efficient usage of the context window
				- map_reduce, refine
	+ Chat
		- handling follow-up questions
			- from langchain.memory import ConversationBufferMemory
			- from langchain.chains import ConversationalRetrievalChain
		- creation of a complete chatbot
 
 
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
