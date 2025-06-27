import subprocess
import sys
import os

# --- Configuration ---
# Define the sequence of scripts to run for the preparation pipeline.
# The paths are relative to the 'scripts' subfolder.
PIPELINE_STEPS = [
    "download_and_process.py",
    "merge_labels.py"
]
# -------------------

def run_script(script_path):
    """Executes a Python script using the same Python interpreter and waits for it to complete."""
    print("\n" + "="*80)
    print(f"--- Running Step: {os.path.basename(script_path)}")
    print("="*80 + "\n")

    if not os.path.exists(script_path):
        print(f"Error: Script not found at '{script_path}'. Aborting.")
        return False

    try:
        # sys.executable ensures we use the same python that is running this script
        process = subprocess.run(
            [sys.executable, script_path],
            check=True,
            text=True
        )
        print(f"\nStatus: Step '{os.path.basename(script_path)}' finished successfully.")
        return True
    except Exception as e:
        print(f"An error occurred while running {script_path}: {e}")
        return False

def main():
    """Runs all steps in the data preparation pipeline."""
    print("--- Starting Data Preparation Pipeline ---")

    for script in PIPELINE_STEPS:
        if not run_script(script):
            print("\nPipeline stopped due to an error in the previous step.")
            # Stop the entire process if a step fails
            sys.exit(1)

    print("\n--- Data Preparation Pipeline Finished ---")
    print("The 'frames' directory is now ready with images and corresponding labels.")

if __name__ == '__main__':
    main()
