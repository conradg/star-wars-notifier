# star-wars-notifier

This was created to notify me when Star Wars: The Force Awakens tickets went on sale, but could be adapted 
to notify you about any change in the content of a website.

It uses Yo, a simple notification program that's free to use, and offers an API. Of course, there's no reason it 
couldn't be set up to use E-mail, SMS, IM or any other method

To use it, you should:
  1. Create a Yo account that will act as the notifier, and subscribe to it with a personal Yo account
  2. Create a file in this directory called `yo_api_token.txt` containing your Yo API token.
  
        echo *your_token* > yo_api_token.txt
  
  3. (optional) Set up the notifier Yo account with IFTTT to trigger any action of your choosing
  4. Run the program on the platform of your choice.
  
        python star_wars.py
        
That's all! When the website you're polling changes to include the content you're looking for, a "Yo!" from
the notifier account will be sent to all it's subscribers containing the link to the website, and to IFTTT
if that's been set up
