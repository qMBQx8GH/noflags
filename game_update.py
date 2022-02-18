# -*- coding: utf-8 -*-

import os
import json
import requests
import subprocess
import xml.etree.ElementTree as ET
import configparser

config = configparser.ConfigParser()
config.read('build.ini')
path_to_game = config['Game']['folder']

xml_root = ET.parse(os.path.join(path_to_game, 'game_info.xml'))
xml_version = xml_root.findall("//version[@name='client']")
version = xml_version[0].attrib['installed']


content = [
    'content/gameplay/common/flags/*.*',
]
for d in content:
    subprocess.run([
        'wowsunpack.exe',
        '-x', os.path.join(path_to_game, "bin", version.split(".")[-1], "idx"),
        '-I', d,
        '-p', '..\\..\\..\\res_packages',
        '-o', 'res',
    ],
        shell=True,
    )
    print(d, 'OK')
