"""Django templates for CWR generation.

Attributes:
    TEMPLATES_21 (dict): Record templates for CWR 2.1
"""

from django.template import Template

TEMPLATES_21 = {
    'HDR': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'HDRPB{{ publisher_ipi_name|slice:"2:" }}'
        '{{ publisher_name|ljust:45 }}01.10{{ creation_date|date:"Ymd" }}'
        '{{ creation_date|date:"His" }}{{ creation_date|date:"Ymd" }}'
        '               \r\n{% endautoescape %}'),
    'GRH': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'GRH{{ transaction_type|ljust:3 }}0000102.10'
        '0000000000  \r\n{% endautoescape %}'),
    'WRK': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        '{{ record_type }}'
        '{{ transaction_sequence|rjust:8 }}00000000'
        '{{ work_title|ljust:60 }}  {{ work_id|ljust:14 }}'
        '{{ iswc|ljust:11 }}00000000            UNC'
        '{{ duration|date:"His"|default:"000000" }}{{ recorded_indicator }}'
        '      {{ version_type }}  ' + ' ' * 40 + 'N00000000000' +
        ' ' * 51 + 'N'
        '\r\n{% endautoescape %}'),
    'SPU': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'SPU{{ transaction_sequence|rjust:8 }}'
        '{{ record_sequence|rjust:8 }}{{ sequence|rjust:2 }}'
        '{{ publisher_id|ljust:9 }}{{ publisher_name|ljust:45 }}'
        ' E 000000000{{ publisher_ipi_name|rjust:11 }}              '
        '{{ publisher_pr_society|soc }}{{ share|prshare }}'
        '{{ publisher_mr_society|soc }}{{ share|mrshare }}'
        '{{ publisher_sr_society|soc }}{{ share|mrshare }}'
        ' N {{ publisher_ipi_base|ljust:13 }}                               '
        '\r\n{% endautoescape %}'),
    'SPT': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'SPT{{ transaction_sequence|rjust:8 }}'
        '{{ record_sequence|rjust:8 }}{{ publisher_id|ljust:9 }}'
        '      {{ share|prshare }}{{ share|mrshare }}{{ share|mrshare }}'
        'I2136N001\r\n{% endautoescape %}'),
    'SWR': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'SWR{{ transaction_sequence|rjust:8 }}'
        '{{ record_sequence|rjust:8 }}{{ code|ljust:9 }}'
        '{{ last_name|ljust:45 }}{{ first_name|ljust:30 }} '
        '{{ capacity|ljust:2 }}000000000{{ ipi_name|rjust:11 }}'
        '{{ pr_society|soc }}{{ share|prshare }}'
        '   00000   00000 N  {{ ipi_base|ljust:13 }}             \r\n'
        '{% endautoescape %}'),
    'SWT': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'SWT{{ transaction_sequence|rjust:8 }}'
        '{{ record_sequence|rjust:8 }}{{ code|ljust:9 }}'
        '{{ share|prshare }}0000000000I2136N001\r\n{% endautoescape %}'),
    'PWR': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'PWR{{ transaction_sequence|rjust:8 }}'
        '{{ record_sequence|rjust:8 }}{{ publisher_id|ljust:9 }}'
        '{{ publisher_name|ljust:45 }}              {{ saan|ljust:14 }}'
        '{{ code|ljust:9 }}\r\n{% endautoescape %}'),
    'OPU': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'OPU{{ transaction_sequence|rjust:8 }}'
        '{{ record_sequence|rjust:8 }}{{ sequence|rjust:2 }}' +
        ' ' * 54 +
        'YE 00000000000000000000              '
        '   {{ share|prshare }}'
        '   {{ share|mrshare }}'
        '   {{ share|mrshare }}'
        ' N                                             '
        '\r\n{% endautoescape %}'),
    'OPT': Template(''),
    'OWT': Template(''),
    'OWR': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'OWR{{ transaction_sequence|rjust:8 }}'
        '{{ record_sequence|rjust:8 }}{{ interested_party_number|ljust:9 }}'
        '{{ last_name|ljust:45 }}{{ first_name|ljust:30 }}'
        '{{ writer_unknown_indicator|default:" "}}'
        '{{ capacity|ljust:2 }}000000000{{ ipi_name|rjust:11 }}'
        '{{ pr_society|soc }}{{ share|mrshare }}'
        '{{ mr_society|soc }}{{ share|mrshare }}'
        '{{ sr_society|soc }}{{ share|mrshare }}    '
        '{{ ipi_base|ljust:13 }}             \r\n{% endautoescape %}'),
    'ALT': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'ALT{{ transaction_sequence|rjust:8 }}'
        '{{ record_sequence|rjust:8 }}{{ alternate_title|ljust:60 }}AT  '
        '\r\n{% endautoescape %}'),
    'VER': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'VER{{ transaction_sequence|rjust:8 }}'
        '{{ record_sequence|rjust:8 }}{{ work_title|ljust:60 }}' +
        ' ' * (11 + 2 + 45 + 30 + 60 + 11 + 13 + 45 + 30 + 11 + 13 + 14) +
        '\r\n{% endautoescape %}'),
    'PER': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'PER{{ transaction_sequence|rjust:8 }}'
        '{{ record_sequence|rjust:8 }}{{ last_name|ljust:45 }}'
        '{{ first_name|ljust:30 }}                        \r\n'
        '{% endautoescape %}'),
    'REC': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'REC{{ transaction_sequence|rjust:8 }}'
        '{{ record_sequence|rjust:8 }}'
        '{{ release_date|default:"00000000" }}' +
        ' ' * 60 + '{{ duration|rjust:6|default:"000000" }}     '
        '{{ album_title|ljust:60 }}'
        '{{ album_label|ljust:60 }}                  {{ ean|ljust:13 }}'
        '{{ isrc|ljust:12 }}     \r\n{% endautoescape %}'),
    'ORN': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'ORN{{ transaction_sequence|rjust:8 }}'
        '{{ record_sequence|rjust:8 }}LIB' + ' ' * 60 +
        '{{ cd_identifier|ljust:15 }}0000{{ library|ljust:60 }}' +
        ' ' * (26 + 12 + 60 + 20) + '0000                  \r\n'
        '{% endautoescape %}'),
    'GRT': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'GRT00001{{ transaction_count|rjust:8 }}'
        '{{ record_count|rjust:8 }}   0000000000\r\n{% endautoescape %}'),
    'TRL': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'TRL00001{{ transaction_count|rjust:8 }}'
        '{{ record_count|rjust:8 }}{% endautoescape %}'),
}

