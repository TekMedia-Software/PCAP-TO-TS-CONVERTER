
import os
import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)

def generate_ts_from_pcap(file_paths):
    """
    Generate TS files from the given PCAP files and save them in the same directory.
    """
    for pcap_file in file_paths:
        try:
            # Get the output directory from the PCAP file path
            output_directory = os.path.dirname(pcap_file)
            base_name = os.path.splitext(os.path.basename(pcap_file))[0]
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            ts_filename = os.path.join(output_directory, f"{base_name}.ts")

            # Running the command to convert PCAP to TS
            command = f"tsp -I pcap '{pcap_file}' -O file '{ts_filename}'"
            logging.info(f"Processing PCAP file: {pcap_file}")
            logging.info(f"Running command: {command}")
            os.system(command)  # Use subprocess for better error handling in production
            
            logging.info(f"TS file generated successfully: {ts_filename}")
        except Exception as e:
            logging.error(f"Error processing {pcap_file}: {e}")
            return False, f"Error processing {pcap_file}: {e}"

    return True, "All TS files generated successfully in their source directory!."
