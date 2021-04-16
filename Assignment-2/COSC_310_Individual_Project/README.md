# Indiviual Project

## To use ChatBot.py you need to pip install vaderSentiment, NLTK, tkinter, and PyDictionary

This is a  indiviual project to create a functional chatbot for COSC 310. The user should be able to hold basic conversation with the bot about sports. The role the agent will take is that of a friend, and the user can ask the agent questions about sports. This bot was built off of the previous bot created in assignment 2.

This program uses modified code from https://github.com/nltk/nltk/blob/develop/nltk/chat/util.py which is open source.

## New Features that were completed for the indiviual project
For the indiviual part I used two api's which are were google translate and wikipedia.

# Wikipedia api: to use first pip install wikipedia
This first API is being used in the chatbot is a wiki api where the chatbot can be asked about a certian topic and the chatbot will return 1 sentence from the wikipedia page that the user asked about. To trigger this the user will ask the chatbot explain to me <topic> and the chatbot will scrape the wiki page and return the 1st sentence on the wiki topic page. Some of the limitations of this api is when the user is not specific on what they ask. An example would be if the user asks explain to me Lebron James and the ChatBot crashes due to it not being specific enough.
  
Example convo:
User: Explain to me Zach Lavine
                                 
                                 ChatBot: Zachary LaVine (born March 10, 1995) is an American professional 
                                          basketball player for the Chicago Bulls of the National Basketball 
                                          Association (NBA).
                                          
User: Explain to me FIFA World Cup
                                 
                                 ChatBot: The FIFA World Cup, often simply called the World Cup, is an international 
                                          association football competition contested by the senior men's national teams 
                                          of the members of the Fédération Internationale de Football Association (FIFA), 
                                          the sport's global governing body.
                                          
User: Explain to me Hong Kong sevens
                                  
                                 ChatBot: The Hong Kong Sevens (Chinese: 香港國際七人欖球賽) is considered the premier tournament 
                                          on the World Rugby Sevens Series competition. 
                                          
## Google Translate api: to use first pip install googletrans==3.1.0a0
This second API is a translator and can be used when the user input is in a differnet language. The ChatBot will sense that the user input is in a different language and will take that input and translate it to english so the chatbot can understand what the user asked. When the ChatBot translates the user input to english it will return the output in english for the user. The translate api supports multiple languages but can be finicky with langauges that have special characters. User who speak spanish, french, german will have the best exprience.

Example convo when the user speak russian:
User: Привет (eng: Hello)
                                 
                                 ChatBot: Hi, what is your name?

When the user speaks finnish:                                
User: nimeni on jeff (eng: My name is jeff)

                                 ChatBot: Hello jeff, my name is sports bot. Do you play any sports?
                                 
When the user speaks dutch:
User: wanneer is het volgende WK? (eng:when is the next world cup?)

                                  ChatBot: Next year in Qatar
                                  
                                  
</br>                                  
</br>  
</br>                                  
</br>  


                    
- - -
*Old Features from A3 update*                                                       
## Old Features that were completed in the group project

Group project features have been implemented in this bot, including POS tagging, sentiment analysis, entity recognition, and synonym recognition.

Sentiment analysis adds to the bot by analyzing the user input, judging the overall sentiment, and providing an appropriate response if necessary. This was done by using the 'SentimentIntensityAnalyzer' function from the 'vaderSentiment' tool. When the user inputs a question/phrase, it is assigned a numerical value based on the overall sentiment (positive is a generally nice input, negative is a generally mean input). If the phrase is negative, the bot will get angry and tell the user it wasn't nice.

Example convo:

when is the next world cup?

                                                      Next year in Qatar
                                                      
who will win the next world cup?

                                                      Canada, no doubt. They are a soccer powerhouse
                                                      
what are you talking about?? Canada sucks at soccer!

                                                      Well that does not seem very nice!
                

POS tagging adds to the bot by splitting up every individual word in the user input, and then assigning each word a grammatical category. This was implemented by using the 'words_tokenize' and 'pos_tag' functions from the nltk tool. The bot is programmed to identify currencies and numerical values (to detect years), and will then give a specific response. The bot will also print out a list of each word and its associated part of speech tag.

Example convo:

what is the premier league?

                                                       The Premier League is the top division of soccer in England.
                                                       
do you think i could go to a premier league game for $100?

                                                       Sorry. I don't understand currency well. Can you try again?
                                             
i was born in 1999, who won the premier league that year?

                                                       Sorry, I am unfamiliar with that year. Can you try again?

Named Entity Recognition(NER) was implemented into the chatbot using NLTK's tagging and word tokenizer features along with the averaged perception tagger library in NLTK. The bot seeks and extracts each word the user types and breaks it apart with the word tokenizer. It then prints to console each individual words and it's association with the english language.  Associations such as pronouns, verbs, and adjectives are printed along with its tokened key as part of an array that includes all words of the user's input.  This feature helps programmers recognize the sentence structure the user inputs and can articulate additional conversation pair according to the logged inputs.

Example:

my name is James

                                                       [('my', 'PRP$'), ('name', 'NN'), ('is', 'VBZ'), ('james', 'NNS')]
                                                       
I play soccer

                                                       [('I', 'PRP'), ('play', 'VBP'), ('soccer', 'NN')]
                                                       
                                                       
Synonym Recognition was implemented into the chatbot in two different versions, one using the PyDictionary library, the other using NLTK's WordNet. They both function the same, passing words to the libraries which return synonyms for the words. To reduce memory usage only verbs and adjectives are passed to the libraries and then the sentence the user inputed is mutated to see if changing a synonym in will make the chatbot recognize the statement as a pair. We are somewhat restricted by libraries, as some words aren't properly recognized as synonyms, such as 'Best' being a synonym of 'greatest' but 'greatest' not being a synonym of 'best' according to the library. As you can see by the example below, the chatbot will reply with the same response to both statements.

Example:

I witness hockey

                                                          Who is your favourite hockey player?
                                            
I watch hockey                            

                                                          Who is your favourite hockey player?