TEMPLATES_30 = {
    'HDR': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'HDRPB{{ publisher_id|ljust:4 }}'
        '{{ publisher_name|ljust:45 }}' + ' ' * 11 +
        '{{ creation_date|date:"Ymd" }}'
        '{{ creation_date|date:"His" }}{{ creation_date|date:"Ymd" }}' +
        ' ' * 15 + '3.0000' + ' ' * 60 +
        '{{ filename|ljust:27 }}\r\n{% endautoescape %}'),
    'GRH': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'GRHWRK0000103.000000000000\r\n{% endautoescape %}'),
    'WRK': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'WRK{{ transaction_sequence|rjust:8 }}00000000'
        '{{ work_title|ljust:60 }}  {{ work_id|ljust:14 }}'
        '{{ iswc|ljust:11 }}00000000            UNC'
        '{{ duration|date:"His"|default:"000000" }}{{ recorded_indicator }}'
        '      {{ version_type }}N00000000000' + ' ' * 51 + 'N'
        '\r\n{% endautoescape %}'),
    'SPU': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'SPU{{ transaction_sequence|rjust:8 }}'
        '{{ record_sequence|rjust:8 }}{{ sequence|rjust:2 }}'
        '{{ publisher_id|ljust:9 }}{{ publisher_name|ljust:45 }}'
        'NE 000000000{{ publisher_ipi_name|rjust:11 }}'
        '{{ publisher_ipi_base|ljust:13 }} \r\n{% endautoescape %}'),
    'SPT': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'SPT{{ transaction_sequence|rjust:8 }}'
        '{{ record_sequence|rjust:8 }}001{{ publisher_id|ljust:9 }}'
        '{{ share|prshare }}{{ share|mrshare }}{{ share|mrshare }}'
        'I2136{{ publisher_pr_society|ljust:4 }}'
        '{{ publisher_mr_society|ljust:4 }}{{ publisher_sr_society|ljust:4 }}'
        + ' ' * 32 + '0000\r\n{% endautoescape %}'),
    'SWR': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'SWR{{ transaction_sequence|rjust:8 }}'
        '{{ record_sequence|rjust:8 }}{{ code|ljust:9 }}'
        '{{ last_name|ljust:45 }}{{ first_name|ljust:30 }}N'
        '{{ capacity|ljust:2 }}000000000{{ ipi_name|rjust:11 }}'
        '{{ ipi_base|ljust:13 }} N  \r\n'
        '{% endautoescape %}'),
    'SWT': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'SWT{{ transaction_sequence|rjust:8 }}'
        '{{ record_sequence|rjust:8 }}001{{ code|ljust:9 }}'
        '{{ share|prshare }}0000000000'
        'I2136{{ pr_society|ljust:4 }}        '
        + ' ' * 32 + '0000\r\n{% endautoescape %}'),
    'OWT': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'OWT{{ transaction_sequence|rjust:8 }}'
        '{{ record_sequence|rjust:8 }}001{{ code|ljust:9 }}'
        '{{ share|mrshare }}{{ share|mrshare }}{{ share|mrshare }}'
        'I2136            '
        + ' ' * 32 + '0000\r\n{% endautoescape %}'),
    'PWR': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'PWR{{ transaction_sequence|rjust:8 }}'
        '{{ record_sequence|rjust:8 }}'
        '{{ publisher_sequence|rjust:2 }}{{ publisher_id|ljust:9 }}'
        '{{ code|ljust:9 }}' + ' ' * 14 + '{{ publisher_pr_society|ljust:4 }}'
        '{{ saan|ljust:14 }}  \r\n{% endautoescape %}'),
    'OPU': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'OPU{{ transaction_sequence|rjust:8 }}'
        '{{ record_sequence|rjust:8 }}{{ sequence|rjust:2 }}' +
        ' ' * 54 +
        'YE 00000000000000000000              \r\n{% endautoescape %}'),
    'OPT': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'OPT{{ transaction_sequence|rjust:8 }}'
        '{{ record_sequence|rjust:8 }}001         '
        '{{ share|prshare }}{{ share|mrshare }}{{ share|mrshare }}'
        'I2136' + ' ' * 44 + '0000\r\n{% endautoescape %}'),
    'OWR': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'OWR{{ transaction_sequence|rjust:8 }}'
        '{{ record_sequence|rjust:8 }}{{ code|ljust:9 }}'
        '{{ last_name|ljust:45 }}{{ first_name|ljust:30 }}'
        '{{ writer_unknown_indicator|default:"N"}}'
        '{{ capacity|ljust:2 }}000000000{{ ipi_name|rjust:11 }}'
        '{{ ipi_base|ljust:13 }} N  \r\n'
        '{% endautoescape %}'),
    'ALT': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'ALT{{ transaction_sequence|rjust:8 }}'
        '{{ record_sequence|rjust:8 }}{{ alternate_title|ljust:60 }}AT  '
        '\r\n{% endautoescape %}'),
    'VER': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'VER{{ transaction_sequence|rjust:8 }}'
        '{{ record_sequence|rjust:8 }}{{ work_title|ljust:60 }}' +
        ' ' * (11 + 2 + 45 + 30 + 60 + 11 + 13 + 45 + 30 + 11 + 13 + 14) +
        '\r\n{% endautoescape %}'),
    'PER': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'PER{{ transaction_sequence|rjust:8 }}'
        '{{ record_sequence|rjust:8 }}{{ last_name|ljust:45 }}'
        '{{ first_name|ljust:30 }}                        \r\n'
        '{% endautoescape %}'),
    'REC': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'REC{{ transaction_sequence|rjust:8 }}'
        '{{ record_sequence|rjust:8 }}'
        '{{ release_date|default:"00000000" }}' +
        ' ' * 60 + '{{ duration|rjust:6|default:"000000" }}     '
        '{{ album_title|ljust:60 }}'
        '{{ album_label|ljust:60 }}                  {{ ean|ljust:13 }}'
        '{{ isrc|ljust:12 }}     \r\n{% endautoescape %}'),
    'ORN': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'ORN{{ transaction_sequence|rjust:8 }}'
        '{{ record_sequence|rjust:8 }}LIB' + ' ' * 60 +
        '{{ cd_identifier|ljust:15 }}0000{{ library|ljust:60 }}' +
        ' ' * (26 + 12 + 60 + 20) + '0000                  \r\n'
        '{% endautoescape %}'),
    'GRT': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'GRT00001{{ transaction_count|rjust:8 }}'
        '{{ record_count|rjust:8 }}\r\n{% endautoescape %}'),
    'TRL': Template(
        '{% load cwr_filters %}{% autoescape off %}'
        'TRL00001{{ transaction_count|rjust:8 }}'
        '{{ record_count|rjust:8 }}{% endautoescape %}'),
}
