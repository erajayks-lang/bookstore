#!/usr/bin/env python3
"""
Script to generate books.json with 200 books
Run this once to create the initial book database
"""

import json

books = []
book_id = 1

# Fiction (40 books)
fiction = [
    ('The Great Gatsby', 'F. Scott Fitzgerald', 12.99, 'Classic American novel set in the Jazz Age, exploring themes of wealth and love.', 50),
    ('To Kill a Mockingbird', 'Harper Lee', 14.99, 'Gripping tale of racial injustice and childhood innocence.', 45),
    ('The Catcher in the Rye', 'J.D. Salinger', 13.49, 'Teenage rebellion and alienation in post-war America.', 38),
    ('Beloved', 'Toni Morrison', 15.99, 'Powerful novel about the lasting effects of slavery.', 42),
    ('The Road', 'Cormac McCarthy', 14.49, 'Post-apocalyptic tale of father and son.', 35),
    ('One Hundred Years of Solitude', 'Gabriel García Márquez', 16.99, 'Magical realism masterpiece.', 40),
    ('The Kite Runner', 'Khaled Hosseini', 14.99, 'Friendship and redemption in Afghanistan.', 48),
    ('Life of Pi', 'Yann Martel', 13.99, 'Boy survives on lifeboat with tiger.', 44),
    ('The Book Thief', 'Markus Zusak', 15.49, 'Girl steals books during WWII.', 52),
    ('Brave New World', 'Aldous Huxley', 13.99, 'Dystopian technological society.', 41),
    ('The Color Purple', 'Alice Walker', 14.49, 'Black woman in American South.', 39),
    ('Atonement', 'Ian McEwan', 15.99, 'Love, war, and consequences.', 37),
    ('The Remains of the Day', 'Kazuo Ishiguro', 13.99, 'Butler reflects on life.', 43),
    ('Middlesex', 'Jeffrey Eugenides', 16.49, 'Family saga exploring identity.', 38),
    ('The Poisonwood Bible', 'Barbara Kingsolver', 15.99, 'Missionary family in Congo.', 42),
    ('The Secret History', 'Donna Tartt', 17.99, 'Dark academia thriller.', 55),
    ('White Teeth', 'Zadie Smith', 14.99, 'Immigrant families in London.', 40),
    ('The Goldfinch', 'Donna Tartt', 18.99, 'Coming-of-age with stolen painting.', 47),
    ('All the Light We Cannot See', 'Anthony Doerr', 16.99, 'WWII French girl and German boy.', 53),
    ('The Shadow of the Wind', 'Carlos Ruiz Zafón', 15.49, 'Gothic mystery in Barcelona.', 44),
    ('The Night Circus', 'Erin Morgenstern', 14.99, 'Magical mysterious circus.', 49),
    ('Cloud Atlas', 'David Mitchell', 17.49, 'Six interconnected stories.', 41),
    ('The Amazing Adventures of Kavalier & Clay', 'Michael Chabon', 16.99, 'Comic book creators.', 38),
    ('Never Let Me Go', 'Kazuo Ishiguro', 14.99, 'Love and identity story.', 45),
    ('Station Eleven', 'Emily St. John Mandel', 14.99, 'Post-apocalyptic theater troupe.', 50),
    ('The Underground Railroad', 'Colson Whitehead', 16.49, 'Reimagined Underground Railroad.', 42),
    ('A Little Life', 'Hanya Yanagihara', 18.99, 'Friendship and trauma.', 39),
    ('The Overstory', 'Richard Powers', 17.99, 'Stories about trees.', 37),
    ('Americanah', 'Chimamanda Ngozi Adichie', 15.99, 'Love, race, and identity.', 46),
    ('The Brief Wondrous Life of Oscar Wao', 'Junot Díaz', 14.99, 'Dominican-American family.', 43),
    ('The Corrections', 'Jonathan Franzen', 16.99, 'Darkly comic family.', 40),
    ('Everything I Never Told You', 'Celeste Ng', 13.99, 'Family mystery.', 48),
    ('The Nickel Boys', 'Colson Whitehead', 15.49, 'Reform school story.', 41),
    ('Lincoln in the Bardo', 'George Saunders', 16.99, 'Experimental Lincoln novel.', 35),
    ('The Sympathizer', 'Viet Thanh Nguyen', 15.99, 'Vietnam War spy thriller.', 44),
    ('There There', 'Tommy Orange', 14.99, 'Urban Native Americans.', 47),
    ('The Vanishing Half', 'Brit Bennett', 16.99, 'Twin sisters, different identities.', 52),
    ('Normal People', 'Sally Rooney', 14.49, 'Modern Irish love story.', 56),
    ('The Handmaid\'s Tale', 'Margaret Atwood', 14.99, 'Dystopian totalitarian society.', 46),
    ('Little Fires Everywhere', 'Celeste Ng', 15.99, 'Suburban family secrets.', 49),
]

