import sys
from core_engine import config, logger

def main():
    # Load configuration
    config.load_config()

    # Initialize logger
    logger.init_logger()

    # Run application
    application = config.get_application()
    application.run()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        sys.exit(1)