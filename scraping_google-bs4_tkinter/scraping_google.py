from tkinter import *
from tkinter.messagebox import showinfo
from bs4 import BeautifulSoup 
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}



def action():
    ### Code For Receiving Query
    query=textF.get()
    textF.delete(0,END)
    print(query)
    def google(query):
        query = query.replace(" ","+")
        try:
            url = f'https://www.google.com/search?q={query}&oq={query}&aqs=chrome..69i57j46j69i59j35i39j0j46j0l2.4948j0j7&sourceid=chrome&ie=UTF-8'
            res = requests.get(url,headers=headers)
            soup = BeautifulSoup(res.text,'html.parser')
        except:
            print("Make sure you have a internet connection")
        try:
            try:
                ans = soup.select('.RqBzHd')[0].getText().strip()
            
            except:
                try:
                    title=soup.select('.AZCkJd')[0].getText().strip()
                    try:
                        ans=soup.select('.e24Kjd')[0].getText().strip()
                    except:
                        ans=""
                    ans=f'{title}\n{ans}'
                    
                except:
                    try:
                        ans=soup.select('.hgKElc')[0].getText().strip()
                    except:
                        ans=soup.select('.kno-rdesc span')[0].getText().strip()
        
        except:
            ans = "can't find on google"
        return ans
    
    result = google(str(query))
    showinfo(title="Result For Your Query", message=result)



main = Tk()
main.geometry("300x100")
main.title("Karl")
top = Frame(main)
top.pack(side=TOP)

textF = Entry(main,font=("helvetica",14,"bold"))
textF.focus()
textF.pack(fill=X,pady=5)
textF.insert(0,"Enter your query")
textF.configure(state=DISABLED)

def on_click(event):
    textF.configure(state=NORMAL)
    textF.delete(0,END)
    textF.unbind('<Button-1>',on_click_id)

on_click_id = textF.bind('<Button-1>',on_click)



btn = Button(main,text="Search",font=("Verdana",16),command=action)
btn.pack()
main.mainloop()
