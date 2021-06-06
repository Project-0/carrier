from jinja2 import Template
from os import environ, getenv


class YAMLComposer(object):
    """ Defines a class to convert YAML templates into docker-compose files

    """

    import_path = getenv('IMPORT_PATH', "/usr/lib/carrier/templates/")
    export_path = getenv('EXPORT_PATH', '/var/carrier/strains/')

    def __init__(self, source_template):
        """Creates an instance of the YAMLComposer
        """
        self._template_kwargs = dict(
            filename=f"{self.import_path}{source_template}",
            mode="r"
        )

    def make(self, output_path, **kwargs):
        """Generates a docker-compose.yaml file at output_path
        """

        template = None
        with open(**self._template_kwargs) as template_file:
            template = template_file.read()

        if not template:
            raise ValueError(str)

        self.rendered_template = Template(template).render(**kwargs)

        with open(
            filename=f"{self.export_path}{output_path}/docker-compose.yaml", 
            mode="w") as outfile:
            outfile.write(self.rendered_template)
