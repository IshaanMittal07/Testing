def create_invitation(name, date, location, theme, description):
    border = "=" * 60
    invitation = f"""
{border}
🎉 You're Invited to a Birthday Party! 🎉
{border}

Name: {name}
Date: {date}
Location: {location}
Theme: {theme}

Details:
{description}

We hope to see you there and celebrate together!

{border}
"""

    return invitation

def main():
    print("🎂 Birthday Invitation Card Creator 🎂\n")

    # Collect user input
    name = input("Enter the birthday person's name: ")
    date = input("Enter the date of the party (e.g., May 13, 2025): ")
    location = input("Enter the location of the party: ")
    theme = input("Enter the party theme: ")
    description = input("Enter a short description of the event: ")

    # Create invitation
    invitation = create_invitation(name, date, location, theme, description)

    # Display the invitation
    print("\nHere is your birthday invitation:\n")
    print(invitation)

    # Optionally save to file
    save = input("Would you like to save this invitation to a file? (yes/no): ").strip().lower()
    if save == 'yes':
        filename = f"{name.replace(' ', '_')}_birthday_invitation.txt"
        with open(filename, 'w') as file:
            file.write(invitation)
        print(f"Invitation saved as '{filename}'")

if __name__ == "__main__":
    main()
