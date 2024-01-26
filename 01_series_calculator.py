from math import floor
series_name = input()
seasons_count = int(input())
episodes_count = int(input())
episode_duration = float(input())

commercials = episode_duration * 0.2
extra_minutes = seasons_count * 10

whole_episodes = seasons_count * episodes_count
total_episode_duration = episode_duration + commercials
total_time_needed = whole_episodes * total_episode_duration + extra_minutes

print(f'Total time needed to watch the {series_name} series is {floor(total_time_needed)} minutes.')