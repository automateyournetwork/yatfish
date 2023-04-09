import os
import json
import logging
import pandas as pd
from pyats import aetest
from pyats.log.utils import banner
from pybatfish.client.session import Session
from pybatfish.datamodel import *
from pybatfish.datamodel.answer import *
from pybatfish.datamodel.flow import *

# ----------------
# Get logger for script
# ----------------

log = logging.getLogger(__name__)

# Batfish Variables
SNAPSHOT_PATH = "./snapshot"
output_dir = "./output"

# ----------------
# AE Test Setup
# ----------------
class common_setup(aetest.CommonSetup):
    """Common Setup section"""
# ----------------
# Connected to devices
# ----------------
    @aetest.subsection
    def connect_to_devices(self, testbed):
        """Connect to all the devices"""
        testbed.connect()
# ----------------
# Mark the loop for Input Discards
# ----------------
    @aetest.subsection
    def loop_mark(self, testbed):
        aetest.loop.mark(Yatfish, device_name=testbed.devices)

# ----------------
# Test Case #1
# ----------------
class Yatfish(aetest.Testcase):
    """Parse all pyATS learn config and learn interfaces data"""

    @aetest.test
    def setup(self, testbed, device_name):
        """ Testcase Setup section """
        # connect to device
        self.device = testbed.devices[device_name]
        # Loop over devices in tested for testing
    
    @aetest.test
    def get_running_config(self):
        self.raw_running_config = self.device.execute("show run")

    @aetest.test
    def save_running_config(self):
        with open(f"{ SNAPSHOT_PATH }/configs/{ self.device.alias }.cfg", "w") as fh:
            fh.write(self.raw_running_config)
            fh.close()

    @aetest.test
    def establish_session(self):
        self.bf = Session(host="batfish")

    @aetest.test
    def init_snapshot(self):
        self.bf.init_snapshot(SNAPSHOT_PATH, overwrite=True)
    
    @aetest.test
    def node_properties(self):
        self.node_result = self.bf.q.nodeProperties().answer().frame()

    @aetest.test
    def save_node_results(self):
        self.node_result.to_csv(f"{ output_dir }/{ self.device.alias }_node_properties.csv")
        self.node_result.to_json(f"{ output_dir }/{ self.device.alias }_node_properties.json", indent=4)
        self.node_result.to_html(f"{ output_dir }/{ self.device.alias }_node_properties.html")

    @aetest.test
    def interface_properties(self):
        self.interface_result = self.bf.q.interfaceProperties().answer().frame()

    @aetest.test
    def save_interface_results(self):
        self.interface_result.to_csv(f"{ output_dir }/{ self.device.alias }_interface_properties.csv")
        self.interface_result.to_json(f"{ output_dir }/{ self.device.alias }_interface_properties.json", indent=4)
        self.interface_result.to_html(f"{ output_dir }/{ self.device.alias }_interface_properties.html")

    @aetest.test
    def undefined_references(self):
        self.undefined_result = self.bf.q.undefinedReferences().answer().frame()

    @aetest.test
    def save_undefined_results(self):
        self.undefined_result.to_csv(f"{ output_dir }/{ self.device.alias }_undefined_results.csv")
        self.undefined_result.to_json(f"{ output_dir }/{ self.device.alias }_undefined_results.json", indent=4)
        self.undefined_result.to_html(f"{ output_dir }/{ self.device.alias }_undefined_results.html")

    @aetest.test
    def unused_structures(self):
        self.unused_result = self.bf.q.unusedStructures().answer().frame()

    @aetest.test
    def save_unused_structures(self):
        self.unused_result.to_csv(f"{ output_dir }/{ self.device.alias }_unused_structures.csv")
        self.unused_result.to_json(f"{ output_dir }/{ self.device.alias }_unused_structures.json", indent=4)
        self.unused_result.to_html(f"{ output_dir }/{ self.device.alias }_unused_structures.html")

    @aetest.test
    def hsrpProperties(self):
        self.hsrp_result = self.bf.q.hsrpProperties().answer().frame()

    @aetest.test
    def save_hsrp_result(self):
        self.hsrp_result.to_csv(f"{ output_dir }/{ self.device.alias }_hsrp_result.csv")
        self.hsrp_result.to_json(f"{ output_dir }/{ self.device.alias }_hsrp_result.json", indent=4)
        self.hsrp_result.to_html(f"{ output_dir }/{ self.device.alias }_hsrp_result.html")

    @aetest.test
    def ospfProcessConfiguration(self):
        self.ospfProcess_result = self.bf.q.ospfProcessConfiguration().answer().frame()

    @aetest.test
    def save_ospfProcess_result(self):
        self.ospfProcess_result.to_csv(f"{ output_dir }/{ self.device.alias }_ospfProcess_result.csv")
        self.ospfProcess_result.to_json(f"{ output_dir }/{ self.device.alias }_ospfProcess_result.json", indent=4)
        self.ospfProcess_result.to_html(f"{ output_dir }/{ self.device.alias }_ospfProcess_result.html")

    @aetest.test
    def ospfInterfaceConfiguration(self):
        self.ospfInterface_result = self.bf.q.ospfInterfaceConfiguration().answer().frame()

    @aetest.test
    def save_ospfInterface_result(self):
        self.ospfInterface_result.to_csv(f"{ output_dir }/{ self.device.alias }_ospfInterface_result.csv")
        self.ospfInterface_result.to_json(f"{ output_dir }/{ self.device.alias }_ospfInterface_result.json", indent=4)
        self.ospfInterface_result.to_html(f"{ output_dir }/{ self.device.alias }_ospfInterface_result.html")

    @aetest.test
    def ospfAreaConfiguration(self):
        self.ospfArea_result = self.bf.q.ospfAreaConfiguration().answer().frame()

    @aetest.test
    def save_ospfArea_result(self):
        self.ospfArea_result.to_csv(f"{ output_dir }/{ self.device.alias }_ospfArea_result.csv")
        self.ospfArea_result.to_json(f"{ output_dir }/{ self.device.alias }_ospfArea_result.json", indent=4)
        self.ospfArea_result.to_html(f"{ output_dir }/{ self.device.alias }_ospfArea_result.html")

    @aetest.test
    def switchedVlanProperties(self):
        self.switchedVlanProperties_result = self.bf.q.switchedVlanProperties().answer().frame()

    @aetest.test
    def save_switchedVlanProperties_result(self):
        self.switchedVlanProperties_result.to_csv(f"{ output_dir }/{ self.device.alias }_switchedVlanProperties_result.csv")
        self.switchedVlanProperties_result.to_json(f"{ output_dir }/{ self.device.alias }_switchedVlanProperties_result.json", indent=4)
        self.switchedVlanProperties_result.to_html(f"{ output_dir }/{ self.device.alias }_switchedVlanProperties_result.html")

class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect_from_devices(self, testbed):
        testbed.disconnect()

# for running as its own executable
if __name__ == '__main__':
    aetest.main()