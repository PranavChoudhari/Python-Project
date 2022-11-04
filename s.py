import sqlite3


conn = sqlite3.connect("database.db")
cur = conn.cursor()

n = 0
acc_no = 10000000003
aadhar_no = 214867896542
mob_num = 9876543210
i=1
name = ["Michael"
"Christopher",
"Jessica",
"Matthew",
"Ashley",
"Jennifer",
"Joshua",
"Amanda",
"Daniel",
"David",
"James",
"Robert",
"John",
"Joseph",
"Andrew",
"Ryan",
"Brandon",
"Jason",
"Justin",
"Sarah",
"William",
"Jonathan",
"Stephanie",
"Brian",
"Nicole",
"Nicholas",
"Anthony",
"Heather",
"Eric",
"Elizabeth",
"Adam",
"Megan",
"Melissa",
"Kevin",
"Steven",
"Thomas",
"Timothy",
"Christina",
"Kyle",
"Rachel",
"Laura",
"Lauren",
"Amber",
"Brittany",
"Danielle",
"Richard",
"Kimberly",
"Jeffrey",
"Amy",
"Crystal",
"Michelle",
"Tiffany",
"Jeremy",
"Benjamin",
"Mark",
"Emily",
"Aaron",
"Charles",
"Rebecca",
"Jacob",
"Stephen",
"Patrick",
"Sean",
"Erin",
"Zachary",
"Jamie",
"Kelly",
"Samantha",
"Nathan",
"Sara",
"Dustin",
"Paul",
"Angela",
"Tyler",
"Scott",
"Katherine",
"Andrea",
"Gregory",
"Erica",
"Mary",
"Travis",
"Lisa",
"Kenneth",
"Bryan",
"Lindsey",
"Kristen",
"Jose",
"Alexander",
"Jesse",
"Katie",
"Lindsay",
"Shannon",
"Vanessa",
"Courtney",
"Christine",
"Alicia",
"Cody",
"Allison",
"Bradley",
"Samuel"]
while n < len(name):
    mob_num = mob_num + 1
    aadhar_no = aadhar_no + 1
    acc_no = acc_no + 1
    cur.execute("INSERT INTO accounts VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (acc_no,name[i-1], aadhar_no + 1, f"dummy_street{n}", f"py_dummy_email_{n}@pyproject.com", 0.0, 1234, mob_num))
    n = n + 1
    i = i +1

conn.commit()

#omkarzore771981@gmail.com
#pranavchoudhary992@gmail.com