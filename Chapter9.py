# Japan Job API Tracker — Chapter 9
# Pulls real data and saves it — your first mini data pipeline

import requests
import json
from datetime import datetime
from pathlib import Path

def fetch_github_japan_jobs():
    """
    Search GitHub Jobs API for Japan-related
    data engineering and robotics roles
    """
    # GitHub search API — public, no key needed
    url = "https://api.github.com/search/repositories"
    
    params = {
        "q": "robotics ROS2 japan",
        "sort": "stars",
        "order": "desc",
        "per_page": 5
    }
    
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    
    try:
        response = requests.get(url, params=params,
                               headers=headers)
        response.raise_for_status()
        data = response.json()
        
        print("=" * 50)
        print("  TOP ROBOTICS + JAPAN REPOS ON GITHUB")
        print("=" * 50)
        
        Path("japan_data").mkdir(exist_ok=True)
        
        repos = []
        for repo in data["items"]:
            info = {
                "name": repo["full_name"],
                "stars": repo["stargazers_count"],
                "description": repo["description"],
                "url": repo["html_url"],
                "language": repo["language"]
            }
            repos.append(info)
            
            print(f"\n  {repo['full_name']}")
            print(f"  ⭐ {repo['stargazers_count']} stars")
            print(f"  {repo['description']}")
            print(f"  Language: {repo['language']}")
        
        # Save to file
        output = {
            "fetched_at": datetime.now().isoformat(),
            "query": "robotics ROS2 japan",
            "results": repos
        }
        
        with open("japan_data/robotics_repos.json", "w") as f:
            json.dump(output, f, indent=2)
        
        print(f"\nData saved to japan_data/robotics_repos.json")
        print("Study these repositories. These are your future peers.")
        
    except requests.exceptions.ConnectionError:
        print("No internet. Check connection.")
    except Exception as e:
        print(f"Error: {e}")

fetch_github_japan_jobs()