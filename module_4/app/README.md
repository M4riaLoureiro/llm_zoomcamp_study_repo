# Module 4 App


## Setup Instructions

1. Install required packages

```
python -m pip install -r requirements.txt
```

2. Run docker compose:

```
docker-compose up
```

3. Run prep.py script

```
python prep.py
```

4. Pull desired model form Ollama (phi3 or any other)

```
docker exec -it ollama_container_id bash

ollama pull phi3
```