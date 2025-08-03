# Resource Agent

Resource Agent is a modular Python agent designed to fetch, curate, and deliver relevant information and resources about any topic. By leveraging Tavily Search (or other search engines), it performs real-time web searches and presents results in a structured, developer-friendly format. The agent is easily extensible, suitable for integration into chatbots, automation systems, research tools, and more.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  - [FastAPI Web Service](#fastapi-web-service)
  - [Python Integration](#python-integration)
  - [Command Line Interface](#command-line-interface)
  - [Sample Output](#sample-output)
- [API Reference](#api-reference)
- [Extensibility & Customization](#extensibility--customization)
- [Error Handling](#error-handling)
- [Testing](#testing)
- [Best Practices](#best-practices)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [FAQ](#faq)

---

## Overview

Resource Agent acts as your intelligent assistant for finding, filtering, and presenting information on any subject. It is built with modularity and extensibility in mind, making it easy to adapt for different contexts and use cases. The agent fetches results from Tavily Search and processes them for quality and relevance.

---

## Features

- **Topic-based Search:** Input any topic or query and receive curated, relevant online resources.
- **Web Search Integration:** Powered by Tavily Search API, enabling real-time access to up-to-date information.
- **Resource Curation:** Filters, ranks, and presents links, summaries, and metadata for each resource.
- **FastAPI Web Service:** RESTful API endpoints for easy integration with web applications.
- **Output Formatting:** Presents results in Python objects, JSON, Markdown, or other formats suitable for different downstream applications.
- **Extensible Architecture:** Easily add new search engines, filtering strategies, or output formats.
- **Error Handling:** Robust and transparent error management.
### Flow Diagram

```
User Query (API/CLI)
   |
   v
[Agent Core] --> [Search API Client] --> [Result Processor] --> [Output]
   ^
   |
[FastAPI App] (for web service)
```
Each module can be swapped or extended independently.

---

## Installation

**Requirements:**
- Python 3.8 or newer
- Tavily Search API key

**Steps:**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sathwikshetty33/resource-agent.git
   cd resource-agent
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

1. **API Key Setup:**
   - Obtain your Tavily Search API key from [Tavily](https://www.tavily.com/) and set it as an environment variable:
     ```bash
     export TAVILY_API_KEY=your_api_key_here
     ```
     - Obtain your Groq API key and set it as an environment variable:
     ```bash
     export GROQ_API_KEY=your_api_key_here
     ```
---

## Usage

### FastAPI Web Service

**Starting the FastAPI Server:**

```bash
# Start the server on default port 8000
uvicorn app:app --reload

# Start the server on custom port 8001
uvicorn app:app --port 8001

# Start with host binding for external access
uvicorn app:app --host 0.0.0.0 --port 8001

# Start in production mode (without auto-reload)
uvicorn app:app --port 8001 --workers 4
```

**API Endpoints:**

Once the server is running, you can access:
- **Interactive API docs:** `http://localhost:8001/docs`
- **Alternative docs:** `http://localhost:8001/redoc`

**Example API Usage:**

```bash
# Using curl
curl -X POST "http://localhost:8001/search" \
     -H "Content-Type: application/json" \
     -d '{"query": "States of water and evaporation", "num_results": 5}'

# Using Python requests
import requests

response = requests.post(
    "http://localhost:8001/search",
    json={"query": "States of water and evaporation", "num_results": 5}
)
results = response.json()
```

### Python Integration

```python


agent = ResourceAgent()
results = agent.search("States of water and evaporation", num_results=5)

for topic, urls in results.items():
    print(f"Topic: {topic}")
    for url in urls:
        print(f"- {url}")
```

### Command Line Interface

If the CLI is implemented:
```bash
python resource_agent/main.py "Applications of blockchain in supply chain"
```

---

## Sample Output

When you ask the agent about a topic, e.g., "States of water and evaporation", it will return a structured dictionary mapping topics/questions to curated resource URLs. For example:

```python
{
    "Here are 5 key topics or questions from the text:": [
        "https://www.middleweb.com/50526/5-questions-to-help-kids-become-critical-readers/",
        "https://classicalconversations.com/blog/five-common-topics-of-dialectic/",
        "https://www.vcestudyguides.com/blog/the-5-types-of-text-response-prompts",
        "https://dynamicecology.wordpress.com/2016/02/24/the-5-pivotal-paragraphs-in-a-paper/",
        "https://www.readingrockets.org/topics/comprehension/articles/seven-strategies-teach-students-text-comprehension"
    ],
    "* **States of Water:** The text explores the different states of water (ice, liquid water, and water vapor) and their properties.": [
        "https://ftp.survation.com/waters-incredible-transformations-exploring-the-states-of-matter/",
        "https://flexbooks.ck12.org/cbook/ck-12-middle-school-earth-science-flexbook-2.0/section/8.2/primary/lesson/states-of-water-ms-es/",
        "https://learning-center.homesciencetools.com/article/states-of-matter/",
        "https://qz.com/871371/there-is-a-fourth-physical-state-of-matter-for-water-besides-solid-liquid-and-gas",
        "https://www.apecwater.com/blogs/news/resource-water-chemistry?srsltid=AfmBOoo4BjRMtI8IcS5wKiXIKQbWYrOzRTl7ZkTRSMWi70THiSAamZ4t"
    ],
    "* **Water Disappearance:**  The story poses the question of where water goes when it disappears from puddles or wet surfaces, leading to discussions about evaporation and seepage.": [
        "https://discussion.tiwariacademy.com/question/why-does-water-disappear-from-puddles/",
        "https://www.epa.gov/sites/default/files/2015-08/documents/mgwc-ww-disap.pdf",
        "https://www.acs.org/education/resources/k-8/inquiryinaction/kindergarten/chapter-1/why-do-puddles-dry-up.html",
        "https://static1.squarespace.com/static/5f09c80930b545063d089cc6/t/5ff9b5033b112d2bb6d06292/1610200324451/Water+in+Puddle.pdf",
        "https://www.canr.msu.edu/resources/teaching_science_when_you_dont_know_diddly_squat_how_do_puddles_disappear"
    ],
    "* **Evaporation:** The text explains the process of evaporation, how liquid water turns into water vapor, and provides examples like drying clothes and sweating.": [
        "https://education.nationalgeographic.org/resource/process-evaporation/",
        "https://www.usgs.gov/water-science-school/science/evaporation-and-water-cycle",
        "https://education.nationalgeographic.org/resource/evaporation/",
        "https://www.youtube.com/watch?v=uV9WDCCaKpk",
        "https://www.cpp.edu/respect/resources/documents_5th/gr5.wc_content_background.pdf"
    ],
    "* **Water Vapor:** The text introduces the concept of water vapor as an invisible gas and explains how it can become visible as steam due to tiny water droplets.": [
        "https://brainly.com/question/58136801",
        "https://en.wikipedia.org/wiki/Steam",
        "https://water.lsbu.ac.uk/water/steam.html",
        "https://www.differencebetween.info/difference-between-water-vapor-and-steam",
        "https://www.youtube.com/watch?v=3ZuMkPsQbjk"
    ],
    "* **Scientific Inquiry:** The text encourages readers to observe, question, and design experiments (like the activity with the steel plate) to investigate phenomena related to water.": [
        "https://www.youtube.com/watch?v=-MqlKogHu4o",
        "https://quizlet.com/566531991/science-scientific-inquiry-design-chapter-1-chapter-2-nature-of-scientific-knowledge-chapter-3-major-developments-historical-figures-in-science-chapter-4-collecting-analyzing-scientific-d-flash-cards/",
        "https://quizlet.com/480276658/scientific-inquiry-flash-cards/"
    ]
}
```

This output can be easily mapped to frontends, educational dashboards, or used as references in research.

---

## API Reference

### ResourceAgent

#### Initialization

```python
ResourceAgent(api_key: str, config: Optional[dict] = None)
```

- **api_key**: Tavily Search API key
- **config**: Optional dictionary of agent configuration parameters

#### Methods

- **search(query: str, num_results: int = 5) -> Dict[str, List[str]]**
  - **query**: Search topic or phrase
  - **num_results**: Number of resources to return per topic
  - **Returns**: Dictionary mapping topic/questions to lists of resource URLs

#### FastAPI Endpoints

- **POST `/process-pdf`**: Main search endpoint while test with post send it as form data where key=file and type = file and then attach the file.
  - **Request Body**: `{"query": "search term", "num_results": 5}`
  - **Response**: JSON object with topic mappings to resource URLs

- **GET `/health`**: Health check endpoint
  - **Response**: `{"status": "healthy"}`

#### Resource Output Structure

```python
{
    "Topic/Question 1": ["url1", "url2", ...],
    "Topic/Question 2": ["url3", "url4", ...]
}
```

---

## Extensibility & Customization

### Adding a New Search Provider

To support new search APIs:

1. Create a new client module (e.g., `my_search_client.py`) with a method matching the Tavily client's interface.
2. Update `agent.py` to support provider selection via configuration.
3. Register your client in the configuration.

### Custom Filtering & Ranking

- Implement your own filtering logic in `processor.py`.
- Use custom ranking algorithms based on metadata, relevance, or even NLP models.

### Output Formatting

- Add new output formats (e.g., HTML, JSON, Markdown) by extending the result processor or agent core.

---

## Error Handling

- All API calls are wrapped in try/except blocks.
- Network/API errors return clear messages in the output: e.g., `"error": "API request failed: <reason>"`
- Malformed queries or missing configuration result in actionable error messages.
- Logging is supported for debugging and traceability (see `logging` section in `config.py`).

---

## Best Practices

- **API Key Security:** Never hardcode your API keys. Use environment variables.
- **Rate Limiting:** Tavily (and other APIs) may have limits; handle `429 Too Many Requests` gracefully.
- **Caching:** For repeated queries, implement a caching layer to reduce API usage.
- **Virtual Environment:** Always use a virtual environment to isolate project dependencies.
- **Extensibility:** Build new modules as plug-ins for easy future upgrades.
- **Documentation:** Keep docstrings up-to-date for every module and method.

---

## Contributing

We welcome contributions of all kinds!

1. Fork the repository
2. Create a branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add feature'`)
4. Push to your fork (`git push origin feature/your-feature`)
5. Open a Pull Request

Please ensure new features are covered by tests and documented in this README.

---

## License

This project is distributed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Acknowledgements

- [Tavily Search API](https://www.tavily.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- Open Source Python Community
- [Your GitHub Profile](https://github.com/sathwikshetty33)

---

## FAQ

**Q:** How do I increase the number of results returned?  
**A:** Adjust the `num_results` parameter when calling `agent.search()` or in the API request body.

**Q:** Can I customize the result filtering?  
**A:** Yes! Edit the `processor.py` module to apply your own filters.

**Q:** How do I add support for another search API?  
**A:** Implement a new search client and update the agent to use it via configuration.

---

## Contact

For support, feature requests, or bug reports, please open an issue on GitHub or email the project maintainer.
