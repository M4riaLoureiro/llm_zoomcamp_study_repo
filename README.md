# LLM Zoomcamp Study Repository

This repository contains all the code and materials developed during the LLM Zoomcamp course, organized by [DataTalks.Club](https://github.com/DataTalksClub/llm-zoomcamp). I worked on this course from July to August 2024, focusing on real-life applications of Large Language Models (LLMs).


## Repository Structure

The repository is organized as follows:

```plaintext
├── __pycache__        # Cache files for Python modules
├── module_1           # Code and notebooks for Module 1: Introduction to LLMs and RAG
├── module_2           # Code and notebooks for Module 2: Open-source LLMs
├── module_3           # Code and notebooks for Module 3: Vector databases
├── module_4           # Code and notebooks for Module 4: Evaluation and monitoring
├── utils              # Utility scripts and helper functions used across modules
├── .gitignore         # Git ignore file
└── README.md          # This README file
```


## Random Useful Notes


### Elastic Search

```
docker run -it \
    --rm \
    --name elasticsearch \
    -m 4GB \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    docker.elastic.co/elasticsearch/elasticsearch:8.4.3
```

### Ollama

1. After deployment using docker run or docker file, access ollama:

```
docker exec -it ollama_container_id bash
```

2. Pull model that we need:

```
ollama pull model_name
```

### Postgres DB

1. Check existing tables:

```
pip install pgcli
pip install "psycopg[binary,pool]"
pgcli -h localhost -U your_username -d course_assistant -W
```

2. After running previous commands, check databases:

```
\l
```

3. Enter a given database:

```
\c database_name
```

4. Check tables within that:

```
\dt
```

## About the Course

**LLM Zoomcamp** is a free online course that teaches participants how to build AI systems that answer questions about knowledge bases. Over 10 weeks, I've learned practical skills and techniques related to LLMs, such as retrieval-augmented generation (RAG), vector databases, evaluation, and monitoring.

**Course Highlights:**
- Build real-world AI systems with LLMs.
- Learn open-source tools and frameworks, including HuggingFace, Streamlit, and LangChain.
- Hands-on workshops to solidify learning through practical projects.
- Weekly video tutorials available on [DataTalks.Club's YouTube channel](https://www.youtube.com/@DataTalksClub).

**Instructors:**
- Alexey Grigorev
- Magdalena Kuhn
- Balaji Dhamodharan
- Tommy Dang
- Timur Kamaliev

For more details, visit the official [LLM Zoomcamp GitHub page](https://github.com/DataTalksClub/llm-zoomcamp).

