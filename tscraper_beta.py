### REQUIREMENT ### CHROME needs to be installed
# Currently only tested on Windows

####IMPORTS####
from tkinter import *
from ttkthemes import ThemedTk # For GUI theme
from Scweet.scweet import scrap
import pandas as pd
import pathlib

####FUNCTIONS####

# Have user double check input and start query
def clickbutton():
    if (search_words_entry_2.get() != "" or search_hash_entry_2.get() != "") or (start_date_entry_2.get() != "" and end_date_entry_2.get() != ""):
        # if a new timeframe but no coin was specified
        if (search_words_entry_2.get() == "" and search_hash_entry_2.get() == "") and (start_date_entry_2.get() != "" and end_date_entry_2.get() != ""):
            display_text = Label(window, text=f"Double check the input data! \n Query hashtag: {search_hash_entry.get()}\n Query words: {search_words_entry.get()}\n Tweet limit per day: {query_limit_entry.get()}\n Start date: {start_date_entry.get()}\n End date: {end_date_entry.get()} \n Second query start date: {start_date_entry_2.get()}\n Second query end date: {end_date_entry_2.get()} \n From user: {user_account_entry.get()}\n This may take a while!", bg="ivory2")
            
        # if a new coin but no timeframe was specified
        elif (search_words_entry_2.get() != "" or search_hash_entry_2.get() != "") and (start_date_entry_2.get() == "" and end_date_entry_2.get() == ""):
            display_text = Label(window, text=f"Double check the input data! \n Query hashtag: {search_hash_entry.get()}\n Query words: {search_words_entry.get()} \n Second query hashtag: {search_hash_entry_2.get()}\n Second query words: {search_words_entry_2.get()}\n Tweet limit per day: {query_limit_entry.get()}\n Start date: {start_date_entry.get()}\n End date: {end_date_entry.get()} \n From user: {user_account_entry.get()}\n This may take a while!", bg="ivory2")
            
        # if a new coin and timeframe was specified
        elif (search_words_entry_2.get() != "" or search_hash_entry_2.get() != "") and (start_date_entry_2.get() != "" and end_date_entry_2.get() != ""):
            display_text = Label(window, text=f"Double check the input data! \n Query hashtag: {search_hash_entry.get()}\n Query words: {search_words_entry.get()} \n Second query hashtag: {search_hash_entry_2.get()}\n Second query words: {search_words_entry_2.get()}\n Tweet limit per day: {query_limit_entry.get()}\n Start date: {start_date_entry.get()}\n End date: {end_date_entry.get()} \n Second query start date: {start_date_entry_2.get()}\n Second query end date: {end_date_entry_2.get()} \n From user: {user_account_entry.get()}\n This may take a while!", bg="ivory2")
            
        display_text.pack_forget()
        display_text.pack(pady=10)
        query_button = ttk.Button(window, text="Start Query", command=lambda:[scraper(), scraper_more(), process()])
        query_button.pack_forget()
        query_button.pack(pady=10)
        return
    
    else:
        display_text = Label(window, text=f"Double check the input data! \n Query hashtag: {search_hash_entry.get()}\n Query words: {search_words_entry.get()}\n Tweet limit per day: {query_limit_entry.get()}\n Start date: {start_date_entry.get()}\n End date: {end_date_entry.get()} \n From user: {user_account_entry.get()}\n This may take a while!", bg="ivory2")
        display_text.pack_forget()
        display_text.pack(pady=10)
        query_button = ttk.Button(window, text="Start Query", command=lambda:[scraper(), scraper_more(), process()])
        query_button.pack_forget()
        query_button.pack(pady=10)
        return

