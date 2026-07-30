import requests
import yaml

# Load configuration
with open('config.yml', 'r', encoding='utf-8') as config_file:
    config = yaml.safe_load(config_file)

# Define language colors using flat colored square emojis
language_emojis = {
    "Rust": "🟧",  # Orange square
    "Python": "🟦",  # Blue square
    "JavaScript": "🟨",  # Yellow square
    "C++": "🟥",  # Red square
    "Mojo": "🟫",  # Brown square
    "Fortran": "🟪",  # Purple square
    "Nim": "🟨",  # Yellow square
    "C": "⬛",  # Black square
    "TypeScript": "🟦",  # Blue square
    "Python/C++": "🟦"  # Blue square for mixed
}

# Function to get star count from GitHub API
def get_star_count(repo_url):
    api_url = repo_url.replace("https://github.com/", "https://api.github.com/repos/")
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json().get('stargazers_count', 0)
    return 0

# Generate README content
def generate_readme(config):
    readme_content = """### Hi there! 👋
![](https://img.shields.io/discord/915760402195959861?color=green&label=discord)
![](https://img.shields.io/github/stars/SatinWukerORIG?label=My%20Stars&color=red&style=social)
![](https://img.shields.io/github/stars/Rick-lang?label=Rick-lang%20Team%20Stars&logoColor=red&style=social)
![](https://komarev.com/ghpvc/?username=SatinWuker)

I am Satin Wuker, the founder of the Rickroll programming language; <br>
a student who devotes himself to compiler & interpreter development, AI, research, and cool stuff. <br>

I have become swamped since school started;-; Sorry if you find me not replying to your issue or PR<br>
but I will still try to study cutting-edge technology and publish useful and outstanding projects!

"""

    for category in config['categories']:
        readme_content += f'<h2>{category["name"]}</h2>\n'
        readme_content += f'<i>{category["description"]}</i>\n\n'
        readme_content += '<table>\n'
        
        # Process repos in pairs (two per row)
        repos = category['repos']
        for i in range(0, len(repos), 2):
            readme_content += '  <tr>\n'
            
            # First column (always exists)
            repo = repos[i]
            star_count = get_star_count(repo['url'])
            language_emoji = language_emojis.get(repo["language"], "⚪")
            readme_content += '    <td valign="top" width="50%">\n'
            readme_content += f'      <h3><a href="{repo["url"]}">{repo["name"]}</a></h3>\n'
            readme_content += f'      {repo.get("description", "")}<br><br>\n'
            readme_content += '      ____________________________________________________________<br><br>\n'
            readme_content += f'      {language_emoji}&nbsp;'
            readme_content += f'{repo["language"]}&nbsp;&nbsp;&nbsp;&nbsp;★ {star_count}\n'
            readme_content += '    </td>\n'
            
            # Second column (if exists)
            if i + 1 < len(repos):
                repo = repos[i + 1]
                star_count = get_star_count(repo['url'])
                language_emoji = language_emojis.get(repo["language"], "⚪")
                readme_content += '    <td valign="top" width="50%">\n'
                readme_content += f'      <h3><a href="{repo["url"]}">{repo["name"]}</a></h3>\n'
                readme_content += f'      {repo.get("description", "")}<br><br>\n'
                readme_content += '      ____________________________________________________________<br><br>\n'
                readme_content += f'      {language_emoji}&nbsp;'
                readme_content += f'{repo["language"]}&nbsp;&nbsp;&nbsp;&nbsp;★ {star_count}\n'
                readme_content += '    </td>\n'
            else:
                # Empty cell for odd number of repos
                readme_content += '    <td valign="top" width="50%">\n'
                readme_content += '    </td>\n'
            
            readme_content += '  </tr>\n'
        
        readme_content += '</table>\n\n'
    
    return readme_content

# Write README.md
readme_content = generate_readme(config)
with open('README.md', 'w', encoding='utf-8') as readme_file:
    readme_file.write(readme_content)

print("README.md has been generated successfully.")
