import re
import statistics

# Реплики Аннет
replicas = [
    "You came here to ask your way and now you know it",
    "Drink up your wine and go",
    "And so what?",
    "He's right, You're drunk. Now go. Go",
    "Father",
    "Father",
    "What d'you want?",
    "It's you. Cochon",
    "Take them away and take yourself off with them",
    "I'm not afraid of you",
    "Get out of here",
    "If you don't go my father will go to Soissons and complain to the general",
    "That's not your business",
    "Working in the fields",
    "We haven't seen cheese for three months. We haven't enough bread to stay our hunger. The French took our horses a year ago and now the Boches have taken our cows, our pigs, our chickens, everything",
    "Can we eat the worthless paper they gave us?",
    "Oh, no",
    "We can eat like kings on potatoes and bread and turnips and lettuce. Tomorrow my father's going to Soissons to see if he can buy some horse meat",
    "I don't want your presents. I'll starve before I touch the food you swine have stolen from us",
    "What are you doing here?",
    "Take them away. Take them",
    "I won't take his presents",
    "The shame of it",
    "Why do you want to come here? Why can't you leave us alone?",
    "Talk. I am a woman and defenceless",
    "You ask me why I can't be reasonable like my father and mother",
    "The shame of it. The shame",
    "Don't touch me. Go away. Go away. Haven't you done me enough harm already?",
    "I don't want it",
    "Never. Why don't you leave me alone? Isn't it enough that you've ruined my life?",
    "Proud?",
    "How dare you say that?",
    "You? Why?",
    "He says he loves me",
    "Nothing of importance",
    "Hold your tongue",
    "I'm engaged to a teacher who worked in the boys' school in the town where I taught, we were to be married after the war. He's not strong and big like you, or handsome; he's small and frail. His only beauty is the intelligence that shines in his face, his only strength is the greatness of his soul. He's not a barbarian, he's civilized; he has a thousand years of civilization behind him. I love him. I love him with all my heart and soul",
    "Where do you suppose he is? In Germany. A prisoner and starving. While you eat the fat of our land. How many times have I got to tell you that I hate you? You ask me to forgive you. Never. You want to make reparation. You fool",
    "Ruined. Oh, he'll forgive me. He's tender. But I'm tortured by the thought that one day the suspicion may come to him that perhaps I hadn't been forced–that perhaps I'd given myself to you for butter and cheese and silk stockings. I shouldn't be the only one. And what would our life be with that child between us, your child, a German child? Big like you, and blond like you, and blue–eyed like you. Oh, my God, why do I have to suffer this?",
    "Thank you for the warning. I shall stay in my room",
    "You're wasting your breath, Mother. I earned my living before, I can earn my living again. I hate him. I hate his vanity and his arrogance. I could kill him: his death wouldn't satisfy me. I should like to torture him as he's tortured me. I think I should die happy if I could find a way to wound him as he's wounded me",
    "Do you think I believe a word in that paper? Why do you think he brings it to you except that it's sold to the Germans? The men who write in it–traitors, traitors. Oh God, may I live to see them torn to pieces by the mob. Bought, bought every one of them–bought with German money. The swine",
    "You should have been a priest. You forgive injuries with a spirit truly Christian",
    "If you'd had any pride, if you'd had any sense of decency, you'd have thrown his presents in his face",
    "Never. Never",
    "I know. I tried not to, I couldn't help myself, I was so hungry. Yes, I knew his meat went into the soup and I ate it. I knew the salad was made with his oil. I wanted to refuse it; I had such a longing for it, it wasn't I that ate it, it was a ravenous beast within me",
    "With shame. With despair. They broke our strength first with their tanks and their planes, and now when we're defenceless they're breaking our spirit by starving us",
    "I ought to. I taught it. For two years I was governess to two little girls in Stuttgart",
    "Don't speak of him",
    "That would be the last straw",
    "Shot in cold blood by his German jailers",
    "Even if there were nothing else do you think I could ever forget that you are a German and I'm a Frenchwoman? If you weren't as stupid as only a German can be you'd see that that child must be a reproach to me as long as I live. Do you think I have no friends? How could I ever look them in the face with the child I had with a German soldier? There's only one thing I ask you; leave me alone with my disgrace. Go, go–for God's sake go and never come again",
    "You?",
    "What can a by–blow that you got in a moment of savage drunkenness mean to you?",
    "I don't know whether I more loathe the brutality of you Germans or despise your sentimentality",
    "You've made up your mind it'll be a boy?",
    "Others may despise me. I will never do anything that can make me despise myself. You are my enemy and you will always be my enemy. I only live to see the deliverance of France. It'll come, perhaps not next year or the year after, perhaps not for thirty years, but it'll come. The rest of them can do what they like, I will never come to terms with the invaders of my country. I hate you and I hate this child that you've given me. Yes, we've been defeated. Before the end comes you'll see that we haven't been conquered. Now go. My mind's made up and nothing on God's earth can change it",
    "Do you suppose we want to spread our shame through the whole countryside? My mother will do all that's necessary",
    "And supposing you mind your own business!",
    "O God, give me strength",
    "The beast",
    "Lies, lies, lies. And I was weak enough to be almost sorry for him",
    "I had to do it at once. I was afraid if I waited I shouldn't have the courage",
    "I've done what I had to do. I took it down to the brook and held it under water till it was dead"
]

# Считаем слова в каждой реплике
word_counts = [len(rep.split()) for rep in replicas]

# Короткие реплики (<5 слов)
short_replicas = [rep for rep in replicas if len(rep.split()) < 5]

# Реплики с отрицанием
negation_words = ['not', "don't", 'never', "can't", "won't", 'no']
negations = [rep for rep in replicas if any(word in rep.lower() for word in negation_words)]

# Реплики с повелительным наклонением (простые ключевые слова)
imperative_words = ['go', 'get out', 'take', 'leave', 'stop', 'stay', 'hold your tongue', 'mind your own business']
imperatives = [rep for rep in replicas if any(word in rep.lower() for word in imperative_words)]

# Реплики с протестом или отказом
protest_phrases = ['i don\'t want', 'i won\'t', 'i hate', 'leave me alone', 'go away', 'i refuse', 'never', 'i despise', 'how dare you', 'you are my enemy', 'i will never']
protests = [rep for rep in replicas if any(phrase in rep.lower() for phrase in protest_phrases)]

# Выводим статистику
print("Общее число реплик:", len(replicas))
print("Общее число слов:", sum(word_counts))
print("Средняя длина реплики (слов):", round(sum(word_counts) / len(word_counts), 2))
print("Медианная длина реплики (слов):", statistics.median(word_counts))
print("Короткие реплики (<5 слов):", len(short_replicas), f"(≈{round(len(short_replicas)/len(replicas)*100)}%)")
print("Минимальная / максимальная длина реплики:", min(word_counts), "/", max(word_counts))
print("Реплики с отрицаниями:", len(negations), f"(≈{round(len(negations)/len(replicas)*100)}%)")
print("Реплики с повелительными конструкциями:", len(imperatives), f"(≈{round(len(imperatives)/len(replicas)*100)}%)")
print("Реплики с протестом / отказом:", len(protests), f"(≈{round(len(protests)/len(replicas)*100)}%)")