# Actual scraper function that makes use of the Scweeter module
def scraper():
    # different call if limit of tweets per interval set
    try:
        if query_limit_entry.get() == "":
            data = scrap(words=search_words_entry.get().split(","), hashtag=search_hash_entry.get(), start_date=start_date_entry.get(), max_date=end_date_entry.get(), from_account = user_account_entry.get(),interval=1, headless=True, display_type="Top", save_images=False, resume=False, filter_replies=True, proximity=False)
        else:
            data = scrap(words=search_words_entry.get().split(","), hashtag=search_hash_entry.get(), start_date=start_date_entry.get(), max_date=end_date_entry.get(), from_account = user_account_entry.get(),interval=1, headless=True, display_type="Top", save_images=False, resume=False, filter_replies=True, proximity=False, limit=int(query_limit_entry.get()))
        return data
    except:
        error_box = messagebox.showerror(title="Input Error", message="Please review your query input and format!")
        
# scraper for comparison with other timeframe or coin
def scraper_more():
    # if comparison was not used
    if search_words_entry_2.get() == "" and search_hash_entry_2.get() == "" and start_date_entry_2.get() == "" and end_date_entry_2.get() == "":
        return
    # if no query limit is used
    elif query_limit_entry.get() == "":
        # if a new timeframe but no coin was specified
        if (search_words_entry_2.get() == "" and search_hash_entry_2.get() == "") and (start_date_entry_2.get() != "" and end_date_entry_2.get() != ""):
            data2 = scrap(words=search_words_entry.get().split(","), hashtag=search_hash_entry.get(), start_date=start_date_entry_2.get(), max_date=end_date_entry_2.get(), from_account = user_account_entry.get(),interval=1, headless=True, display_type="Top", save_images=False, resume=False, filter_replies=True, proximity=False)
        # if a new coin but no timeframe was specified
        elif (search_words_entry_2.get() != "" or search_hash_entry_2.get() != "") and (start_date_entry_2.get() == "" and end_date_entry_2.get() == ""):
            data2 = scrap(words=search_words_entry_2.get().split(","), hashtag=search_hash_entry_2.get(), start_date=start_date_entry.get(), max_date=end_date_entry.get(), from_account = user_account_entry.get(),interval=1, headless=True, display_type="Top", save_images=False, resume=False, filter_replies=True, proximity=False)
        # if a new coin and timeframe was specified
        elif (search_words_entry_2.get() != "" or search_hash_entry_2.get() != "") and (start_date_entry_2.get() != "" and end_date_entry_2.get() != ""):
            data2 = scrap(words=search_words_entry_2.get().split(","), hashtag=search_hash_entry_2.get(), start_date=start_date_entry_2.get(), max_date=end_date_entry_2.get(), from_account = user_account_entry.get(),interval=1, headless=True, display_type="Top", save_images=False, resume=False, filter_replies=True, proximity=False)
    # if query limit is used
    else:
        # if a new timeframe but no coin was specified
        if (search_words_entry_2.get() == "" and search_hash_entry_2.get() == "") and (start_date_entry_2.get() != "" and end_date_entry_2.get() != ""):
            data2 = scrap(words=search_words_entry.get().split(","), hashtag=search_hash_entry.get(), start_date=start_date_entry_2.get(), max_date=end_date_entry_2.get(), from_account = user_account_entry.get(),interval=1, headless=True, display_type="Top", save_images=False, resume=False, filter_replies=True, proximity=False, limit=int(query_limit_entry.get()))
        # if a new coin but no timeframe was specified
        elif (search_words_entry_2.get() != "" or search_hash_entry_2.get() != "") and (start_date_entry_2.get() == "" and end_date_entry_2.get() == ""):
            data2 = scrap(words=search_words_entry_2.get().split(","), hashtag=search_hash_entry_2.get(), start_date=start_date_entry.get(), max_date=end_date_entry.get(), from_account = user_account_entry.get(),interval=1, headless=True, display_type="Top", save_images=False, resume=False, filter_replies=True, proximity=False, limit=int(query_limit_entry.get()))
        # if a new coin and timeframe was specified
        elif (search_words_entry_2.get() != "" or search_hash_entry_2.get() != "") and (start_date_entry_2.get() != "" and end_date_entry_2.get() != ""):
            data2 = scrap(words=search_words_entry_2.get().split(","), hashtag=search_hash_entry_2.get(), start_date=start_date_entry_2.get(), max_date=end_date_entry_2.get(), from_account = user_account_entry.get(),interval=1, headless=True, display_type="Top", save_images=False, resume=False, filter_replies=True, proximity=False, limit=int(query_limit_entry.get()))
    
    return data2


