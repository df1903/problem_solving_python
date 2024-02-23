"""
Maria plays college basketball and wants to go pro.
Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game.
Points scored in the first game establish her record for the season, and she begins counting from there.

scores = [12,24,10,24]


Scores are in the same order as the games played. She tabulates her results as follows:

                                     Count
    Game  Score  Minimum  Maximum   Min Max
     0      12     12       12       0   0
     1      24     12       24       0   1
     2      10     10       24       1   1
     3      24     10       24       1   1

Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.
"""

def breakingRecords(scores: int) -> [int]:
    records: [int] = [0, 0]
    max_score: int = scores[0]
    min_score: int = scores[0]

    for i in scores:
        if i > max_score:
            max_score = i
            records[0] += 1
            continue
        if i < min_score:
            min_score = i
            records[1] += 1

    return records


if __name__ == '__main__':
    scores: [int] = [12, 24, 10, 24]
    result: [int]= breakingRecords(scores)
    print(result)