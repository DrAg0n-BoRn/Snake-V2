from turtle import Turtle as Turtle_class
from snake import SCREEN_HEIGHT
from tkinter import messagebox, simpledialog
import sqlite3
import datetime as dt

FONT = ("Courier", 16, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle_class):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.score = 0
        self.high_score = 0
        self.get_initial_score()
        self.update_board()
    
    def get_initial_score(self):
        # Get high score from database
        db = sqlite3.connect('scores.db')
        try:
            score_ = list(db.execute("SELECT MAX(score) FROM players"))
        except sqlite3.OperationalError:
            db.close()
            create_table()
            self.high_score = 0
        else:
            db.close()
            if check_cursor(score_):
                for tuple_ in score_:
                    self.high_score = tuple_[0]
            else:
                self.high_score = 0
        
    def update_board(self):
        self.clear()
        self.goto(x=-75, y=SCREEN_HEIGHT * 0.45)
        self.write(arg=f"SCORE: {self.score}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(x=75, y=SCREEN_HEIGHT * 0.45)
        self.write(arg=f"HIGH SCORE: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.score += 1
        self.update_board()

    def reset_scoreboard(self):
        if self.high_score < self.score:
            self.high_score = self.score
        self.score = 0
        self.update_board()
        
    def game_over(self) -> bool:
        """Returns True if game over."""
        # Player name
        player_name = " "
        while not player_name.isalnum():
            player_name = simpledialog.askstring(title="Game Over", prompt="Your Name: ", initialvalue="Guest")
            if player_name is None:
                return True
                
        self.update_player_score(name=player_name)
        
        answer = messagebox.askyesno(title="Game Over", message=f"Your score: {self.score}\nPlay again?")
        self.reset_scoreboard()
        return not answer
    
    def update_player_score(self, name: str):
        # Format data
        name = name.upper()
        today = str(dt.datetime.now()).split(" ")[0]
        
        # Update database
        db = sqlite3.connect('scores.db')
        
        # Fetch, check and update data
        stored_score_cursor = list(db.execute("SELECT score FROM players WHERE name = ?", (name,)))
        # Found
        if check_cursor(stored_score_cursor):
            for tuple_ in stored_score_cursor:
                if self.score > tuple_[0]:
                    # print(f"AN UPDATE SHOULD HAPPEN for {name}")
                    db.execute("UPDATE players SET score = ?, date = ? WHERE name = ?", (self.score, today, name))
                    db.commit()
        # Not found
        else:
            # print(f"Insert new record for {name}")
            db.execute("INSERT INTO players(name, score, date) VALUES(?, ?, ?)", (name, self.score, today))
            db.commit()
            
        db.close()


def check_cursor(cursor) -> bool:
    """Returns True if cursor not empty or NULL"""
    test_ = []
    for row in cursor:
        test_.extend(row)
    if None in test_ or len(test_) == 0:
        return False
    else:
        return True
        

def create_table():
    db = sqlite3.connect('scores.db')
    db.execute('''CREATE TABLE players(
        name TEXT NOT NULL PRIMARY KEY, 
        score INTEGER NOT NULL,
        date TEXT NOT NULL);''')
    db.close()
    
    
def get_best() -> list:
    """Returns a list of dict with the top 3 players"""
    db = sqlite3.connect('scores.db')
    data = list(db.execute("SELECT * FROM players ORDER BY score DESC LIMIT(3)"))
    db.close()
    if not check_cursor(data):
        return None

    chicken_dinner = []
    for tuple_ in data:
        helper = {}
        helper["player"] = tuple_[0]
        helper["score"] = tuple_[1]
        helper["date"] = tuple_[2]
        chicken_dinner.append(helper)
    
    return chicken_dinner
    