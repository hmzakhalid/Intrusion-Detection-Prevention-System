# Intrusion Detection and Prevention System (IDPS)
#### Author: [Hamza Khalid](https://github.com/hmzakhalid) 

This project is a basic Intrusion Detection and Prevention System (IDPS) designed to monitor various activities on a host system, detect suspicious behavior, and alert the user to possible threats. The IDPS includes file system, network, and process monitoring, as well as anomaly detection features.

## Features

1. Monitor file system changes (create, modify, delete, move) in a specified directory.
2. Monitor network connections.
3. Monitor system processes.
4. Anomaly detection based on the number of events in a short period and machine learning techniques (Isolation Forest algorithm).

## Installation

1. Clone the repository:
`git clone https://github.com/hmzakhalid/Intrusion-Detection-Prevention-System`
2. Install the required Python packages:
`pip install -r requirements.txt`

## Usage

1. Edit the `idps.py` script and set the `path` variable to the directories you want to monitor.

2. Run the IDPS:
`python idps.py`

The IDPS will begin monitoring the specified directory and the host system for any suspicious activity. Detected events will be logged in the following files:

- `file_system_log.txt`: File system changes
- `network_connections_log.txt`: Network connections
- `processes_log.txt`: System processes

Additionally, the IDPS will alert the user if an anomaly is detected based on the number of events in a short period or unusual event patterns recognized by the Isolation Forest algorithm.

## Customization

You can customize various aspects of the IDPS, such as the monitoring intervals, anomaly detection thresholds, and logging options, by editing the corresponding variables and parameters in the `idps.py`,  `monitor.py` and `detector.py` scripts.

## Limitations and Future Work

This IDPS is a basic implementation and has several limitations. The anomaly detection system could be further enhanced by incorporating more advanced machine learning algorithms, statistical models, or event pattern analysis. Integrating the IDPS with other security tools and platforms can also improve its effectiveness.



