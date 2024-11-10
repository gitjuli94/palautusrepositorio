from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        parsed_toml = toml.loads(content)
        #print(parsed_toml)

        poetry_data = parsed_toml.get("tool", {}).get("poetry", {})
        name = poetry_data.get("name")
        description = poetry_data.get("description")
        license = poetry_data.get("license")
        authors = poetry_data.get("authors")
        dependencies = list(poetry_data.get("dependencies", {}).keys())
        dev_dependencies = list(poetry_data.get("group", {}).get("dev", {}).get("dependencies", {}).keys())

        # Return the Project object
        return Project(name, description, license, authors, dependencies, dev_dependencies)

