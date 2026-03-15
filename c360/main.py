import sys
import importlib
from datamart.credit_card_datamart import create_seed  # Changed to relative import assuming module is in parent dir

def load_env_config(env):
    return importlib.import_module(f"config.{env}.config")

def main(args):
    env, system, table, operation, timestamp, start_time, end_time, dry_run = args
    dry_run = dry_run in ["True", "true", "1"] if isinstance(dry_run, str) else dry_run

    env_config = load_env_config(env)

    if operation == "create_seed":
        create_seed.run(env_config, system, table, operation, timestamp, start_time, end_time, dry_run)
    else:
        raise ValueError(f"Unsupported operation: {operation}")

if __name__ == "__main__":
    main(sys.argv[1:])