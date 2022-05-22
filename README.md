# 🎫Guts Ticket Notifier 
## 🎫Ticket notifier app that notifies the user when a ticket is available on guts.events
* 🛠️Build using selenium
* Every 5 seconds it checks if a ticket is available for a specific day e.g "Friday"
  - If after 30 seconds the ticket is still available it will send another message

* 🔔User gets notified by email using 📧Gmail
  - There seems to be a small delay of about 2-4 minutes, which is not ideal in this usecase
* 🔔And user gets notified by Discord webhook message in a specified channel 

## ✨To-do:
* ~~Only notify user when a specific type of ticket is available~~
* ~~notify user by using a discord bot in a discord server~~
