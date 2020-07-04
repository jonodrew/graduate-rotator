# Graduate rotator
Transparent. Objective. Efficient.

Matching people to roles is a subset of matching things with other things. This is also 
known as _the assignment problem_ and it's really exceptionally difficult. I think most 
people doing it don't realise how difficult it is, so I've made a little toy prototype to
show them. You can play along too: https://grad-rotator.herokuapp.com/pitch/start

Matching people to things is hard, because the numbers go up very quickly. Matching one 
person to one thing is easy: there's one solution. Matching two people to two things is 
also easy: there are two solutions.

There are six solutions when matching three people to three things, and 24 when matching 
four people to four things.

There are _3,628,800_ possible solutions when matching ten people to ten things.

The number that describes the number of potential solutions when you try to match 100 
people to 100 things is so big that we haven't yet invented a word to describe it, but 
I firmly believe it's a problem that should be delegated to a computer. 

This is the beginnings of open-source software that should make it easier to solve this 
absurdly niche problem. It relies on the extremely marvellous [munkres library by 
Brian Clapper](https://github.com/bmc/munkres) to solve this complex problem in less than
a second.

All of the window dressing is mine. This project is licensed under the [MIT License](LICENSE).
