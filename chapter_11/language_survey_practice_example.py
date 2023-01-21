from language_survey import AnonymousSurvey

question ='What language did you first learn to speak?'

my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time to exit the program.\n")
while True:
    response = input("Languages: ")
    if response == 'q':
        break
    my_survey.store_response(response)
    
print("Thank you for taking this survey!")

my_survey.show_results()

