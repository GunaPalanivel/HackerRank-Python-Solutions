if __name__ == '__main__':
    # initialize the nested list of students and their scores
    student_scores = []
    
    # get the number of students from user input
    n = int(input())
    
    # get the names and scores of each student from user input
    for i in range(n):
        name = input()
        score = float(input())
        student_scores.append([name, score])
    
    # sort the nested list by score in ascending order
    student_scores.sort(key=lambda x: x[1])
    
    # find the second lowest score
    second_lowest_score = sorted(set([x[1] for x in student_scores]))[1]
    
    # get the names of students who have the second lowest score
    result = [x[0] for x in student_scores if x[1] == second_lowest_score]
    
    # sort the names in ascending order and print them
    result.sort()
    for name in result:
        print(name)
