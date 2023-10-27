# -*- coding: utf-8 -*-

import os
import sys
import glob
import subprocess
import xml.etree.ElementTree as ET
import configparser
import zipfile
import shutil
from PIL import Image

config = configparser.ConfigParser()
config.read(sys.argv[1])
path_to_game = config['Game']['folder']
print(path_to_game)

xml_root = ET.parse(os.path.join(path_to_game, 'game_info.xml'))
xml_version = xml_root.findall(".//version[@name='client']")
version = xml_version[0].attrib['installed']
print(version)

base_dir = os.path.abspath(os.path.dirname(__file__))
tmp_dir = os.path.join(base_dir, 'tmp')
os.makedirs(tmp_dir, exist_ok=True)

# Clean up tmp folder
files = glob.glob(os.path.join(tmp_dir, '*'))
for f in files:
    os.remove(f)

empty_image = os.path.join(tmp_dir, 'empty.dds')
flag = Image.new('RGBA', (4, 4), (0, 0, 0, 0))
flag.save(empty_image, "DDS")

output = subprocess.check_output([
        'wowsunpack.exe',
        '-l', os.path.join(path_to_game, "bin", version.split(".")[-1], "idx"),
        '-I', 'content/gameplay/common/flags/*.*',
        '-p', '..\\..\\..\\res_packages',
    ],
).decode()

c = 0;
zip_archive = os.path.join(tmp_dir, 'flags.zip')
with zipfile.ZipFile(zip_archive, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for line in output.split("\n"):
        line = line.rstrip()
        if line.count('/') == 4:
            zipf.write(empty_image, line)
            c = c + 1

target_dir = config['Destination']['folder']
suffix = config['Destination']['suffix']
target_file = 'noflags-' + version + '-' + suffix + '.zip'
target = os.path.join(target_dir, target_file)
print(target, c)
shutil.copy2(zip_archive, target)
