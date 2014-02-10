Title: Goodbye Wordpress, Hello Pelican
Date: 2013-11-08 20:52
Tags: Blogging, Programming

I've made a lot of changes to the site over the past couple of weeks after an almost painful journey into the internals of Wordpress, the biggest change being that I've dumped Wordpress in favour of [Pelican](http://www.getpelican.com), which is a static site generator written in [Python](http://www.python.org). 

Pelican will take content written in a variety of simple markup formats, combine it with a theme and produce a site in static HTML. It sounds a bit backwards for 2013 but it seems to becoming quite popular and when you think about it there are a lot of advantages;

* No database to slow the page load time down.
* No scripting language for supposed hackers to exploit.
* Can be hosted anywhere, I've move to using [Github Pages](http://pages.github.com).
* All content is written in [Markdown](http://daringfireball.net/projects/markdown), and stored in version control.

In addition to that I've created a Pelican theme for the site using Twitter's [Bootstrap](http://www.getbootstrap.com) framework, it's basically a rewrite of the theme that I was using on Wordpress (and Drupal before that), but with some shiny extras! It's freely available for you to do whatever you like with on [Github](http://www.github.com/barryorourke/pelican-orodor).

Finally, I've removed everything google from the site after hearing [Mikko Hypponen](https://twitter.com/mikko) speak at LinuxCon, you can see him present a similar talk at [Ted Brussels](http://www.ted.com/talks/mikko_hypponen_how_the_nsa_betrayed_the_world_s_trust_time_to_act.html), It's only 20 minutes long and definitely worth the watch. This will cause issues for anyone who used to read the site using my feedburner feed, they'll need to resubscribe using the new one.

The only issues I have at the moment are that due to it being static HTML there is no comment system or built in search, I'm looking into a few options at the moment and should have something up and running shortly, twitter can be used in the meantime if anyone wants to talk!
