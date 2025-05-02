import json
import os

# Define the path to the data directory relative to this script
# Assuming the script is run from the root of the repository or within the scripts/ directory
DATA_DIR = os.path.join(os.path.dirname(__file__), "../data/scripture")
FILE_NAME = "proverbs_15_1.json"
FILE_PATH = os.path.join(DATA_DIR, FILE_NAME)

def load_and_print_example(file_path):
    """Loads a JSON data file and prints example content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Assuming the file contains a list with at least one entry
        if isinstance(data, list) and len(data) > 0:
            entry = data[0] # Get the first entry

            print(f"--- Example Usage: Loading {FILE_NAME} ---")
            print(f"\nEntry ID: {entry.get('entry_id', 'N/A')}")
            print(f"Topic(s): {', '.join(entry.get('topic', []))}")
            print(f"\nContent Summary:\n{entry.get('content_summary', 'N/A')}")

            qa_pairs = entry.get('qa_pairs', [])
            if qa_pairs:
                print(f"\nExample Q&A Pair:")
                print(f"  Q: {qa_pairs[0].get('question', 'N/A')}")
                print(f"  A: {qa_pairs[0].get('answer', 'N/A')}")
            else:
                print("\nNo Q&A pairs found in this entry.")

        else:
            print(f"Error: File {file_path} does not contain a list of entries or is empty.")

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        print("Please ensure you are running this script from the repository root or adjust the path.")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Adjust path if running directly from scripts directory vs. root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    data_file_path = os.path.join(repo_root, "data", "scripture", FILE_NAME)
    
    # Check if running from root
    if not os.path.exists(data_file_path):
         data_file_path = os.path.join(script_dir, "..", "data", "scripture", FILE_NAME)

    load_and_print_example(data_file_path)


