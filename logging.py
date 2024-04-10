import logging

# Configure logging
logging.basicConfig(filename='data_pipeline.log', level=logging.INFO)

# Example usage of logging
try:
    # Data processing code
    logging.info('Data processing successful.')
except Exception as e:
    logging.error(f'Error processing data: {e}')
