# yatfish
Combining Cisco pyATS and Batfish for automated network running configuration analysis

# Requirements
WSL2 Ubuntu and Docker Desktop for Windows
Or any Linux environment with Docker

## Steps
1. Clone the repository 
2. Update the testbed.yaml to reflect your topology and devices
3. Docker build -t <your docker handle >/yatfish -f docker/Dockerfile . --no-cache
4. Docker push <your handle>/yatfish
5. Docker-compose up 
6. In Docker Desktop Volumes - yatfish Volume - Data - Save As to retrieve analysis