import requests
import json
import os

def get_user_data(per_page, username, page=1):
    url = f"https://gitlab.com/api/v4/users.json?search=&per_page={per_page}&username={username}&page={page}"
    response = requests.get(url)
    response.raise_for_status()  # exception handler
    return response.json()

def print_gitly_ascii_art():
    gitly_art = """
        #                      .-') _                         
        #                     (  OO) )                        
        #   ,----.     ,-.-') /     '._ ,--.       ,--.   ,--.
        #  '  .-./-')  |  |OO)|'--...__)|  |.-')    \  `.'  / 
        #  |  |_( O- ) |  |  \'--.  .--'|  | OO ) .-')     /  
        #  |  | .--, \ |  |(_/   |  |   |  |`-' |(OO  \   /   
        # (|  | '. (_/,|  |_.'   |  |  (|  '---.' |   /  /\_  
        #  |  '--'  |(_|  |      |  |   |      |  `-./  /.__) 
        #   `------'   `--'      `--'   `------'    `--'      
        #                _~ "crafted by Stevemats (@stevematindi)"
        # --------------------------------------------------------
    """
    print(gitly_art)

def colored_input(prompt):
    return input(f"\033[93m{prompt}\033[0m")

def main():
    try:
        print_gitly_ascii_art()

        per_page = int(colored_input("Enter the number of results per page: "))
        username = colored_input("Enter the username to search for: ")
        total_pages = int(colored_input("Enter the total number of pages to retrieve (0 for all): ") or 0)
        page = 1
        user_data = []

        while total_pages == 0 or page <= total_pages:
            page_data = get_user_data(per_page, username, page)
            user_data.extend(page_data)
            if len(page_data) < per_page:
                break
            page += 1

        # outputting to console
        print("\033[92mJSON Output:\033[0m")
        print(json.dumps(user_data, indent=4))

        # outputting to txt
        output_file = colored_input("Enter the output file name (user_data.txt by default): ") or "users.txt"
        output_file_path = os.path.abspath(output_file) #path to out file
        with open(output_file, "w") as file:
            json.dump(user_data, file, indent=4)

        print(f"Data saved to {output_file} at {output_file_path}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
