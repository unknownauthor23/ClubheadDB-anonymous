import subprocess
import sys
import os

# --- Configuration ---
# Define the sequence of scripts to run for the preparation pipeline.
# The paths are relative to this script's location.
PIPELINE_STEPS = [
    "download_and_process.py",
    "merge_labels.py"
]
# -------------------

def run_script(script_path):
    """Executes a Python script using the same Python interpreter and waits for it to complete."""
    print("\n" + "="*80)
    print(f"--- Running Script: {script_path}")
    print("="*80 + "\n")

    # Ensure the script exists before trying to run it
    if not os.path.exists(script_path):
        print(f"Error: Script not found at '{script_path}'. Aborting.")
        return False

    try:
        # sys.executable ensures we use the same python that is running this script
        # This makes it robust to virtual environments.
        process = subprocess.run(
            [sys.executable, script_path],
            check=True, # This will raise an exception if the script returns a non-zero exit code (i.e., fails)
            text=True
        )
        print(f"\nStatus: Script '{script_path}' finished successfully.")
        return True
    except FileNotFoundError:
        print(f"Error: Could not find the Python interpreter at '{sys.executable}'.")
        return False
    except subprocess.CalledProcessError as e:
        print(f"Error: Script '{script_path}' failed with exit code {e.returncode}.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred while running {script_path}: {e}")
        return False

def main():
    """Runs all steps in the data preparation pipeline."""
    print("--- Starting Data Preparation Pipeline ---")

    for script in PIPELINE_STEPS:
        if not run_script(script):
            print("\nPipeline stopped due to an error in the previous step.")
            break

    print("\n--- Data Preparation Pipeline Finished ---")

if __name__ == '__main__':
    main()
