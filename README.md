# aiagentpositivenews
AI agent that uses smolagents to fetch headline news and returns positive emotion headlines.

# Huggingface smolagents
Huggingface smilagents provides a framework to build AI agents. AI agents follow the paradigm of *thought*-*action*-*observation* They think, act and observe. In all in this process, LLM acts as the brain that provides information for the agent.

# Smolagent
Most of the agentic frameworks interact with LLM through Json blobs. However, Smolagents uses CodeAgent that generate dynamic python code thus making it easy to decipher and understand the actions performed by the agent.
[Code Agents](https://huggingface.co/blog/smolagents#code-agents) explains briefly the working of CodeAgent.

# Positive headline news
Currently if you go through any news paper headlines, you might wonder why the world is full of negativity. Using agentic frameworks, positive headline news filters out all news headlines and displays only headlines that evokes positive emotions.

**Prerequisites**
1. Create a huggingface account if not done
2. Generate a HF_TOKEN
3. Login to hf using python or cli
4. pip install smolagents
5. python positivenewsheadline.py 