emojis = ['📕', '📗', '📘', '📙']
for i, (title, author, price, desc, stock) in enumerate(fiction):
    books.append({
        'id': book_id,
        'title': title,
        'author': author,
        'price': price,
        'category': 'Fiction',
        'description': desc,
        'stock': stock,
        'image': emojis[i % 4]
    })
    book_id += 1

# Science Fiction (30 books)
scifi = [
    ('1984', 'George Orwell', 13.99, 'Dystopian totalitarianism novel.', 60),
    ('Dune', 'Frank Herbert', 18.99, 'Epic saga on desert planet.', 52),
    ('Neuromancer', 'William Gibson', 14.99, 'Groundbreaking cyberpunk.', 44),
    ('The Left Hand of Darkness', 'Ursula K. Le Guin', 13.99, 'Gender exploration alien world.', 40),
    ('Foundation', 'Isaac Asimov', 15.49, 'Galactic empire saga.', 48),
    ('Snow Crash', 'Neal Stephenson', 16.99, 'Cyberpunk metaverse.', 46),
    ('The Martian', 'Andy Weir', 14.99, 'Astronaut stranded on Mars.', 65),
    ('Ender\'s Game', 'Orson Scott Card', 15.99, 'Child genius interstellar war.', 58),
    ('The Three-Body Problem', 'Liu Cixin', 16.49, 'First contact with aliens.', 50),
    ('Hyperion', 'Dan Simmons', 17.99, 'Space opera epic.', 43),
    ('Do Androids Dream of Electric Sheep?', 'Philip K. Dick', 13.99, 'Bounty hunter tracks androids.', 47),
    ('The Dispossessed', 'Ursula K. Le Guin', 14.99, 'Anarchist physicist.', 41),
    ('Childhood\'s End', 'Arthur C. Clarke', 13.49, 'Alien overlords bring peace.', 39),
    ('Fahrenheit 451', 'Ray Bradbury', 12.99, 'Firemen burn books.', 54),
    ('The Forever War', 'Joe Haldeman', 14.99, 'Time dilation in war.', 42),
    ('Ringworld', 'Larry Niven', 15.99, 'Artificial ring world.', 38),
    ('The Moon is a Harsh Mistress', 'Robert A. Heinlein', 14.49, 'Lunar colony revolt.', 40),
    ('Stranger in a Strange Land', 'Robert A. Heinlein', 15.49, 'Human raised on Mars.', 44),
    ('A Canticle for Leibowitz', 'Walter M. Miller Jr.', 13.99, 'Post-apocalyptic monks.', 36),
    ('The Time Machine', 'H.G. Wells', 11.99, 'Victorian time travel.', 48),
    ('Slaughterhouse-Five', 'Kurt Vonnegut', 14.99, 'Time-traveling Billy Pilgrim.', 51),
    ('Ready Player One', 'Ernest Cline', 15.99, 'VR treasure hunt.', 62),
    ('Altered Carbon', 'Richard K. Morgan', 14.99, 'Consciousness transfer.', 45),
    ('The Expanse: Leviathan Wakes', 'James S.A. Corey', 16.99, 'Detective ship captain.', 53),
    ('Ancillary Justice', 'Ann Leckie', 15.49, 'AI seeks revenge.', 41),
    ('The Fifth Season', 'N.K. Jemisin', 16.99, 'Apocalyptic earth powers.', 47),
    ('Old Man\'s War', 'John Scalzi', 14.49, 'Elderly interstellar military.', 49),
    ('Seveneves', 'Neal Stephenson', 18.99, 'Escape dying Earth.', 38),
    ('Contact', 'Carl Sagan', 15.99, 'First contact with aliens.', 43),
    ('The War of the Worlds', 'H.G. Wells', 12.49, 'Martian invasion of Earth.', 45),
]

for i, (title, author, price, desc, stock) in enumerate(scifi):
    books.append({
        'id': book_id,
        'title': title,
        'author': author,
        'price': price,
        'category': 'Science Fiction',
        'description': desc,
        'stock': stock,
        'image': emojis[i % 4]
    })
    book_id += 1

