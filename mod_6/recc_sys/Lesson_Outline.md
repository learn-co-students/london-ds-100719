# Teacher Lesson Plan for Recc Sys Lecture

! COSINE DISTANCE EXAMPLES
! SVG STUFF

This document provides a general outline for teachers to plan the Recc System lecture at Flatiron School.
The slides for the presentation can be found [HERE]() and were originally created by [THIS PERSON]().
Notes for this lesson plan were created by [David Baker]().

## Lesson Outline

### Lesson Goals 

At the end of the lesson, students should be able to...

* Explain Advantages/Disadvantages of Various Recc Systems
* Calculate Similarty metrics 
* Determine predicted ratings in context of collaborative filtering
* Explain Latent Recc Models and their creation 

### Why ReccSys?

When opening the lecture, you can first acknowledge that reccomendation systems are everywhere and everyone probably sees them daily in the 21st century.
Exemplars of this are product reccomendations from Walmart and Amazon (Slides), but there's also where to eat, music to listen to, what news to read, and anything else you might turn to a friend to ask them what they would suggest. 

After a brief intro, possibly pause for an open ended question to the class:

> When you reccomend a TV show to a friend, what do you consider before making a reccomendation?
> What makes a good reccomendation?
> What questions would you ask of someone before you made a reccomendation?

In bringing discussion back together points you might want to highlight 

* Making reccomendations for basic stuff is easy
* A good reccomendation takes a comprehensive understanding of what is out there
* It also requires you to know the entire space of "things" you could recc, but the asker doesn't know about.

Can use this to transiton into a slide talking about the idea of the "Long Tail" (slide).

Take time to discuss what is the "long tail".
Idea basically is that most people know most things.
Easy example is Top 40 radio station.
You can pretty much get away with playing popular stuff for people.
A good recc is saying, "Hey, I see you like band X (maybe for reasons A,B,C), you might ALSO like Y (which is way less popular than X) but shares similar (enough) attributes.

If wanting to dig deeper here, can also highlight that sometimes people just want things that are similar, but sometimes they are in mood for discovery?
That theoretically should be built into your models.

Given this is a tough question... lots of ways to go about answering this. 

### Types of Systems  

#### Non-Personalized 

First type of reccomendation is the easiest, most safe: Non-Personalized.
These say "I have no idea about an individual's background, but I assume you like things that are popular".

Main points on slide.
Examples of this are Trending on Youtube or Twitter.
Billboard Top 40 if you want to keep with the music metaphor. 

It's GOOD because it's simple and people get why something is reccomended.
It's BAD because it's not personalized at all.

It's not bespoke...

#### Content Based

Reccomendations that's just concerned about ITEMS and not about USERS.
You have USER profile and ITEM profile.
Here EVERY items typically has same set of attributes.

Can note here that companies like PANDORA (music radio recc) have people go in an hand annotate songs based on 150ish charateristics.
Idea as user INTERACTS with platform, platform will push you towards things you like and listen to (Explicit or Implicit)

> What are ways that you explicitly and implicitly interact with a Recc System? (i.e. Spotify) 


Answers?

* Listen time 
* Skipping Songs
* Liking Songs
* Disliking Songs
* Number of times you repeat listen 

Go through example witih MOVIES table.

Explain you have big fat grid with everything you're interested in.
Genre, actor, directory (stuff with the items) each ITEM or MOVIE in this case is rated on all these dimensions.

Next quetion is how to determine what is similar?

This is a **HUGE** question from a perceptual level.
Things that could go wrong...

* What items are more important?
* How sensative is each rating?
* Do people see similarity and dissimiarity as two sides of same coin?

Point out here that can use COSINE distance between vectors to make this determination.

It's GOOD because you get what is happening 
It's GOOD because if you get a new item, alreay know where it fits in similarity space
It's GOOD because can figure out what a user likes and gives them reccs for unique tastes.
It's BAD(ish) becuase you need a lot of tagging involved.
It's BAD because of overspecialzation (?) of items?

#### Collaborative Filtering

In this case you use both USER data and ITEM data. 

Here we make assumption that IF one person is like another, they probably will like similar things.
How is this done?

Need to represent the data of the users, we put this all in a matrix.
SLIDES on 16 show you can have this represented with UTILITY MATRIX.
Can have INTERGERS or WHATEVER SCALE (thumbs)

BECAUSE not everyone rates every item, our job is to try to GUESS what people haven't rated.
AFTER making predictions, we then just show people the highest numbers. 

