# import requests
# import random
# from selenium import webdriver
# # response = requests.get("https://api.github.com/users/avielb/repos")
# # repositories = response.json()
# # assert len(repositories) >= 5
#
# # general_first_names = ['John', 'Alice', 'Bob', 'Eva', 'Michael', 'Sophia', 'David', 'Emma', 'Christopher', 'Olivia',
# # #                        'Daniel', 'Ava', 'Matthew', 'Emily', 'Andrew', 'Isabella', 'Joshua', 'Mia', 'Anthony', 'Abigail',
# # #                        'James', 'Madison', 'Alexander', 'Chloe','Noam', 'Tamar', 'Yosef', 'Shira', 'Itai', 'Maya', 'Eitan', 'Yael', 'Omer', 'Lior', 'Noya',
# # #                        'Amit', 'Yonatan', 'Roni', 'Hadar', 'Eliana', 'Ido', 'Liat', 'Avi', 'Nina', 'Oren', 'Adi',
# # #                        'Yehuda', 'Ayelet']
# # # for i in range(3):
# # #     random_first_name = random.choice(general_first_names)
# # #     response1 = requests.get("https://api.agify.io/?name="+random_first_name)
# # #     age = response.json()
# # #     print (age)
# # #     age = age["age"]
# # #
# # #     assert age >0 and age < 120
#
# # response2 = requests.get("http://universities.hipolabs.com/search?country=Israel")
# # universities = response2.json()
# # count = 0
# # print("list of universities in Israel: ")
# # for university in universities:
# #     print(str(university['name']))
# #     count += 1
# # print("total is:"+ str(count))
#
# title1 = webdriver.Chrome()
# title1.get("https://www.ycombinator.com/")
# assert title1.title =="Y Combinator"
#
# title2 = webdriver.Chrome()
# title2.get("https://hub.docker.com")
#
# assert title2.title == "Docker Hub Container Image Library | App Containerization"a