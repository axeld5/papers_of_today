"""ArXiV API related functions used for paper extraction"""

import requests
import xml.etree.ElementTree as ET

CS_CLASSES = [
    'cs.' + cat for cat in [
        'AI', 'AR', 'CC', 'CE', 'CG', 'CL', 'CR', 'CV', 'CY', 'DB',
        'DC', 'DL', 'DM', 'DS', 'ET', 'FL', 'GL', 'GR', 'GT', 'HC',
        'IR', 'IT', 'LG', 'LO', 'MA', 'MM', 'MS', 'NA', 'NE', 'NI',
        'OH', 'OS', 'PF', 'PL', 'RO', 'SC', 'SD', 'SE', 'SI', 'SY',
    ]
]

def get_arxiv_papers(date:str) -> list:
    """Extracts all computer vision papers related to a date.
    
    Args:
        date (str): Must be of the form YYYY-MM-DD
    
    Returns:
        papers (list[dict[str, str]]): papers with links, titles, summaries, authors, and publication date
    """
    papers = []    
    for cls in CS_CLASSES:
        query = f"http://export.arxiv.org/api/query?search_query=cat:'{cls}'&sortBy=submittedDate&sortOrder=descending"
        params = {
                "start": 0,
                "max_results": 1000
        }
        response = requests.get(query, params=params)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            entries = root.findall('{http://www.w3.org/2005/Atom}entry')
            for entry in entries:
                paper = {
                    'id': entry.find('{http://www.w3.org/2005/Atom}id').text,
                    'title': entry.find('{http://www.w3.org/2005/Atom}title').text,
                    'summary': entry.find('{http://www.w3.org/2005/Atom}summary').text,
                    'authors': [author.find('{http://www.w3.org/2005/Atom}name').text for author in entry.findall('{http://www.w3.org/2005/Atom}author')],
                    'published': entry.find('{http://www.w3.org/2005/Atom}published').text
                }
                if date in paper["published"]:
                    papers.append(paper)
    return papers