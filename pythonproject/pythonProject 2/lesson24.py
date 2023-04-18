class VotersElligiblity(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

try:
    age = int(input("Enter age:"))
    
    print("Age is",age)
    if age < 18:
        raise VotersElligiblity
except VotersElligiblity:
    print("Age is less than 18")
else:
    print("Age is greater than or equal to 18")
finally:
    print("\nThe end of the procces")