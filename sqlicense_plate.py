import sqlite3


# Create database and table
def create_database():
    conn = sqlite3.connect("license_plates.db")
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS plates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        license_plate TEXT UNIQUE
    );
    """)
    conn.commit()
    conn.close()


# Add license plate to the database
def add_license_plate(license_plate):
    conn = sqlite3.connect("license_plates.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO plates (license_plate) VALUES (?)", (license_plate,))
    except sqlite3.IntegrityError:
        print("Duplicate entry. Ignored.")
    conn.commit()
    conn.close()


# Check if license plate exists in the database
def check_license_plate(license_plate):
    conn = sqlite3.connect("license_plates.db")
    c = conn.cursor()
    c.execute("SELECT * FROM plates WHERE license_plate=?", (license_plate,))
    result = c.fetchone()
    conn.close()
    return "RECOGNIZED: " + license_plate if result else "NO DATA ON: " + license_plate

# Create the database and table
# create_database()

# Add some test data
# add_license_plate("ABC123")

# Test the function
# print(check_license_plate("ABC123"))  # Should print "RECOGNIZED"
# print(check_license_plate("NOT_IN_DB"))  # Should print "NO DATA"
