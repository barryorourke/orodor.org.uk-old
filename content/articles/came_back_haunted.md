Title: Came Back Haunted
Date: 2013-12-16 22:43
Tags: Blogging, Programming

After recently switching from [Wordpress to Pelican]({filename}/articles/goodbye_wordpress_hello_pelican.md), I've changed my mind again and the site is now running [Ghost](http://www.ghost.org).

The funny thing is that if you compare the two, they are almost opposite, with the only thing in common being that posts are written in markdown.

Pelican is a static site generator which creates HTML files from text files written in markdown, it has no database or dynamically generated content. Ghost on the other hand is written in javascript using node.js, which at the moment isn't very common on standard web hosting. To self-host you'll likely need a VPS running apache or nginx as a reverse proxy server.

So why switch when I bigged up static site generators so much a couple of posts back? It was a simple decision really, I see promise in Ghost, I like it's minimalist approach and almost OCD level of quality control on development, everything has been thought out really well and that pleases the order loving part of my brain! On top of that there are certain elements that remind me of the early days of Drupal, back then my uid was somewhere under 20 on drop.org.

Not staying active in the Drupal community must be one of my open source regrets. I'd quite like to make up for it now by becoming active in the Ghost community!

As my first offering you'll find the source to the theme used on this site in my [Geist](http://www.github.org/barryorourke/geist) repository on github..
