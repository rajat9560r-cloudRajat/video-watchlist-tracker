import sqlite3

con=sqlite3.connect('sqlite_yt')
cur=con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL 
            )''')

def add_video(name,time):

    cur.execute('INSERT INTO videos (name,time) VALUES (?,?)', (name,time))
    con.commit()

def show_videos():
    cur.execute('SELECT * FROM videos')
    data=cur.fetchall()
    if data:
        for row in data:
            print(row,)
    else:
        print('Empty')

def delete_video(id):
    cur.execute('Delete FROM videos WHERE id = ?',(id,))
    con.commit()
    if cur.rowcount == 0:
        print('Id not valid')
    else:
        print('Deleted')


def update_video(id,time):
    cur.execute('UPDATE videos SET time = ? WHERE id = ? ',(time,id))
    con.commit()
    if cur.rowcount == 0:
        print('Something is fishy [ not updated ]')
    else:
        print('Updated ')

def main():
    while True: 
        print('ITS ALWAYS YOURS, NOW WITH SQLITE3')
        print('1. Add video details')
        print('2. Show video details')
        print('3. Delete video details')
        print('4. Update video\\s duration')
        print('5. Exit app')
        try:
            user=input('Enter your input: ')

            if user == '1':
                name=input('Enter video name: ')
                time=input('Enter video time: ')
                add_video(name,time)

            elif user == '2':
                show_videos()

            elif user == '3':
                id=int(input('Enter video id to delete: '))
                delete_video(id)

            elif user == '4':
                id=int(input('Enter video id to update its time: '))
                time=input('Enter new time: ')
                update_video(id,time)

            elif user == '5':
                break

            else:
                print('Enter valid input')
        except ValueError:
            print('Enter integers not letters')

    con.close()

if __name__=='__main__':
    try:    
        main()
    finally:
        con.close()