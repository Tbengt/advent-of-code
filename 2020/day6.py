import sys


if __name__ == "__main__":
    answers_raw = []
    for line in sys.stdin:
        answers_raw.append(line.strip())

    answer_freq = {}
    total_sum = 0
    people_in_group = 0
    for answer in answers_raw:
        if answer == "":
            for key in answer_freq:
                if answer_freq[key] == people_in_group:
                    total_sum += 1
            answer_freq = {}
            people_in_group = 0
        else:
            people_in_group += 1
            for c in answer:
                if c in answer_freq:
                    answer_freq[c] += 1
                else:
                    answer_freq[c] = 1

    print(total_sum)

