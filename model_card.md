# 🎧 Model Card: Music Recommender Simulation

## Model Name

VibeFinder 1.0

## Goal / Task

This system suggests songs a user might like from a small catalog. It uses user preferences to rank songs and return the top results.

## Data Used

The dataset has 18 songs from `data/songs.csv`. Each song has genre, mood, energy, tempo, valence, danceability, and acousticness. The dataset is small, so some tastes are missing or only appear once.

## Algorithm Summary

The recommender gives points for matching genre and matching mood. It also gives energy similarity points based on how close song energy is to the user's target energy. The total score is the sum of those parts, and songs are sorted from highest to lowest score.

## Observed Behavior / Biases

The system is sensitive to feature weights. In the experiment where energy was emphasized, high-energy songs often rose even with weaker genre match. With a small catalog, some songs repeat across profiles, which can create a filter-bubble effect. Conflicting profiles can produce only partial matches because the model has to prioritize one signal over others.

## Evaluation Process

I tested four profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and a Conflicting Edge Case. I compared the top 5 recommendations and checked whether they matched intuition. I also ran a sensitivity experiment by increasing energy importance and reducing genre importance to see how rankings changed. Terminal screenshots were saved as `image1.png` to `image4.png`.

## Intended Use and Non-Intended Use

Intended use: classroom exploration of recommendation logic and model documentation.

Non-intended use: real production music recommendations, high-stakes decisions, or personalization for real users.

## Ideas for Improvement

1. Add more songs and better balance across genres and moods.
2. Add diversity rules so the same artist does not appear too often.
3. Use more features in scoring (tempo, valence, danceability, acousticness) with tuned weights.

## Personal Reflection

My biggest learning moment was seeing how a small weight change can completely reshape the ranked list. AI tools helped me move faster when writing and revising code, but I still had to double-check scoring math and outputs in the terminal. I was surprised that a simple rule-based system can still feel "smart" when the profile and dataset line up well. If I extend this project, I would add automatic weight tuning, more diverse data, and clearer explanation outputs for each recommendation.
