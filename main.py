import random
import sys

def load_all_stories():
    stories = {
        "horror": {
            "openings": [
                "In a ramshackle house on the edge of town",
                "Late one night, during a violent thunderstorm",
                "Deep within the catacombs, where light never touches",
                "A single flickering candle lit the dusty attic"
            ],
            "characters": [
                "a young historian obsessed with a local legend",
                "a skeptical paranormal investigator",
                "a pair of teenagers who dared each other",
                "an old man who hadn't spoken in years"
            ],
            "problems": [
                "found a locked box that seemed to whisper",
                "realized they were not alone",
                "saw a face in a mirror that wasn't their own",
                "heard footsteps in the empty hall above them"
            ],
            "actions": [
                "to barricade the door and hide",
                "to try and communicate with the entity",
                "to find the source of the noise",
                "to run as fast as they could"
            ],
            "locations": [
                "into the flooded cellar",
                "up the rickety stairs to the forbidden room",
                "through a secret passage behind a bookcase",
                "out into the unnerving, silent graveyard"
            ],
            "climaxes": [
                "the door burst open, and a cold wind blew out the light",
                "they saw the final, terrifying truth and screamed",
                "it was all just a misunderstanding caused by an old pipe",
                "they escaped, vowing never to return"
            ]
        },
        "comedy": {
            "openings": [
                "It was a Tuesday, the most boring day, until",
                "At the annual 'Most Serious Person' competition",
                "In a kitchen full of angry, sentient vegetables",
                "The day the entire town's Wi-Fi was replaced by a single kazoo"
            ],
            "characters": [
                "a very confused penguin who thought he was a lawyer",
                "a grandma who was secretly a pro-wrestler",
                "a talking cat with a terrible sense of humor",
                "a knight who was afraid of butterflies"
            ],
            "problems": [
                "was suddenly put in charge of a runaway hot dog stand",
                "had to explain why there was a goat on the roof",
                "accidentally swapped briefcases with a birthday clown",
                "was mistaken for a famous pop star"
            ],
            "actions": [
                "to improvise a song and dance",
                "to disguise themselves as a potted plant",
                "to blame the talking cat for everything",
                "to simply nod and pretend they knew what was happening"
            ],
            "locations": [
                "right into the middle of a live news broadcast",
                "to a high-stakes bingo game",
                "to an elevator filled with opera singers",
                "all the way to a very confused dog park"
            ],
            "climaxes": [
                "they somehow won the competition and a lifetime supply of glitter",
                "the goat was given the key to the city",
                "it all turned out to be a reality TV show",
                "they just decided to take a nap right there"
            ]
        },
        "adventure": {
            "openings": [
                "On the coast of a forgotten island",
                "In a city built on the clouds",
                "A weathered map was found in an old library book",
                "The oldest tree in the forest began to speak"
            ],
            "characters": [
                "a daring pilot with a rusty airship",
                "a young scholar who could read ancient runes",
                "a grumpy warrior looking for one last quest",
                "a nimble thief with a heart of gold"
            ],
            "problems": [
                "was given a quest by a mysterious old wizard",
                "discovered that a powerful artifact was stolen",
                "heard rumors of a lost city made of crystal",
                "had to rescue a friend from a rival explorer"
            ],
            "actions": [
                "to charter a ship and face the storm",
                "to decode the ancient map",
                "to sneak into the fortress of the Sky Pirates",
                "to journey through the Whispering Desert"
            ],
            "locations": [
                "to the peak of the shaking volcano",
                "deep into the Sunken Temple",
                "across the great chasm on a rope bridge",
                "aboard a giant, friendly turtle"
            ],
            "climaxes": [
                "they found the treasure and shared it with the people",
                "they defeated the villain in a clever duel",
                "the map led to a beautiful, hidden waterfall",
                "they made it home just in time for dinner"
            ]
        }
    }
    return stories

def show_menu():
    print("\n==================================")
    print("--- Random Story Generator ---")
    print("==================================")
    print("What kind of story do you want?")
    print("1. Horror")
    print("2. Comedy")
    print("3. Adventure")
    print("4. Exit")

def generate_story(category, story_db):
    try:
        parts = story_db[category]

        opening = random.choice(parts["openings"])
        character = random.choice(parts["characters"])
        problem = random.choice(parts["problems"])
        action = random.choice(parts["actions"])
        location = random.choice(parts["locations"])
        ending = random.choice(parts["climaxes"])
        
        print("\n...Generating your story...")
        print("--------------------------------------------------")
        
        story = (
            f"{opening}, {character} {problem}. "
            f"They decided {action}, which led them {location}. "
            f"In the end, {ending}."
        )
        
        print(story)
        print("--------------------------------------------------")
        
        input("\n[Press Enter to return to the menu]...")
        
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