# yatfish
Combining Cisco pyATS and Batfish for automated network running configuration analysis

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/automateyournetwork/yatfish)

[![Run in Cisco Cloud IDE](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-runable-icon.svg)](https://developer.cisco.com/devenv/?id=devenv-vscode-base&GITHUB_SOURCE_REPO=https://github.com/automateyournetwork/yatfish)

# Requirements
WSL2 Ubuntu and Docker Desktop for Windows
Or any Linux environment with Docker

## Steps
1. Clone the repository 
2. Update the testbed.yaml to reflect your topology and devices
3. docker build -t <your docker handle >/yatfish -f docker/Dockerfile . --no-cache
4. docker push <your handle>/yatfish
5. docker-compose up 
6. In Docker Desktop Volumes - yatfish Volume - Data - Save As to retrieve analysis

If you need to run this 'hands-off' and make zero touch es to your devices you can adjust the testbed.connect() command as follows:

testbed.connect(init_exec_commands=[],
               init_config_commands=[],
               log_stdout=False)

## Batfish Questions asked per configuration

bf.q.nodeProperties()

bf.q.interfaceProperties()

bf.q.bgpProcessConfiguration()

bf.q.bgpPeerConfiguration()

bf.q.undefinedReferences()

bf.q.unusedStructures()

bf.q.hsrpProperties()

bf.q.ospfProcessConfiguration()

bf.q.ospfInterfaceConfiguration()

bf.q.ospfAreaConfiguration()

bf.q.switchedVlanProperties()

bf.q.mlagProperties()

bf.q.namedStructures()

bf.q.definedStructures()

bf.q.referencedStructures()

bf.q.vrrpProperties()
