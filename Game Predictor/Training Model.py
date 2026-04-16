import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import joblib


game_file=pd.read_csv('videogames.csv')
game_file = game_file[['Name','Platform','Year_of_Release','Genre','Publisher']].dropna()
game_file['Platform'] = game_file['Platform'].str.lower()
game_file['Genre'] = game_file['Genre'].str.lower()
game_file['Publisher'] = game_file['Publisher'].str.lower()

platform_code = LabelEncoder()
genre_code = LabelEncoder()
publisher_code = LabelEncoder()
game_file['Platform'] = platform_code.fit_transform(game_file['Platform'])
game_file['Genre'] = genre_code.fit_transform(game_file['Genre'])
game_file['Publisher'] = publisher_code.fit_transform(game_file['Publisher'])

X=game_file.drop(columns=['Name'])
y=game_file['Name']
model = DecisionTreeClassifier(max_depth=7)
model.fit(X,y)

joblib.dump(model, 'game_model.joblib')
joblib.dump(platform_code, 'platform_encoder.joblib')
joblib.dump(genre_code, 'genre_encoder.joblib')
joblib.dump(publisher_code, 'publisher_encoder.joblib')

user_platform = input("Please enter your Platform: ").lower()
user_publisher = input("Please enter your Publisher: ").lower()
user_genre = input("Please enter your Genre: ").lower()
user_year = int(input("Please enter your Year: "))
platform = platform_code.transform([user_platform])[0]
genre= genre_code.transform([user_genre])[0]
publisher = publisher_code.transform([user_publisher])[0]

prediction = model.predict([[platform,user_year,genre,publisher]])

correct_details = game_file[
    (game_file['Platform'] == platform) &
    (game_file['Year_of_Release'] == user_year) &
    (game_file['Genre'] == genre) &
    (game_file['Publisher'] == publisher)]
if not correct_details.empty:
    print(f'The exact match found which is "{prediction[0]}"')
else:
    print(f'No exact match could be found the closet match is "{prediction[0]}"')