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
OUTPUT_DIR = "./output"


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
    """pyATS and Batfish integration."""

    def save_result(self, output, file_name):
        output_file = os.path.join(OUTPUT_DIR, f"{self.device.alias}_{file_name}")
        output.to_csv(f"{output_file}.csv")
        output.to_json(f"{output_file}.json", indent=4)
        output.to_html(f"{output_file}.html")

    def run_batfish_question(self, question, file_name):
        try:
            if hasattr(self.bf.q, question) and callable(
                func := getattr(self.bf.q, question)
            ):
                result = func().answer().frame()
                self.save_result(result, file_name)
        except Exception as error:
            log.error(
                f"Error running Batfish question {question} on device {self.device.alias}:\n{error}"
            )

    @aetest.test
    def setup(self, testbed, device_name):
        """Testcase Setup section"""
        # connect to device
        self.device = testbed.devices[device_name]

    @aetest.test
    def get_running_config(self):
        self.raw_running_config = self.device.execute("show run")

    @aetest.test
    def save_running_config(self):
        with open(f"{ SNAPSHOT_PATH }/configs/{ self.device.alias }.cfg", "w") as fh:
            fh.write(self.raw_running_config)

    @aetest.test
    def establish_session(self):
        self.bf = Session(host="batfish")

    @aetest.test
    def init_snapshot(self):
        self.bf.init_snapshot(SNAPSHOT_PATH, overwrite=True)

    @aetest.test
    def load_batfish_questions(self):
        questions = [
            {"question": "nodeProperties", "file_name": "node_properties"},
            {"question": "interfaceProperties", "file_name": "interface_properties"},
            {"question": "bgpProcessConfiguration", "file_name": "bgp_process_configuration"},
            {"question": "bgpPeerConfiguration", "file_name": "bgp_peer_configuration"},
            {"question": "hsrpProperties", "file_name": "hsrp_properties"},
            {"question": "ospfProcessConfiguration", "file_name": "ospf_process_configuration"},
            {"question": "ospfAreaConfiguration", "file_name": "ospf_area_configuration"},
            {"question": "ospfInterfaceConfiguration", "file_name": "ospf_interface_configuration"},
            {"question": "mlagProperties", "file_name": "mlag_properties"},
            {"question": "namedStructures", "file_name": "named_structures"},
            {"question": "definedStructures", "file_name": "defined_structures"},
            {"question": "referencedStructures", "file_name": "referenced_structures"},
            {"question": "undefinedReferences", "file_name": "undefined_references"},
            {"question": "unusedStructures", "file_name": "unused_structures"},
            {"question": "switchedVlanProperties", "file_name": "switched_vlan_properties"},
            {"question": "vrrpProperties", "file_name": "vrrp_properties"},
        ]
        aetest.loop.mark(self.ask_batfish_question, question=questions)

    @aetest.test
    def ask_batfish_question(self, section, question):
        section.uid = question["question"]
        self.run_batfish_question(question["question"], question["file_name"])


class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect_from_devices(self, testbed):
        testbed.disconnect()


# for running as its own executable
if __name__ == "__main__":
    aetest.main()
