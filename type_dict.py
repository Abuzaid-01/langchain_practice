from typing import TypedDict

from dotenv import load_dotenv

load_dotenv()

class person(TypedDict):
    name: str
    age: int
    city: str

new_person: person = {
    "name": 1,
    "age": "hi",
    "city": "New York"
}
print(new_person)    