# Fantasy (30 books)
fantasy = [
    ('The Hobbit', 'J.R.R. Tolkien', 15.99, 'Bilbo Baggins adventure.', 55),
    ('Harry Potter and the Sorcerer\'s Stone', 'J.K. Rowling', 16.99, 'Boy wizard discovers magic.', 65),
    ('The Name of the Wind', 'Patrick Rothfuss', 17.99, 'Legendary hero life story.', 43),
    ('A Game of Thrones', 'George R.R. Martin', 18.99, 'Political medieval fantasy.', 58),
    ('The Way of Kings', 'Brandon Sanderson', 19.99, 'Epic unique magic.', 47),
    ('The Fellowship of the Ring', 'J.R.R. Tolkien', 17.99, 'Epic Lord of the Rings.', 52),
    ('The Final Empire', 'Brandon Sanderson', 16.99, 'Thieves overthrow emperor.', 49),
    ('The Eye of the World', 'Robert Jordan', 18.49, 'Wheel of Time begins.', 45),
    ('American Gods', 'Neil Gaiman', 16.99, 'Old gods vs new.', 51),
    ('The Lies of Locke Lamora', 'Scott Lynch', 15.99, 'Con artists fantasy Venice.', 42),
    ('The Blade Itself', 'Joe Abercrombie', 16.49, 'Grimdark morally gray.', 40),
    ('Assassin\'s Apprentice', 'Robin Hobb', 15.49, 'Royal bastard assassin.', 44),
    ('The Poppy War', 'R.F. Kuang', 17.99, 'Chinese history fantasy.', 38),
    ('Gardens of the Moon', 'Steven Erikson', 18.99, 'Military fantasy epic.', 35),
    ('The Bear and the Nightingale', 'Katherine Arden', 15.99, 'Russian folklore fantasy.', 46),
    ('Circe', 'Madeline Miller', 16.99, 'Greek goddess retelling.', 53),
    ('The Ocean at the End of the Lane', 'Neil Gaiman', 14.99, 'Dark fairy tale.', 48),
    ('Uprooted', 'Naomi Novik', 15.99, 'Apprenticed to sorcerer.', 44),
    ('The Priory of the Orange Tree', 'Samantha Shannon', 19.99, 'Epic standalone dragons.', 41),
    ('Good Omens', 'Neil Gaiman & Terry Pratchett', 15.49, 'Comic apocalypse.', 56),
    ('Jonathan Strange & Mr Norrell', 'Susanna Clarke', 18.99, 'Magic in 19th century England.', 39),
    ('Words of Radiance', 'Brandon Sanderson', 20.99, 'Stormlight Archive book 2.', 43),
    ('Prince of Thorns', 'Mark Lawrence', 15.99, 'Dark fantasy antihero.', 37),
    ('The City of Brass', 'S.A. Chakraborty', 17.49, 'Middle Eastern fantasy.', 42),
    ('Warbreaker', 'Brandon Sanderson', 16.99, 'Color-based magic.', 45),
    ('The Once and Future King', 'T.H. White', 15.99, 'King Arthur retelling.', 40),
    ('Elantris', 'Brandon Sanderson', 15.49, 'Fallen magical city.', 38),
    ('The Golem and the Jinni', 'Helene Wecker', 16.99, '1899 New York magic.', 44),
    ('The Sword of Shannara', 'Terry Brooks', 14.99, 'Classic epic fantasy quest.', 41),
    ('The Black Prism', 'Brent Weeks', 17.49, 'Color-based magic system.', 39),
]

for i, (title, author, price, desc, stock) in enumerate(fantasy):
    books.append({
        'id': book_id,
        'title': title,
        'author': author,
        'price': price,
        'category': 'Fantasy',
        'description': desc,
        'stock': stock,
        'image': emojis[i % 4]
    })
    book_id += 1

