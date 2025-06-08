import requests
from typing import Dict
import logging
from bs4 import BeautifulSoup
import time
import random

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SEODataFetcher:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def get_google_suggestions(self, keyword: str) -> int:
        """
        Get search volume estimate from Google Autocomplete suggestions
        """
        try:
            url = f"https://suggestqueries.google.com/complete/search?client=firefox&q={keyword}"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            suggestions = response.json()[1]
            return len(suggestions) * 1000  # Rough estimate based on suggestion count
        except Exception as e:
            logger.error(f"Error getting Google suggestions: {str(e)}")
            return 0

    def get_competition_score(self, keyword: str) -> float:
        """
        Get competition score based on Google search results
        """
        try:
            url = f"https://www.google.com/search?q={keyword}"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Count number of ads and organic results
            ads = len(soup.find_all('div', {'class': 'uEierd'}))
            organic_results = len(soup.find_all('div', {'class': 'g'}))
            
            # Calculate competition score (0-100)
            if organic_results == 0:
                return 0
            competition_score = (ads / organic_results) * 100
            return min(competition_score, 100)
        except Exception as e:
            logger.error(f"Error getting competition score: {str(e)}")
            return 0

    def get_cpc_estimate(self, keyword: str) -> float:
        """
        Get estimated CPC based on keyword length and competition
        """
        try:
            # Simple CPC estimation based on keyword length and competition
            word_count = len(keyword.split())
            competition = self.get_competition_score(keyword)
            
            # Base CPC on word count and competition
            base_cpc = 0.5 + (word_count * 0.1)
            competition_multiplier = 1 + (competition / 100)
            
            return round(base_cpc * competition_multiplier, 2)
        except Exception as e:
            logger.error(f"Error calculating CPC estimate: {str(e)}")
            return 0.5

    def get_seo_data(self, keyword: str) -> Dict[str, float]:
        """
        Get SEO metrics for a given keyword using free data sources.
        
        Args:
            keyword (str): The keyword to get SEO data for
            
        Returns:
            Dict[str, float]: Dictionary containing SEO metrics
        """
        try:
            # Add delay to avoid rate limiting
            time.sleep(1)
            
            search_volume = self.get_google_suggestions(keyword)
            keyword_difficulty = self.get_competition_score(keyword)
            avg_cpc = self.get_cpc_estimate(keyword)
            
            seo_data = {
                "search_volume": search_volume,
                "keyword_difficulty": keyword_difficulty,
                "avg_cpc": avg_cpc
            }
            
            logger.info(f"Successfully fetched SEO data for keyword: {keyword}")
            return seo_data
            
        except Exception as e:
            logger.error(f"Unexpected error in get_seo_data: {str(e)}")
            # Fallback to basic data if all methods fail
            return {
                "search_volume": 0,
                "keyword_difficulty": 0,
                "avg_cpc": 0
            }

# Create a singleton instance
seo_fetcher = SEODataFetcher()

def get_seo_data(keyword: str) -> Dict[str, float]:
    """
    Get SEO metrics for a given keyword.
    This is a wrapper function that uses the SEODataFetcher class.
    
    Args:
        keyword (str): The keyword to get SEO data for
        
    Returns:
        Dict[str, float]: Dictionary containing SEO metrics
    """
    return seo_fetcher.get_seo_data(keyword)