#YT manager- hold video length and video duration [ just like a todo app]
import json

def load_video():
    try:
        with open('whatsapp.json','r') as file:
            return json.load(file)
             
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_video(video):
    with open('whatsapp.json','w') as file:
        json.dump(video,file,indent=4)

def add_video(video):
    name= input('Enter video name: ')
    duration= input('Enter video duration: ')
    video.append({'name':name, 'duration':duration })
    save_video(video)
    print('Video added ✅ \n')

def show_videos(video):
    if video:
        print('*'*150)
        for i,val in enumerate(video,start=1):
            print(f"{i}. {val['name']} --> {val['duration']}")
        print('*'*150)
    else:
        print('Empty list 🙋‍♂️ \n')

def delete_video(video):
    show_videos(video)
    index=int(input('Enter which numberth video details you want to delete: '))
    try:
        if 1<= index <=len(video):
            del video[index-1]
            save_video(video)
            print('Details deleted ⚒️\n')
            show_videos(video)
        else:
            print('Index not available 🤷‍♂️\n')
    except ValueError:
        print('Enter integers, not characters')

def update_duration_only(video):
    show_videos(video)
    no=int(input('Enter which numberth video detail to update(duration): '))
    try:
        if 1<= no <=len(video):
            duration=input('Enter new duration detail: ')
            video[no-1]['duration']=duration
            print('Updated')
            save_video(video)
            show_videos(video)
        else:
            print('Invalid numberth')
    except ValueError:
        print('Enter integers, not characters')

def main():
    video=load_video()

    while True:
        print('ITS COMPLETELY YOURS, CHOOSE YOUR OPTION 🏓')
        print('1. Add video details')
        print('2. Show video details')
        print('3. Delete video details')
        print('4. Update video\\s duration')
        print('5. Exit app')       
        user_input=input('Enter your option: ')
        match user_input:
            case '1':
                add_video(video)
            case '2':
                show_videos(video)
            case '3':
                delete_video(video)
            case '4':
                update_duration_only(video)
            case '5':
                break
            case _:
                print('Invalid input, try again! 🗣️')

if __name__=='__main__':
    main()