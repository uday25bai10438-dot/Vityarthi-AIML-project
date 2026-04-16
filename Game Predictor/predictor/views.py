from django.shortcuts import render
import pandas as pd
import joblib
import difflib

model = joblib.load('game_model.joblib')
platform_code = joblib.load('platform_encoder.joblib')
genre_code = joblib.load('genre_encoder.joblib')
publisher_code = joblib.load('publisher_encoder.joblib')

game_file = pd.read_csv('videogames.csv')
game_file = game_file[['Name', 'Platform', 'Year_of_Release', 'Genre', 'Publisher']].dropna()
game_file['Platform'] = game_file['Platform'].str.lower()
game_file['Genre'] = game_file['Genre'].str.lower()
game_file['Publisher'] = game_file['Publisher'].str.lower()

game_file['Platform'] = platform_code.transform(game_file['Platform'])
game_file['Genre'] = genre_code.transform(game_file['Genre'])
game_file['Publisher'] = publisher_code.transform(game_file['Publisher'])

def index(request):
    result = ""
    if request.method == 'POST':
        user_platform = request.POST.get('platform').strip().lower()
        user_publisher = request.POST.get('publisher').strip().lower()
        user_genre = request.POST.get('genre').strip().lower()
        user_year = int(request.POST.get('year').strip())

        wrong_spelling = ""

        if user_publisher not in publisher_code.classes_:
            closest_match = difflib.get_close_matches(user_publisher, publisher_code.classes_, n=1, cutoff=0.6)
            if closest_match:
                corrected_pub = closest_match[0]
                wrong_spelling  = f" ['{user_publisher}' was auto corrected to '{corrected_pub}']"
                user_publisher = corrected_pub
            else:
                return render(request, 'index.html',
                              {'prediction': f'Error: Could not find any publisher close to "{user_publisher}".'})

        platform = platform_code.transform([user_platform])[0]
        genre = genre_code.transform([user_genre])[0]
        publisher = publisher_code.transform([user_publisher])[0]

        prediction = model.predict([[platform, user_year, genre, publisher]])
        guess = prediction[0]

        correct_details = game_file[
            (game_file['Platform'] == platform) &
            (game_file['Year_of_Release'] == user_year) &
            (game_file['Genre'] == genre) &
            (game_file['Publisher'] == publisher)
            ]

        if not correct_details.empty:
            matching_names = correct_details['Name'].tolist()
            if len(matching_names) > 1:
                games_list = ", ".join(matching_names)
                result = f'Multiple exact matches found : {games_list}{wrong_spelling}'
            else:
                result = f'The exact match found which is "{matching_names[0]}"{wrong_spelling}'
        else:
            result = f'No exact match could be found. The closest match is "{guess}"{wrong_spelling}'

    return render(request, 'index.html', {'prediction': result})