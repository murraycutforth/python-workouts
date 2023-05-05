from pathlib import Path
from statistics import mean
from collections import defaultdict
import json


def print_scores():
    score_dir = Path("scores")
    for class_score in score_dir.iterdir():
        with open(class_score, "r") as infile:
            scorelist = json.load(infile) # List of dicts

        # Invert representation to dict of lists
        subject_to_scores = defaultdict(list)
        for score_element in scorelist:
            for subject, score in score_element.items():
                subject_to_scores[subject].append(score)

        # Print out summary
        print(class_score.name)
        for subject, scores in subject_to_scores.items():
            print(f"{subject:20}Max:{max(scores):3} Min:{min(scores):3} Mean:{mean(scores):3}")

        

print_scores()

