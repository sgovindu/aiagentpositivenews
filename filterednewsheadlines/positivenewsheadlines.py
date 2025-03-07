from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel, tool
from transformers import pipeline

@tool
def only_positive_news(news_headline: str) -> bool:
    """ A tool that checks if the news headline evokes positive emotion.
        Args:
         news_headline: str **today's headline news** # Added description on same line as argument
        Returns:
         news_headline: bool **True if the news headline evokes positive emotion, False otherwise** # Added description on same line as return value
    """
    sentiment_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")
    filtered_headline = sentiment_pipeline(news_headline)
    print(f'{news_headline} has sentiment {filtered_headline}')
    # Label 2 is positive and Label 1 is neutral
    # Label 0 is negative
    if "LABEL_2" in filtered_headline[0].get('label') or "LABEL_1" in filtered_headline[0].get('label'):
        return True
    else:
        return False

agent = CodeAgent(tools=[DuckDuckGoSearchTool(), only_positive_news], model=HfApiModel(), additional_authorized_imports=['bs4', 're', 'requests'])

prompt = """
    Search for latest headline news published today from NDTV. Find url that has latest in it and fetch the top 10 news headline.
    Fetch the headline text using link css defined as NwsLstPg_ttl-lnk. Once you get the headline find only positive news headlines.
"""
prompt_1 = """
    Search for latest headline news published today from HINDU. Find url that has latest-news in it and fetch the top 10 news headlines.
    Fetch the headline text using link css defined as h3 title. Once you get the headline find only positive news headlines.
"""

agent.run(prompt)
