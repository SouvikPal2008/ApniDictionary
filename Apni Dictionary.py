print("Welcome To Apni Dictionary !!!")
DictionaryItems = {"Thought" : "the act of thinking about or considering something, an idea or opinion, or a set of ideas about a particular subject" ,
                "Appreciate" : "to recognize how good someone or something is and to value him, her, or it" ,
                "Opportunity" : "an occasion or situation that makes it possible to do something that you want to do or have to do, or the possibility of doing something" ,
                "Appeal" : "A Request To Public For Money, Information or Help"}
print("Our Stock of Words -" , "Thought," , "Appreciate," , "Opportunity," , "Appeal,")
print("Please Enter Which Word's Meaning Would You Like To Know")
in1 = input()
print("The Meaning Is")
print(DictionaryItems[in1])
print("Source - https://dictionary.cambridge.org")