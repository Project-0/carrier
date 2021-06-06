#!/usr/bin/env python

from unittest import TestCase, mock

from carrier.models import YAMLComposer

mock_template = """# For testing only
version: "{{ version }}"
"""

class TestYAMLComposer(TestCase):
    @mock.patch(
        "builtins.open", 
        new_callable=mock.mock_open, 
        read_data=mock_template
    )
    def test_make(self, mocked_open):
        with mock.patch.dict(
            'os.environ', 
            {
                'IMPORT_PATH': '/usr/lib/carrier/templates/',
                'EXPORT_PATH': '/var/carrier/strains/'
            }
        ):
            converter = YAMLComposer('atlanta-carrier.yaml')
            self.assertDictEqual(
                d1=converter._template_kwargs,
                d2=dict(
                    filename=(
                        "/usr/lib/carrier/templates/"
                        "atlanta-carrier.yaml"
                    ),
                    mode="r"
                )
            )

            converter.make('test', version="3")

            mocked_open.assert_any_call(
                filename='/usr/lib/carrier/templates/atlanta-carrier.yaml',
                mode='r'
            )

            mocked_open.assert_any_call(
                filename='/var/carrier/strains/test/docker-compose.yaml',
                mode='w'
            )

            self.assertEqual(
                first=converter.rendered_template,
                second="# For testing only\nversion: \"3\""
            )
            