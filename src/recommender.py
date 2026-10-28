import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    int_fields = ["id"]
    float_fields = ["energy", "tempo_bpm", "valence", "danceability", "acousticness"]

    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            song = dict(row)
            for field in int_fields:
                song[field] = int(row[field])
            for field in float_fields:
                song[field] = float(row[field])
            songs.append(song)

    print(f"Loaded {len(songs)} songs from {csv_path}")
    return songs

DEFAULT_WEIGHTS = {
    "genre": 2.0,
    "mood": 1.0,
    "energy": 2.0,
    "tempo": 1.0,
    "acousticness": 1.0,
    "valence": 0.5,
    "danceability": 0.5,
}

CATEGORICAL_FEATURES = ["genre", "mood"]

# user preference key -> song dict field
NUMERIC_FEATURES = {
    "energy": "energy",
    "tempo": "tempo_bpm",
    "acousticness": "acousticness",
    "valence": "valence",
    "danceability": "danceability",
}

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.

    Categorical features (genre, mood) score 1 on a match and 0 otherwise.
    Numeric features (energy, tempo, acousticness, valence, danceability)
    score 1 - abs(song - target), with the tempo difference divided by 100
    and every feature score clamped to a minimum of 0.

    Only features present in user_prefs are scored. Each feature score is
    multiplied by its weight (user_prefs["weights"] if given, otherwise
    DEFAULT_WEIGHTS), and the sum is divided by the total weight of the
    scored features so the final score falls between 0 and 1.

    Returns:
        (score, reasons), where reasons is a list of strings such as
        "genre match (+2.0)" or "energy closeness (+1.96 of 2.0)".

    Required by recommend_songs() and src/main.py
    """
    weights = user_prefs.get("weights", DEFAULT_WEIGHTS)

    total_points = 0.0
    total_weight = 0.0
    reasons = []

    # Categorical features: 1 for a match, 0 otherwise
    for feature in CATEGORICAL_FEATURES:
        if feature not in user_prefs:
            continue
        weight = weights.get(feature, 0.0)
        total_weight += weight
        if song[feature] == user_prefs[feature]:
            total_points += weight
            reasons.append(f"{feature} match (+{weight:.1f})")

    # Numeric features: 1 - abs(song - target), tempo difference scaled by 100
    for feature, song_field in NUMERIC_FEATURES.items():
        if feature not in user_prefs:
            continue
        weight = weights.get(feature, 0.0)
        difference = abs(song[song_field] - user_prefs[feature])
        if feature == "tempo":
            difference = difference / 100
        feature_score = max(0.0, 1 - difference)

        points = weight * feature_score
        total_points += points
        total_weight += weight
        reasons.append(f"{feature} closeness (+{points:.2f} of {weight:.1f})")

    if total_weight == 0:
        return 0.0, reasons

    score = total_points / total_weight
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.

    Scores every song with score_song(), sorts them from highest to lowest
    score, and returns the top k.

    Returns:
        A list of (song_dict, score, explanation) tuples, where explanation
        is the song's scoring reasons joined into one comma-separated string.

    Required by src/main.py
    """
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_songs.append((song, score, explanation))

    ranked = sorted(scored_songs, key=lambda item: item[1], reverse=True)
    return ranked[:k]
