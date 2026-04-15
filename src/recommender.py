from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

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
        """Store the song catalog used for OOP-style recommendations."""
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top-k songs ranked by genre, mood, and energy match."""
        def score(song: Song) -> float:
            genre_points = 1.0 if song.genre.lower() == user.favorite_genre.lower() else 0.0
            mood_points = 1.0 if song.mood.lower() == user.favorite_mood.lower() else 0.0
            energy_points = 2.0 * max(0.0, min(1.0, 1.0 - abs(song.energy - user.target_energy)))
            return genre_points + mood_points + energy_points

        ranked = sorted(self.songs, key=score, reverse=True)
        return ranked[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain why a song was recommended using the same scoring factors."""
        reasons = []
        if song.genre.lower() == user.favorite_genre.lower():
            reasons.append("genre match (+1.0)")
        if song.mood.lower() == user.favorite_mood.lower():
            reasons.append("mood match (+1.0)")

        energy_points = 2.0 * max(0.0, min(1.0, 1.0 - abs(song.energy - user.target_energy)))
        reasons.append(f"energy similarity (+{energy_points:.2f})")

        if not reasons:
            reasons.append("overall similarity across your preferences")

        return f"Recommended for {', '.join(reasons)}."

def load_songs(csv_path: str) -> List[Dict]:
    """
    Load songs from a CSV file and convert numeric fields to floats.

    Returns a list of dictionaries so the functional recommender can
    perform scoring and ranking math on the song data.
    """
    songs: List[Dict] = []
    numeric_fields = ["id", "energy", "tempo_bpm", "valence", "danceability", "acousticness"]
    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for field in numeric_fields:
                row[field] = float(row[field])
            songs.append(
                {
                    "id": row["id"],
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": row["energy"],
                    "tempo_bpm": row["tempo_bpm"],
                    "valence": row["valence"],
                    "danceability": row["danceability"],
                    "acousticness": row["acousticness"],
                }
            )
    return songs


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Score each song, sort by total score, and return the top-k recommendations.

    Each result is a tuple of (song_dict, score, explanation).
    """
    if not songs or k <= 0:
        return []

    energy_values = [float(song["energy"]) for song in songs]
    energy_range = max(energy_values) - min(energy_values)
    if energy_range <= 0:
        energy_range = 1.0

    scored: List[Tuple[Dict, float, str]] = []
    for song in songs:
        genre_points = (
            1.0
            if user_prefs.get("genre", "").lower() == str(song.get("genre", "")).lower()
            else 0.0
        )
        mood_points = (
            1.0
            if user_prefs.get("mood", "").lower() == str(song.get("mood", "")).lower()
            else 0.0
        )
        energy_points = 2.0 * max(
            0.0,
            min(
                1.0,
                1.0
                - abs(float(song.get("energy", 0.0)) - float(user_prefs.get("energy", 0.0)))
                / energy_range,
            ),
        )

        total_score = genre_points + mood_points + energy_points
        reason_parts = []
        if genre_points > 0:
            reason_parts.append(f"genre match (+{genre_points:.1f})")
        if mood_points > 0:
            reason_parts.append(f"mood match (+{mood_points:.1f})")
        reason_parts.append(f"energy similarity (+{energy_points:.2f})")
        explanation = f"Recommended for {', '.join(reason_parts)}."
        scored.append((song, total_score, explanation))

    scored.sort(key=lambda item: item[1], reverse=True)
    return scored[:k]
