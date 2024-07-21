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
    "TypeScript": "2b7489"
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
        readme_content += f'<td valign="top"><h2>{category["name"]}</h2><i>{category["description"]}</i><br><br>\n'
        for repo in category['repos']:
            star_count = get_star_count(repo['url'])
            language_color = language_colors.get(repo["language"], "000000")
            readme_content += (
                '<table>\n'
                '  <tr>\n'
                '    <td>\n'
                f'      <h3><a href="{repo["url"]}">{repo["name"]}</a></h3>\n'
                f'      {repo.get("description", "")}<br><br>\n'
                '      ____________________________________________________________<br><br>\n'
                '    </td>\n'
                '  </tr>\n'
                '  <tr>\n'
                '    <td>\n'
                f'      <img src="https://via.placeholder.com/12/{language_color}/000000?text=+"></img>&nbsp;'
                f'{repo["language"]}&nbsp;&nbsp;&nbsp;&nbsp;★ {star_count}\n'
                '    </td>\n'
                '  </tr>\n'
                '</table>\n<br>\n'
            )
        readme_content += '<br>\n'
    return readme_content

# Write README.md
readme_content = generate_readme(config)
with open('README.md', 'w') as readme_file:
    readme_file.write(readme_content)

print("README.md has been generated successfully.")
