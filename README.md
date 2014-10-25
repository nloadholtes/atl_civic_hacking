atl_civic_hacking
=================

The Center for Civic Innovation hosted a "Food security" hackathon. Participants were told about some challenges in getting food to people, and then invited to explore several options.

This repo is for the code I made there to try and do some analysis on some EBT/SNAP/WIC data realting to Farmer's Markets.

Farmer's Markets are an interesting option in food: They are typically stocked with locally grown foods, are typically community centric/oriented, and some vendors accept EBT/SNAP/WIC.

One of the challenges with programs like SNAP is not only getting people connected with food, but also ensuring that they have access to healthy choices, not just what's convenient (such as fast foods).

A Farmer's Market presents an interesting solution: Healthy foods, local community support, and a place where EBT/SNAP/WIC is accepted.


~~~~
Notes: The data is not here in this repo. Some of the data contained Personally Identifiable Information (PII), and it was requested that it not be posted publicly. 

~~~~
Observations:

Looking at the Data for 2013, we see that there are two columns, "TOTAL $ EBT/WIC" and "AMOUNT SWIPED" for each day and location. It is possible to pay with paper tickets instead of the card. Looking at each location we can see on average how much was charged:

```
Decatur Farmers Market avgerage of 51.64% charged
Cotton Mill Farmers Market avgerage of 53.44% charged
Peachtree Rd Farmers Market avgerage of 51.54% charged
Macon (Mulberry St.) avgerage of 52.73% charged
SWOOM avgerage of 55.49% charged
Battlefield Farmers Market avgerage of 51.96% charged
East Lake Farmers Market avgerage of 58.76% charged
Rockmart Farmers Market avgerage of 52.67% charged
Statesboro Mainstreet Farmers Market avgerage of 55.65% charged
International City Farmers Market avgerage of 52.48% charged
Veggie Truck Farmers Market avgerage of 52.25% charged
East Atlanta Village Farmers Market avgerage of 55.44% charged
CHW Veggie Van avgerage of 50.00% charged
Clarkston Farmers Market avgerage of 50.60% charged
Truly Living Well avgerage of 48.58% charged
Farm Mobile avgerage of 50.00% charged
Grant Park Farmers Market avgerage of 49.09% charged
Athens Farmers Market avgerage of 50.98% charged
White Oak Pastures Farmstand avgerage of 50.00% charged
East Point Farmers Market avgerage of 57.77% charged
Forsyth Farmers' Market avgerage of 53.58% charged
```

It would appear that swiping a card is not the preferred means of purchasing at the farmers market. At this point it is unclear if this is due to vendors not accepting cards, or purchasers not having/preferring the cards.