# Mystery & Thriller (25 books)
mystery = [
    ('The Girl with the Dragon Tattoo', 'Stieg Larsson', 15.99, 'Swedish mystery thriller.', 51),
    ('Gone Girl', 'Gillian Flynn', 14.99, 'Psychological thriller marriage.', 46),
    ('The Da Vinci Code', 'Dan Brown', 16.49, 'Religious conspiracy thriller.', 54),
    ('Big Little Lies', 'Liane Moriarty', 13.99, 'School murder mystery.', 41),
    ('The Silent Patient', 'Alex Michaelides', 14.99, 'Woman stops speaking.', 49),
    ('In the Woods', 'Tana French', 15.49, 'Detective Irish woods.', 43),
    ('The Cuckoo\'s Calling', 'Robert Galbraith', 14.99, 'Private detective investigation.', 47),
    ('Sharp Objects', 'Gillian Flynn', 13.99, 'Reporter hometown murder.', 44),
    ('The Woman in the Window', 'A.J. Finn', 15.99, 'Agoraphobic witnesses crime.', 42),
    ('And Then There Were None', 'Agatha Christie', 12.99, 'Ten strangers trapped island.', 56),
    ('Murder on the Orient Express', 'Agatha Christie', 13.49, 'Poirot train murder.', 52),
    ('The Girl on the Train', 'Paula Hawkins', 14.99, 'Woman witnesses from train.', 48),
    ('Before I Go to Sleep', 'S.J. Watson', 13.99, 'Woman with amnesia.', 45),
    ('The Snowman', 'Jo Nesbø', 15.49, 'Detective hunts serial killer.', 41),
    ('The Dry', 'Jane Harper', 14.99, 'Detective drought hometown.', 46),
    ('Still Life', 'Louise Penny', 13.99, 'Inspector Gamache mystery.', 47),
    ('The Guest List', 'Lucy Foley', 14.99, 'Wedding turns deadly.', 50),
    ('The 7½ Deaths of Evelyn Hardcastle', 'Stuart Turton', 16.99, 'Groundhog Day mystery.', 43),
    ('Rebecca', 'Daphne du Maurier', 13.49, 'Gothic Manderley mystery.', 48),
    ('The Hunting Party', 'Lucy Foley', 14.49, 'New Year murder mystery.', 44),
    ('Dark Places', 'Gillian Flynn', 14.99, 'Family massacre investigation.', 42),
    ('The Kind Worth Killing', 'Peter Swanson', 15.49, 'Strangers plot murder.', 40),
    ('Into the Water', 'Paula Hawkins', 14.99, 'River with dark history.', 45),
    ('The Reversal', 'Michael Connelly', 15.99, 'Defense attorney prosecutes.', 40),
    ('The Poet', 'Michael Connelly', 15.99, 'Reporter investigates death.', 39),
]

for i, (title, author, price, desc, stock) in enumerate(mystery):
    books.append({
        'id': book_id,
        'title': title,
        'author': author,
        'price': price,
        'category': 'Mystery',
        'description': desc,
        'stock': stock,
        'image': emojis[i % 4]
    })
    book_id += 1

# Romance (20 books)
romance = [
    ('Pride and Prejudice', 'Jane Austen', 11.99, 'Elizabeth Bennet and Mr. Darcy.', 40),
    ('Outlander', 'Diana Gabaldon', 17.99, 'Time-travel Scotland romance.', 45),
    ('The Notebook', 'Nicholas Sparks', 12.99, 'Timeless love story.', 52),
    ('Me Before You', 'Jojo Moyes', 13.99, 'Caregiver quadriplegic love.', 48),
    ('The Hating Game', 'Sally Thorne', 12.49, 'Enemies-to-lovers office.', 44),
    ('Red, White & Royal Blue', 'Casey McQuiston', 14.99, 'President son British prince.', 51),
    ('The Kiss Quotient', 'Helen Hoang', 13.99, 'Woman hires escort.', 46),
    ('Beach Read', 'Emily Henry', 14.49, 'Romance writers challenge.', 49),
    ('The Flatshare', 'Beth O\'Leary', 13.99, 'Strangers share apartment.', 43),
    ('It Ends with Us', 'Colleen Hoover', 14.99, 'Love story dealing abuse.', 55),
    ('The Rosie Project', 'Graeme Simsion', 13.49, 'Professor seeks wife.', 42),
    ('Eleanor & Park', 'Rainbow Rowell', 12.99, 'Young adult 1986.', 47),
    ('The Time Traveler\'s Wife', 'Audrey Niffenegger', 15.99, 'Love complicated time travel.', 44),
    ('Jane Eyre', 'Charlotte Brontë', 12.49, 'Gothic romance criticism.', 38),
    ('Wuthering Heights', 'Emily Brontë', 11.99, 'Passionate destructive love.', 36),
    ('People We Meet on Vacation', 'Emily Henry', 14.99, 'Best friends trip.', 50),
    ('The Wedding Date', 'Jasmine Guillory', 13.99, 'Fake relationship real.', 45),
    ('Book Lovers', 'Emily Henry', 15.49, 'Literary agent editor.', 48),
    ('The Spanish Love Deception', 'Elena Armas', 14.99, 'Fake dating wedding.', 46),
    ('One Day', 'David Nicholls', 14.49, 'Twenty years one day.', 41),
]