# Collect data needed from the GUI for processing and read in output file 
def process():
    # for the future, it is probably best to make these global variables 
    path = pathlib.Path(__file__).parent.absolute()
    words = search_words_entry.get().split(',')
    hashtags = search_hash_entry.get().split(',')
    timeframe_start = start_date_entry.get()
    timeframe_end = end_date_entry.get()
    df = pd.read_csv(f'{path}\outputs\{words[0]}_{start_date_entry.get()}_{end_date_entry.get()}.csv')
    listi = [list(row) for row in df.values]
    
    if (search_words_entry_2.get() != "" or search_hash_entry_2.get() != "") or (start_date_entry_2.get() != "" and end_date_entry_2.get() != ""):
        # if a new timeframe but no coin was specified
        if (search_words_entry_2.get() == "" and search_hash_entry_2.get() == "") and (start_date_entry_2.get() != "" and end_date_entry_2.get() != ""):
            words2 = search_words_entry.get().split(',')
            hashtags2 = search_hash_entry.get().split(',')
            timeframe_start2 = start_date_entry_2.get()
            timeframe_end2 = end_date_entry_2.get()
            df2 = pd.read_csv(f'{path}\outputs\{words2[0]}_{timeframe_start2}_{timeframe_end2}.csv')
            listi2 = [list(row) for row in df2.values]
        # if a new coin but no timeframe was specified
        elif (search_words_entry_2.get() != "" or search_hash_entry_2.get() != "") and (start_date_entry_2.get() == "" and end_date_entry_2.get() == ""):
            words2 = search_words_entry_2.get().split(',')
            hashtags2 = search_hash_entry_2.get().split(',')
            timeframe_start2 = timeframe_start
            timeframe_end2 = timeframe_end
            df2 = pd.read_csv(f'{path}\outputs\{words2[0]}_{timeframe_start2}_{timeframe_end2}.csv')
            listi2 = [list(row) for row in df2.values]
        # if a new coin and timeframe was specified
        elif search_words_entry_2.get() != "" or search_hash_entry_2.get() != "" and (start_date_entry_2.get() != "" and end_date_entry_2.get() != ""):
            words2 = search_words_entry_2.get().split(',')
            hashtags2 = search_hash_entry_2.get().split(',')
            timeframe_start2 = start_date_entry_2.get()
            timeframe_end2 = end_date_entry_2.get()
            df2 = pd.read_csv(f'{path}\outputs\{words2[0]}_{timeframe_start2}_{timeframe_end2}.csv')
            listi2 = [list(row) for row in df2.values]
            
        #also put new button to visualize data for user
        proceed_button = ttk.Button(window, text="Proceed", command=lambda:[clear(), visualize(listi, hashtags, words, timeframe_start, timeframe_end), visualize(listi2, hashtags2, words2, timeframe_start2, timeframe_end2)]).pack(pady=10)
        return
    else:
        proceed_button = ttk.Button(window, text="Proceed", command=lambda:[clear(), visualize(listi, hashtags, words, timeframe_start, timeframe_end)]).pack(pady=10)
        return

#find all widgets of the window
def all_children():
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())
            
    return _list

#clear window
def clear():
    widget_list = all_children()
    
    for item in widget_list:
        item.pack_forget()
        
    return

