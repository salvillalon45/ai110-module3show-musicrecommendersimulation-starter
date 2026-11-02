"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


# Standard profiles: clear, consistent tastes the scorer should handle well.
HIGH_ENERGY_POP = {
    "genre": "pop",
    "mood": "happy",
    "energy": 0.9,
    "tempo": 128,
    "acousticness": 0.1,
}

CHILL_LOFI = {
    "genre": "lofi",
    "mood": "chill",
    "energy": 0.35,
    "tempo": 75,
    "acousticness": 0.8,
}

DEEP_INTENSE_ROCK = {
    "genre": "rock",
    "mood": "intense",
    "energy": 0.92,
    "tempo": 150,
    "acousticness": 0.1,
}

# Adversarial / edge-case profiles: built to try to trick the scoring logic.

# Conflict: sad mood (low valence songs) paired with very high energy.
# No song is both, so energy closeness and mood match will pull in opposite
# directions. "sad" is also not a mood in the catalog, so it can never match.
CONFLICTING_ENERGY_SAD = {
    "genre": "classical",
    "mood": "sad",
    "energy": 0.9,
    "valence": 0.1,
}

# Impossible combination: genre and mood each exist in the catalog, but never
# on the same song, and the numeric targets point at a third kind of song.
IMPOSSIBLE_COMBO = {
    "genre": "metal",
    "mood": "peaceful",
    "energy": 0.1,
    "tempo": 60,
    "acousticness": 0.95,
}

# Out-of-range values: energy above 1.0 and a huge tempo, to check that
# clamping keeps scores sane and nothing goes negative or above 1.0.
OUT_OF_RANGE = {
    "genre": "edm",
    "mood": "euphoric",
    "energy": 1.5,
    "tempo": 400,
}

PROFILES = {
    "High-Energy Pop": HIGH_ENERGY_POP,
    "Chill Lofi": CHILL_LOFI,
    "Deep Intense Rock": DEEP_INTENSE_ROCK,
    "Adversarial: Conflicting (energy 0.9 + sad)": CONFLICTING_ENERGY_SAD,
    "Adversarial: Impossible genre/mood combo": IMPOSSIBLE_COMBO,
    "Adversarial: Out-of-range values": OUT_OF_RANGE,
}


def main() -> None:
    songs = load_songs("data/songs.csv")

    for profile_name, user_prefs in PROFILES.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\n" + "=" * 50)
        print(f"  {profile_name.upper()}")
        print(f"  Prefs: {user_prefs}")
        print("=" * 50)

        for rank, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            reasons = explanation.split(", ")

            print(f"\n#{rank}  {song['title']} by {song['artist']}")
            print(f"    Score: {score:.2f} / 1.00")
            print("    Reasons:")
            for reason in reasons:
                print(f"      - {reason}")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