for i, (title, author, price, desc, stock) in enumerate(romance):
    books.append({
        'id': book_id,
        'title': title,
        'author': author,
        'price': price,
        'category': 'Romance',
        'description': desc,
        'stock': stock,
        'image': emojis[i % 4]
    })
    book_id += 1

# Non-Fiction (20 books)
nonfiction = [
    ('Sapiens', 'Yuval Noah Harari', 18.99, 'Brief history of humankind.', 62),
    ('Educated', 'Tara Westover', 16.99, 'Memoir self-education family.', 56),
    ('Thinking, Fast and Slow', 'Daniel Kahneman', 17.99, 'Two systems of thinking.', 47),
    ('The Immortal Life of Henrietta Lacks', 'Rebecca Skloot', 15.99, 'Revolutionary medical cells.', 43),
    ('Atomic Habits', 'James Clear', 16.99, 'Building good habits.', 68),
    ('Homo Deus', 'Yuval Noah Harari', 19.99, 'Brief history tomorrow.', 51),
    ('The Power of Habit', 'Charles Duhigg', 16.49, 'Why we do what we do.', 54),
    ('Quiet', 'Susan Cain', 15.99, 'Power of introverts.', 49),
    ('Bad Blood', 'John Carreyrou', 17.99, 'Silicon Valley secrets.', 44),
    ('When Breath Becomes Air', 'Paul Kalanithi', 15.99, 'Neurosurgeon facing death.', 48),
    ('The Lean Startup', 'Eric Ries', 17.49, 'Entrepreneurs use innovation.', 46),
    ('Freakonomics', 'Steven D. Levitt', 15.99, 'Rogue economist explores.', 50),
    ('The Wright Brothers', 'David McCullough', 16.99, 'Aviation pioneers story.', 41),
    ('Born to Run', 'Christopher McDougall', 15.49, 'Hidden tribe running.', 45),
    ('The Gene', 'Siddhartha Mukherjee', 18.99, 'Intimate history genetics.', 39),
    ('Outliers', 'Malcolm Gladwell', 16.99, 'Story of success.', 52),
    ('The Emperor of All Maladies', 'Siddhartha Mukherjee', 19.99, 'Biography of cancer.', 38),
    ('Shoe Dog', 'Phil Knight', 17.99, 'Nike creator memoir.', 55),
    ('The Soul of an Octopus', 'Sy Montgomery', 15.99, 'Exploration of consciousness.', 42),
    ('The Body Keeps the Score', 'Bessel van der Kolk', 18.99, 'Brain healing trauma.', 51),
]

for i, (title, author, price, desc, stock) in enumerate(nonfiction):
    books.append({
        'id': book_id,
        'title': title,
        'author': author,
        'price': price,
        'category': 'Non-Fiction',
        'description': desc,
        'stock': stock,
        'image': '📚' if i % 5 == 0 else emojis[i % 4]
    })
    book_id += 1

# Biography (15 books)
biography = [
    ('Steve Jobs', 'Walter Isaacson', 19.99, 'Apple co-founder biography.', 50),
    ('Becoming', 'Michelle Obama', 18.99, 'Former First Lady memoir.', 64),
    ('The Diary of a Young Girl', 'Anne Frank', 12.99, 'Holocaust diary.', 55),
    ('Long Walk to Freedom', 'Nelson Mandela', 17.99, 'Anti-apartheid leader.', 42),
    ('Born a Crime', 'Trevor Noah', 15.99, 'Apartheid South Africa.', 53),
    ('Unbroken', 'Laura Hillenbrand', 16.99, 'WWII survival story.', 47),
    ('The Glass Castle', 'Jeannette Walls', 14.99, 'Unconventional upbringing.', 49),
    ('Einstein: His Life and Universe', 'Walter Isaacson', 18.99, 'Genius physicist.', 41),
    ('Alexander Hamilton', 'Ron Chernow', 19.99, 'Founding father biography.', 44),
    ('The Autobiography of Malcolm X', 'Malcolm X', 15.99, 'Civil rights leader.', 46),
    ('I Am Malala', 'Malala Yousafzai', 14.99, 'Girl stood for education.', 52),
    ('Wild', 'Cheryl Strayed', 15.49, 'Hiking Pacific Crest Trail.', 48),
    ('Benjamin Franklin', 'Walter Isaacson', 18.49, 'American polymath life.', 40),
    ('Yes Please', 'Amy Poehler', 14.99, 'Comedian honest memoir.', 45),
    ('Open', 'Andre Agassi', 16.99, 'Tennis legend autobiography.', 38),
]