#takes a list constructed from .csv output file of query and the words from initial query
def visualize(_list, hashtag, query, start, end):
    # initialize
    t_count = 0
    likes = 0
    retweets = 0
    most_liked_content = ""
    most_liked_content_user = ""
    most_retweeted_content = ""
    most_retweeted_content_user = ""
    
    # iterate through list (and list of lists)
    for x in _list:
        #to count tweets that were found
        t_count += 1
        
        #strip newlines
        for y in x:
            # try except for non-str elements
            try:
                y.replace('\n', '')
            except:
                pass
            
        #fix e.g. 2.6K to 2600 in likes so we can use it later to compare
        if 'K' in str(x[7]):
            x[7] = x[7].replace('.', '')
            x[7] = int(x[7].replace('K','00'))
        
        #fix e.g. 2.6K to 2600 in retweets for later comparison
        if 'K' in str(x[8]):
            x[8] = x[8].replace('.', '')
            x[8] = int(x[8].replace('K','00'))

        #assign most liked tweet
        # try except for unassigned likes/retweets ("NaN" - not a number)
        try:
            if int(x[7]) > likes:
                likes = int(x[7])
                most_liked_content = x[3]
                most_liked_content_user = x[1]
            
            #assign most retweeted tweet
            if int(x[8]) > retweets:
                retweets = int(x[8])
                most_retweeted_content = x[3]
                most_retweeted_content_user = x[1]
        except:
            continue
        
    # For private account, likes/retweets not available and "NAN" in the list
    # Workaround for now is checking if all tweets were unavailable for likes/retweets
    if most_liked_content == "":
        # And then just set the first entry to be most liked
        try:
            most_liked_content = _list[0][3]
            most_liked_content_user = _list[0][1]
            likes = "unavailable"
        except:
            most_liked_content = "No tweets were found for this query."
    # Same workaround for unavailable retweets     
    if most_retweeted_content == "":
        # Just set the first entry to be most liked
        try:
            most_retweeted_content = _list[0][3]
            most_retweeted_content_user = _list[0][1]
            retweets = "unavailable"
        except:
            most_retweeted_content = "No tweets were found for this query."
            
    #print findings for user to read
    if likes == 0:
        content = Label(window, text = f'No tweets were found for this query: {", ".join(str(x) for x in query)}. Hashtag(s): {", ".join(str(x) for x in hashtag)}. From {start} to {end}.', bg="ivory2").pack(padx=10,pady=10)
    elif hashtag[0] != '':
        if query[0] != '':
            content = Label(window, text = f'{t_count} tweets were found for the query of {", ".join(str(x) for x in query)} and hashtag(s) {", ".join(str(x) for x in hashtag)} from {start} to {end}.\n\n The most liked tweet was: \n {most_liked_content} \n by {most_liked_content_user} with {likes} likes. \n\n The most retweeted content was: \n {most_retweeted_content} \n by {most_retweeted_content_user} with {retweets} retweets.', bg="ivory2").pack(padx=10, pady=10)
        else:
            content = Label(window, text = f'{t_count} tweets were found for the hashtag(s) {", ".join(str(x) for x in hashtag)} from {start} to {end}.\n\n The most liked tweet was: \n {most_liked_content} \n by {most_liked_content_user} with {likes} likes. \n\n The most retweeted content was: \n {most_retweeted_content} \n by {most_retweeted_content_user} with {retweets} retweets.', bg="ivory2").pack(padx=10, pady=10)
    elif query[0] != '':
        content = Label(window, text = f'{t_count} tweets were found for the query of {", ".join(str(x) for x in query)} from {start} to {end}.\n\n The most liked tweet was: \n {most_liked_content} \n by {most_liked_content_user} with {likes} likes. \n\n The most retweeted content was: \n {most_retweeted_content} \n by {most_retweeted_content_user} with {retweets} retweets.', bg="ivory2").pack(padx=10, pady=10)
    
    #terminate window and program
    #quit_button = ttk.Button(window, text="Quit", command=window.destroy).pack()
    return

def compare():
 
    label_2.pack(padx=10, pady=10)
    search_hash_2.pack(padx=10)
    search_hash_entry_2.pack(padx=10)
    search_words_2.pack(padx=10)
    search_words_entry_2.pack(padx=10)
    start_date_2.pack(padx=10)
    start_date_entry_2.pack(padx=10)
    end_date_2.pack(padx=10)
    end_date_entry_2.pack(padx=10)

    ok_button.pack_forget()
    ok_button.pack(padx=10, pady=10)
    
    

####STUFF####

