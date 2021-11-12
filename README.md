# Load balance testing for Eileen Southern site

This repo is for load balance testing on the Eileen Southern Omeka site using locust. With locust installed, you should just be able to run the `locust` terminal command for a web app using the locustfile to hit pages on the site.

The locustfile will visit the home page, item pages, and pages present in the "Exhibitions" menu, preferring the items or pages.

The idea is to make sure that Omeka won't break too hard on 500 people.
