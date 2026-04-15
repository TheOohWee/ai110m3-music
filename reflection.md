# Reflection Notes

## Profile Pair Comparisons

- High-Energy Pop vs Chill Lofi: The pop profile prefers upbeat, brighter songs like Sunrise City, while the lofi profile shifts toward calmer, lower-energy tracks like Library Rain and Midnight Coding. That makes sense because the two profiles are almost opposites on genre, mood, and energy.
- High-Energy Pop vs Deep Intense Rock: Both profiles like high energy, but the rock profile pulls Storm Runner to the top because genre and mood also match. The pop profile stays closer to happier, more polished songs, which shows the genre and mood signals are still shaping the output.
- High-Energy Pop vs Conflicting Edge Case: The conflicting profile asks for sad, jazz, and very high energy at the same time. The recommender can only partially satisfy that, so it ends up leaning on energy and returns songs that are intense even when they do not match the mood perfectly.
- Chill Lofi vs Deep Intense Rock: These profiles produce very different top songs because one wants relaxed and acoustic-feeling tracks while the other wants loud, fast, aggressive tracks. The overlap is small, which is a good sign that the scorer can separate clear extremes.
- Chill Lofi vs Conflicting Edge Case: Chill Lofi prefers low energy and cozy sounds, but the conflicting profile pushes toward high energy. That creates very different rankings, which shows the energy target is a strong signal in the system.
- Deep Intense Rock vs Conflicting Edge Case: Both profiles like energy, but the rock profile also rewards the correct genre and mood. The conflicting profile does not have that same alignment, so its ranking is less clean and more mixed.

## Short Summary

The outputs changed in ways that mostly made sense. When the profile was clear, the recommender felt accurate. When the profile had conflicting preferences, the system had to choose which rule mattered most, and that exposed how strongly the energy score can influence the ranking.