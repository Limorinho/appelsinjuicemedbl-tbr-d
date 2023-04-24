import random

names = ['Jed Mueller', 'Liana Larson', 'Aleeza Trujillo', 'Ellie-May Clarke', 'Priya Khan', 'Kaleb Webb',
         'Roger Edwards', 'Natalia Wilkins', 'Wojciech Huffman', 'Kye Bolton', 'Francesca Duffy', 'Adem O\'Doherty',
         'Hayden Allen', 'Kingsley Hensley', 'Stevie Daniel', 'Briony Richardson', 'Sienna Garner', 'Davina Weeks',
         'Cohen Graves', 'Xavier Hale', 'Jodie Mccullough', 'Katherine Black', 'Aaron Lawrence', 'Aamina Middleton',
         'Penelope Cantu', 'Arran Stanley', 'Hattie Green', 'Mohammad Spence', 'Freya Harris', 'Zarah Mckay',
         'Halima Pope', 'Regan Wong', 'Willie Ramos', 'Anisha Robertson', 'Darcy Fitzgerald', 'Richie Bean',
         'Valerie Pitts', 'Rhonda Blackburn', 'Melvin Parrish', 'Maxim Collier', 'Jasmine Riley', 'Lyla Preston',
         'Christian Tanner', 'Ariana Escobar', 'Kyle Walsh', 'Eric Ward', 'Jade Sharp', 'Jaydon Marquez',
         'Kaan Eaton', 'Gloria Camacho', 'Rio Booker', 'Arianna Stone', 'Franciszek Barlow', 'Sulayman Massey',
         'Karim Cain', 'Lucia Owen', 'Evangeline Rivera', 'Ali Lucas', 'Emil Dalton', 'Joao Brady',
         'Abdulrahman Sloan', 'Kristian Rivers', 'Kiara Rubio', 'Kamal Ryan', 'Luis Sanchez', 'Jaime Newman',
         'Hussain Lowe', 'Imogen Sanders', 'Abi Cabrera', 'Lance Faulkner', 'Alastair Rose', 'Logan Donnelly',
         'Rex Mccarthy', 'Millie England', 'Lee Boone', 'Greta Cannon', 'Tammy Waller', 'Sidney Austin',
         'Carrie Dorsey', 'Tiffany Sheppard', 'Otis Sullivan', 'Edie Cisneros', 'Ted Francis', 'Hamza Odonnell',
         'Caitlyn Wagner', 'Aneesa Levy', 'Gilbert Fox', 'James Sawyer', 'Josh Terrell', 'Ivan Raymond',
         'Owais English', 'Amaan Kim', 'Derek Aguirre', 'Wayne Herman', 'Mark O\'Neill', 'Cain Castillo',
         'David Branch', 'Rachael Shannon', 'Reuben Blackwell', 'Denise Long']


domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com", "protonmail.com"]


for name in names:
    domain = random.choice(domains)
    email = name.lower() + "@" + domain
    print("(\"" + name + "\", \"" + email + "\", " + str(random.randint(0, 2023)) + "),")
