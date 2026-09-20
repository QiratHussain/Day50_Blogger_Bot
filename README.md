#  Automated Quote Blogger

A Python + Selenium automation project that finds a random quote, sends it to ChatGPT to generate content around the quote, and publishes the result automatically to Blogger.

This project started as my **Day 50 alternative project** during the 100 Days of Code challenge, but I eventually turned it into an idea of my own.

##  What It Does

The automation handles the entire workflow:

1.  Opens a quote website
2.  Finds a random quote
3.  Sends the quote to ChatGPT
4.  Generates content based on the quote
5.  Opens Blogger
6.  Publishes the generated content automatically

The goal was to experiment with combining **web scraping, browser automation, AI, and content publishing** into one workflow.

##  Technologies Used

* **Python**
* **Selenium**
* **Web scraping**
* **Browser automation**
* **ChatGPT**
* **Blogger**
* **Chrome / ChromeDriver**

##  Project Structure

```text
Automated-Quote-Blogger/
│
├── main.py
├── quote.py
├── blogger.py
├── ...
└── README.md
```

> The exact structure may change as the project evolves.

##  How It Works

The project is divided into separate stages:

```text
Quote Website
      ↓
Find Random Quote
      ↓
Extract Quote + Author
      ↓
Send to ChatGPT
      ↓
Generate Content
      ↓
Open Blogger
      ↓
Create Post
      ↓
Publish
```

Each stage is handled through browser automation using Selenium.

##  Why I Built It

This wasn't simply another course exercise.

I wanted to see whether I could take the automation concepts I had learned and use them to build something based on **my own idea**.

The project combines several things I've learned throughout my Python journey:

* Object-oriented programming
* Selenium
* Web scraping
* Browser interaction
* Automation workflows
* Exception handling
* Working with multiple websites
* Integrating AI into an automation workflow

##  Current Limitations

This project currently relies heavily on Selenium and browser interaction.

That means it isn't designed as a production-ready cloud application yet.

Some parts may also break if the websites involved change their HTML structure or user interface.

The project is currently intended primarily as a **learning and portfolio project**.

##  Future Improvements

There are several things I'd like to explore in future versions:

* [ ] Add AI-generated images for each quote
* [ ] Improve the generated article structure
* [ ] Add better error handling and recovery
* [ ] Reduce dependence on manual browser interaction
* [ ] Add configurable posting schedules
* [ ] Store previously used quotes to avoid duplicates
* [ ] Make the workflow easier to configure
* [ ] Explore deploying the automation as an actual service

##  What I Learned

The biggest lesson from this project wasn't just learning another Selenium technique.

It was learning that **a small personal idea can be turned into an actual software project by connecting tools together.**

This project also pushed me beyond simply following a tutorial and gave me experience designing an automation workflow from my own idea.

##  Day 50

This project represents my **Day 50** of the 100 Days of Code challenge.

50 days in, I'm becoming less interested in simply completing exercises and more interested in asking:

> **"What can I actually build with what I know?"**

And this project was one of my first attempts to answer that question.

