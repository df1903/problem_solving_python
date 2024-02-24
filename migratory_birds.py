"""Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type.
If more than 1 type has been spotted that maximum amount, return the smallest of their ids."""

def migratoryBirds(arr: [int]) -> int:
    ids: [int] = [0,0,0,0,0]
    id: int = 0
    max: int = 0

    for i in arr:
        ids[i-1] += 1

    for j in range(len(ids)):
        if ids[j] > max:
            id = j+1
            max = ids[j]

    return id

if __name__ == '__main__':
    arr: [int] = [1,4,4,4,5,3]
    reslt: int = migratoryBirds(arr)
    print(reslt)