import random
import sys

def load_all_stories():
    stories = {
        "horror": {
            "characters": ["A lonely ghost", "A nervous night guard", "A lost traveler", "A creepy doll"],
            "actions": ["heard a strange whisper", "found a mysterious old book", "ran from a dark shadow", "saw a door slam shut"],
            "places": ["in a haunted mansion", "in an abandoned hospital", "in a foggy graveyard", "in a dark, endless forest"],
            "climaxes": ["and was never seen again.", "but it was only a black cat.", "and woke up from the nightmare.", "and the whispering stopped."]
        },
        "comedy": {
            "characters": ["A clumsy detective", "A talking squirrel", "A chef who hates food", "A robot trying to be human"],
            "actions": ["slipped on a banana peel", "tried to bake a cake", "wore two different shoes", "accidentally joined a circus"],
            "places": ["at a fancy party", "in the middle of a supermarket", "on live TV", "during a very serious meeting"],
            "climaxes": ["and everyone burst out laughing.", "but ended up with a pie on their face.", "and accidentally became famous.", "and realized it was all a dream."]
        },
        "adventure": {
            "characters": ["A brave knight", "A clever explorer", "A pirate with a secret map", "A young wizard"],
            "actions": ["discovered a hidden cave", "climbed the tallest mountain", "sailed across the stormy sea", "outsmarted a dragon"],
            "places": ["to find a lost treasure", "in a jungle full of strange creatures", "on a floating island", "deep within a volcano"],
            "climaxes": ["and found the legendary Golden Pineapple.", "and saved the day.", "and returned home a hero.", "and began a new journey."]
        }
    }
    return stories

def show_menu():
    print("\n--- Random Story Generator ---")
    print("What kind of story do you want?")
    print("1. Horror")
    print("2. Comedy")
    print("3. Adventure")
    print("4. Exit")

def generate_story(category, story_db):
    try:
        category_parts = story_db[category]

        character = random.choice(category_parts["characters"])
        action = random.choice(category_parts["actions"])
        location = random.choice(category_parts["places"])
        ending = random.choice(category_parts["climaxes"])
        
        story = f"\nOnce upon a time... {character} {action} {location} {ending}"
        
        print(story)
        
    except KeyError:
        print(f"Error: Story category '{category}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    all_stories = load_all_stories()
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            generate_story("horror", all_stories)
        elif choice == '2':
            generate_story("comedy", all_stories)
        elif choice == '3':
            generate_story("adventure", all_stories)
        elif choice == '4':
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
