# Installation Guide

This document provides step-by-step instructions for installing and running the **PCAP to TS Converter** project.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python: Ensure you have Python installed (preferably Python 3.x) - (https://www.python.org/downloads/)
- PyQt5: This is the framework we'll use to build the GUI.
- TSDuck (TSTool): TSDuck is a set of tools for handling MPEG transport streams, and we use it to convert PCAP files into TS format. Since TSDuck is not a Python package, it needs to be installed separately. (https://tsduck.io/download/tsduck/)

## Installation Steps

1. **Clone the repository**:
```
git clone https://github.com/TekMedia-Software/PCAP-to-TS-Converter.git
```

2. **Navigate to the project directory**:
```
cd PCAP-to-TS-Converter
```

3. **Install dependencies**:

For Linux (Ubuntu/Debian):

- Installing Python:
```
sudo apt install python3.10
```
```
sudo apt-get install python3-pip
```
	
- Installing PyQt:
```
pip install PyQt5
```

- Installing TSDuck:
```
sudo apt-get update && sudo apt-get install tsduck
```

## Running the Project

To start the project after installation, use the following command:
```
python3 app.py
```
    
This will open the GUI, where you can select your PCAP files and initiate the conversion to TS files.
       
## Contact

If you encounter any issues or have questions regarding the installation, please contact:

- Awadh Bajpai - [awabaj@tekmediasoft.net](mailto:awabaj@tekmediasoft.net)
- Sushanthika Manikandan - [susman@tekmediasoft.net](mailto:susman@tekmediasoft.net)

