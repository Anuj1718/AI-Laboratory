def evaluate_performance():
    print("Welcome to the Employee Performance Evaluation Chatbot!")
    print("Please rate yourself on a scale of 1 to 5, where 1 is 'Poor' and 5 is 'Excellent'.\n")
    
    # Chatbot conversation for rating
    work_quality = int(input("How would you rate your Work Quality? (1-5): "))
    punctuality = int(input("How would you rate your Punctuality? (1-5): "))
    teamwork = int(input("How would you rate your Teamwork? (1-5): "))
    innovation = int(input("How would you rate your Innovation? (1-5): "))
    communication = int(input("How would you rate your Communication Skills? (1-5): "))
    
    # Check if input is within the valid range
    ratings = [work_quality, punctuality, teamwork, innovation, communication]
    if any(rating < 1 or rating > 5 for rating in ratings):
        print("Please enter a rating between 1 and 5.")
        return

    # Calculate the average score
    avg_score = sum(ratings) / len(ratings)

    # Evaluate the performance
    if avg_score >= 4.5:
        performance = "Excellent"
        feedback = "Outstanding performance! Keep up the great work."
    elif avg_score >= 3.5:
        performance = "Good"
        feedback = "Good performance, but there's always room for improvement."
    elif avg_score >= 2.5:
        performance = "Average"
        feedback = "Your performance is average. Focus on improving specific areas."
    else:
        performance = "Needs Improvement"
        feedback = "You need to improve in multiple areas. Please focus on your weaknesses."

    # Display the result
    print("\nEmployee Performance Evaluation Results:")
    print(f"Your average score is: {avg_score:.2f}")
    print(f"Performance Level: {performance}")
    print(feedback)

# Start the evaluation
evaluate_performance()