A PROBLEM here is that we have sparse data.
That's the whole problem.
Here we RETURN to IMPLICIT vs EXPLICIT. 
EXPLICIT is people making 5 star or something ratings.
IMPLICIT is just maybe completing a listen on YouTube.

With any matrix, you can then figure out how close two users are to one another.
We do this with three step process.

1. Pick a similarity metric
2. Calculate similarity between the two vectors.
3. Find OTHER similar users, use their scores to guess what should be there (and use that number to make a recc)

Example of this is USER USER SLIDE.

Have GREY HAIR person with three books.
Calculate SIMILARITY of GREY with all others (see bottom right which is just first column.
Do that for EVERY user (not just one).

IN Slide 2, want to find out what GREY book THREE.
BLONDE BOY gave it a 4 and PINK SHIRT gave it a FIVE.
We then take in the GLOBAL similarity and multiply the rating times user similarity.
This allows us to mirror assumption that we get better reccs from people who are similar.
We then DIVIDE by summation of each weights.
This puts us back on the scale.

OR WE COULD DO ITEMS

Just REPEAT this process for ITEM ITEM Similarity.
Same thing, but now flipped on its head (transposed).
COLUMNS now but before we did ROWS.

Item wise typically does better.

TIME TO NOW MAKE RECC.

Example for lesson now is how much will Jon Snow like Harry Potter.

#### Memory Based Systems

Going to cut deeper now.
Now NOT just going to use big matrix of items and cosine differene.
As mentioned BEFORE, lots of different ways of recc systems.

If we have all this information, we want to explore different ways of making similarity calculations.

List four on slides.

##### Similarity Metrics 

Jaccard

* Implicit Data (clicking skip on Spotify)
* Intersection of items rated by users DIVIDED by UNION of both Users.
* Ignores the actual value.

List of songs we both listened to all the way through divided by everything we have in common???

Euclidean Distance

* Squared summation between all points, then sqrt

Manhattan

* Close to Euclidean but take ABS VALUE.

Cosine

* What used before.
* Make NA a 0
* Scale between -1 and 1
* Missing Ratings are now 0 (not nessecariliy true)

Adjusted Cosine

* Get rid of extent problem by just saying above of below 0
* Gets rid of the superlative people (OMG IT WAS THE BEST/WORST)

Pearson

* Literally just correlation
* No missing values!

Which one? 
Depends.
Correlation...

!! CREATE PYTHON CODE THAT SHOWS ALL THESE.

NOW going to run through the calculations with table.

1. AVERAGE over all users.
2. NOTE means on far right.
3. MEAN normalize, aka Center your variables over 0 (easy to show with Tyrion) 
4. (Could note that 3 is very close to idea of Repeated Measures Designs with Sum of Squares)
5. Find out who is JON mot similar to next via COSINE Similarity
6. Like Book example, now take weighted average of it all. 
7. Arrive at answer of 4.

!!! Not sure about ADVANCED SLIDE.

Collaborative Filtering is GOOD because it is much more personalized.
It requires a lot of MATH (lots of making computer cry) 
Also brings to idea of *COLD START* problem which is why asked to pick things you are interested in when starting website.
For Recc Systems to be good, need to interact with the platform!!
Still washes towards popularity.

#### Model Based Techniques

But what if you DON'T want to get all this data and have people rate everything?
We can do some sort of data analysis based on theory ahead of time. 

EXPLAIN Latent Features Graph.
LINK to PCA of LATENT Dimensions.
LINK to fact that PCA is form of dimensonality reduction.
THIS is just like PERSONALITY reserach, but using lots of different variables.

Very much like PCA...

Use Matrices to reduce our data.

SVD EXAMPLE:

1. ONE Matrix has list of individual ratings of movies
2. OTHER Matrix has extent that each film loads on a ????

????????????

Use Factors?

Very good for gettinig results, but computatioanlly expensive.

### Evaluating ReccSys

When you make something, how do you know it's good?
Can use RMSE if have a bunch of numeric, explicit ratings.
Would have to use something that accomondates Binary for Implicit (Skip or Not) ROC, AUC, Accuracy, Precision

Though in general EVALUATIING is hard to do, especially when you don't know what it's doing.
Answer is NOT in the numbers but rather product end. 

With NETFLIX prize, RMSE appears to be less?


### Issues with Recc Systems 

* Re-address Cold Start


