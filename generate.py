import requests
import yaml

# Load configuration
with open('config.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)

# Define language colors
language_colors = {
    "Rust": "dea584",
    "Python": "3572A5",
    "JavaScript": "f1e05a",
    "C++": "f34b7d",
    "Mojo": "c6904b",
    "Fortran": "734f96",
    "Nim": "ffc200",
    "C": "555555",
    "TypeScript": "2b7489",
    "HTML": "e34c26"
}

# Function to get star count from GitHub API
def get_star_count(repo_url):
    api_url = repo_url.replace("https://github.com/", "https://api.github.com/repos/")
    print(api_url)
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json().get('stargazers_count', 0)
    
    print(f"{response.status_code}:", repo_url)
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

<style>
.container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}
.category {
    width: 48%;
    margin-bottom: 20px;
}
.repo-box {
    background-color: #1e1e1e;
    border-radius: 6px;
    padding: 10px;
    margin-bottom: 10px;
}
.repo-name {
    font-size: 16px;
    font-weight: bold;
    margin-bottom: 5px;
}
.repo-description {
    font-size: 14px;
    margin-bottom: 10px;
}
.repo-info {
    font-size: 12px;
}
</style>

<div class="container">
"""

    for category in config['categories']:
        readme_content += f'''
<div class="category">
<h2>{category["name"]}</h2>
<i>{category["description"]}</i><br><br>
'''
        for repo in category['repos']:
            star_count = get_star_count(repo['url'])
            language_color = language_colors.get(repo["language"], "000000")
            readme_content += f'''
<div class="repo-box">
<div class="repo-name"><a href="{repo["url"]}">{repo["name"]}</a></div>
<div class="repo-description">{repo.get("description", "")}</div>
<div class="repo-info">
    <span style="color: #{language_color};">●</span> {repo["language"]} ★ {star_count}
</div>
</div>
'''
        readme_content += '</div>\n'
    
    readme_content += '</div>\n'
    return readme_content

# Write README.md
readme_content = generate_readme(config)
with open('README.md', 'w') as readme_file:
    readme_file.write(readme_content)

print("README.md has been generated successfully.")