for i, (title, author, price, desc, stock) in enumerate(biography):
    books.append({
        'id': book_id,
        'title': title,
        'author': author,
        'price': price,
        'category': 'Biography',
        'description': desc,
        'stock': stock,
        'image': '📚' if i % 5 == 0 else emojis[i % 4]
    })
    book_id += 1

# History (10 books)
history = [
    ('A People\'s History of the United States', 'Howard Zinn', 18.99, 'American history from below.', 45),
    ('Guns, Germs, and Steel', 'Jared Diamond', 17.99, 'Fates of human societies.', 48),
    ('The Silk Roads', 'Peter Frankopan', 19.99, 'New history of world.', 41),
    ('SPQR', 'Mary Beard', 18.49, 'History of Ancient Rome.', 39),
    ('Team of Rivals', 'Doris Kearns Goodwin', 19.99, 'Lincoln political genius.', 44),
    ('1491', 'Charles C. Mann', 17.99, 'Americas before Columbus.', 42),
    ('The Warmth of Other Suns', 'Isabel Wilkerson', 18.99, 'Epic Great Migration.', 47),
    ('The Devil in the White City', 'Erik Larson', 16.99, 'Murder 1893 World Fair.', 51),
    ('A Short History of Nearly Everything', 'Bill Bryson', 17.49, 'Science for layperson.', 54),
    ('The Sixth Extinction', 'Elizabeth Kolbert', 16.99, 'Unnatural history.', 43),
]

for i, (title, author, price, desc, stock) in enumerate(history):
    books.append({
        'id': book_id,
        'title': title,
        'author': author,
        'price': price,
        'category': 'History',
        'description': desc,
        'stock': stock,
        'image': '📚' if i % 5 == 0 else emojis[i % 4]
    })
    book_id += 1

# Self-Help (5 books)
selfhelp = [
    ('The 7 Habits of Highly Effective People', 'Stephen Covey', 16.99, 'Timeless effectiveness principles.', 70),
    ('How to Win Friends and Influence People', 'Dale Carnegie', 14.99, 'Classic relationship guide.', 65),
    ('The Power of Now', 'Eckhart Tolle', 15.99, 'Spiritual enlightenment guide.', 58),
    ('Daring Greatly', 'Brené Brown', 16.49, 'Vulnerability and courage.', 54),
    ('The Subtle Art of Not Giving a F*ck', 'Mark Manson', 15.49, 'Counterintuitive life approach.', 62),
]

for i, (title, author, price, desc, stock) in enumerate(selfhelp):
    books.append({
        'id': book_id,
        'title': title,
        'author': author,
        'price': price,
        'category': 'Self-Help',
        'description': desc,
        'stock': stock,
        'image': '📚'
    })
    book_id += 1

# Children's Books (5 books)
children = [
    ('Where the Wild Things Are', 'Maurice Sendak', 9.99, 'Classic imagination picture book.', 75),
    ('The Very Hungry Caterpillar', 'Eric Carle', 8.99, 'Caterpillar transformation.', 80),
    ('Charlotte\'s Web', 'E.B. White', 11.99, 'Friendship pig and spider.', 68),
    ('Matilda', 'Roald Dahl', 12.99, 'Brilliant girl telekinetic.', 72),
    ('The Giving Tree', 'Shel Silverstein', 10.99, 'Story about selfless love.', 70),
]

for i, (title, author, price, desc, stock) in enumerate(children):
    books.append({
        'id': book_id,
        'title': title,
        'author': author,
        'price': price,
        'category': 'Children',
        'description': desc,
        'stock': stock,
        'image': emojis[i % 4]
    })
    book_id += 1

# Save to JSON
with open('books_200.json', 'w') as f:
    json.dump(books, f, indent=2)

print(f'✅ Generated {len(books)} books successfully!')
print(f'Categories: Fiction(40), Sci-Fi(30), Fantasy(30), Mystery(25), Romance(20), Non-Fiction(20), Biography(15), History(10), Self-Help(5), Children(5)')
