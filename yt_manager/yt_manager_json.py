#youtube video manager CLI
import json 

def load_data():
    try:
        with open('yt_json.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
   
def helper_method(videos):
    with open('yt_json.txt','w') as file:
        json.dump(videos,file,indent=4)

def show_all_videos(videos):
    if videos:
        print('\n')
        print('*' *150)
        for i, val in enumerate(videos, start=1):
            print(f'{i}. {val['name']} ----> {val['time'] }')
        print('*' *150)
    else:
        print('Empty bucket')
    
def add_a_video(videos):
    name= input('Enter video name: ')
    time=input('Enter video time: ')
    videos.append({'name':name, 'time':time })
    helper_method(videos)
    print('Details added ✅')

def update_a_video(videos):
    show_all_videos(videos)
    index=int(input('Enter which numberth you want to update: '))
    if 1<= index <= len(videos):
        name=input('Enter new name: ')
        time=input('Enter new time: ')
        videos[index-1] = {'name':name, 'time':time}
        helper_method(videos)
    else:
        print('Invalid result')

def delete_a_video(videos):
    show_all_videos(videos)
    index=int(input('Enter which video you want to delete: '))
    if 1<= index <=len(videos):
        del videos[index-1]
        helper_method(videos)
        print('Details deleted ⚒️')
    else:
        print('Invalid index no: ')
        
def main():
    videos=load_data()
    while True:
        print('Welcome to yt manager app ')
        print('1. Show all vids')
        print('2. Add a vid')
        print('3. Update a vid')
        print('4. Delete a vid')
        print('5. Exit the app')

        response=input('Enter your mood: ')
        match response:
            case '1':
                show_all_videos(videos)
            case '2':
                add_a_video(videos)
            case '3':
                update_a_video(videos)
            case '4':
                delete_a_video(videos)
            case '5':
                break
            case _:
                print('Invalid choice')

if __name__ == '__main__':
    main()
        
            
    