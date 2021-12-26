import xml.etree.ElementTree as ET


def get_data(node_name):
    root = ET.parse("../config_files/config_setting.xml").getroot()
    return root.find(".//" + node_name).text