# window parameters
window = ThemedTk(theme="blue")
window.configure(bg="ivory2")
window.title('    Twitterscraper   ')
l = Label(text = "Enter cryptocurrency you want to search for. LEAVE BLANK if specification is not needed.", bg = "ivory2")

# Input parameters
search_hash = Label(window, text="Enter hashtag(s) you want to search for (e.g.: BTC,ETH,DOGE):", bg = "ivory2")
search_hash_entry = Entry(window, width=60, bg = "powder blue", fg="black", borderwidth=5)

search_words = Label(window, text="Enter word(s) you want to search for (e.g.: This,is,an,example):", bg = "ivory2")
search_words_entry = Entry(window, width=60, bg = "powder blue", fg="black", borderwidth=5)

comparison = Label(window, text="If you would like to compare different time periods of the same coin, or different coins, please click below.", bg="ivory2")
comparison_button = ttk.Button(window, text="MORE", command=compare)

query_limit = Label(window, text="Top limit for matching tweets per each day in interval (e.g.: 10):", bg = "ivory2")
query_limit_entry = Entry(window, width=60, bg = "powder blue", fg="black", borderwidth=5)

start_date = Label(window, text="Enter start date of tweets (YYYY-MM-DD):", bg = "ivory2")
start_date_entry = Entry(window, width=60, bg = "powder blue", fg="black", borderwidth=5)

end_date = Label(window, text="Enter end date of tweets (YYYY-MM-DD):", bg = "ivory2")
end_date_entry = Entry(window, width=60, bg = "powder blue", fg="black", borderwidth=5)

user_account = Label(window, text="Specific user account to search tweets from (e.g.: @elonmusk):", bg = "ivory2")
user_account_entry = Entry(window, width=60, bg = "powder blue", fg="black", borderwidth=5)
    
ok_button = ttk.Button(window, text="OK", command=clickbutton)
query_button = ttk.Button(window, text="Start Query", command=lambda:[scraper(), scraper_more(), process()])

# more stuff
label_2 = Label(window, text="Enter 2nd cryptocurrency or timeframe you want to analyze (LEAVE BLANK if not needed).", bg="ivory2")
search_hash_2 = Label(window, text="Enter hashtag(s) you want to search for (e.g.: BTC,ETH,DOGE):", bg = "ivory2")
search_hash_entry_2 = Entry(window, width=60, bg = "powder blue", fg="black", borderwidth=5)

search_words_2 = Label(window, text="Enter word(s) you want to search for (e.g.: This,is,an,example):", bg = "ivory2")
search_words_entry_2 = Entry(window, width=60, bg = "powder blue", fg="black", borderwidth=5)

start_date_2 = Label(window, text="Enter start date of tweets (YYYY-MM-DD):", bg = "ivory2")
start_date_entry_2 = Entry(window, width=60, bg = "powder blue", fg="black", borderwidth=5)

end_date_2 = Label(window, text="Enter end date of tweets (YYYY-MM-DD):", bg = "ivory2")
end_date_entry_2 = Entry(window, width=60, bg = "powder blue", fg="black", borderwidth=5)

display_text = Label(window, text=f"Double check the input data! \n Query hashtag: {search_hash_entry.get()}\n Query words: {search_words_entry.get()}\n Tweet limit per day: {query_limit_entry.get()}\n Start date: {start_date_entry.get()}\n End date: {end_date_entry.get()} \n From user: {user_account_entry.get()}\n This may take a while!", bg="ivory2")


### pack widgets on window ###
l.pack(pady=10)
search_hash.pack()
search_hash_entry.pack()
search_words.pack()
search_words_entry.pack()
comparison.pack(padx=10, pady=10)
comparison_button.pack(pady=(0,10))
query_limit.pack()
query_limit_entry.pack()
start_date.pack()
start_date_entry.pack()
end_date.pack()
end_date_entry.pack()
user_account.pack()
user_account_entry.pack()
#query_button.pack(pady=10)
ok_button.pack(pady=10)

# main loop for window
window.mainloop()