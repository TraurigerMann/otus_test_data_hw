import json
from csv import DictReader




with open("books.csv", "r") as csv_file:
    reader_for_length = DictReader(csv_file)

    #declare the length of csv-file
    books_data_len = len(list(reader_for_length))

with open("users.json", "r") as json_file:
    user_data = json.loads(json_file.read())

    #calculate basic variables for distribution
    books_per_user_base = books_data_len // len(user_data)
    books_per_user_extra = books_data_len % len(user_data)


    users_to_json = [
        {}
    ]

    with open("books.csv", "r") as csv_file:
        reader = DictReader(csv_file)


        user_count = 0
        for user in user_data:
            if user_count < books_per_user_extra:
                books_data = {"books": []}
                for row in range(books_per_user_base + 1):
                    books_data["books"].append(next(reader))
            else:
                books_data = {"books": []}
                for row in range(books_per_user_base):
                    books_data["books"].append(next(reader))

            filtered_user_data = {
                "name": user['name'],
                "gender": user['gender'],
                "address": user['address'],
                "age": user['age'],
            }

            filtered_user_data.update(books_data)
            users_to_json.append(filtered_user_data)

            user_count += 1


with open("result.json", "w") as json_file:

    # Remove first null json object
    users_to_json.pop(0)

    s = json.dumps(users_to_json, indent=4)
    json_file.write(s)



