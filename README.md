> This repository was built upon a mock-project template.
> You can see in `TODO.md` that there were a series of tasks given to be completed.
>
> All the tasks are complete in this project workspace!
> I had a lot of fun completing these tasks on my own and tweaking the codebase, to help practice and showcase my skills.

# Midpoint Suggestions
This project is designed to match groups of users/travelers up with potential midpoint activities, as a way to plan events that are fair and desireable for involved users and their preferences.
It takes in lists of activities, users, group requests, and travel timetables.
It outputs data for each "suggestion" made per user-group request.

## How to Run
Download the code, and then run:
1. `npm install`
1. `npm start`

## How to Use
### Input Values
The input values can all be found in the csv files.
Navigate to `./src/data/` in order to view all the data!
There is a lot in this project; in fact, I've split up some of the more complex data into multiple components.
For example, users were given their own csv file so that multiple of their locations could be saved.

You'll find files for metro stations, activities, midpoint requests, and users within the data directory.

### Terminal Output
When you run the script, data is output in your terminal.

**<details><summary>Here is an example of the output...</summary>**

~~~txt
Finding suggested activities...

Results for request: MidpointRequest<000000>
Suggested activity: Activity<Lakeside Grill>
Distance from User<000000>: 21.633182195379405
Distance from User<000013>: 29.089866838883466

Results for request: MidpointRequest<000001>
Suggested activity: Activity<Lakeside Grill>
Distance from User<000000>: 21.633182195379405
Distance from User<000013>: 29.089866838883466

Results for request: MidpointRequest<000002>
Suggested activity: Activity<Presidio Main Post Lawn>
Distance from User<000000>: 30.186780844724847
Distance from User<000043>: 68.6343079233556

Results for request: MidpointRequest<000003>
Suggested activity: Activity<Presidio Main Post Lawn>
Distance from User<000000>: 30.186780844724847
Distance from User<000044>: 113.009018556202

Results for request: MidpointRequest<000004>
Suggested activity: Activity<The Saloon>
Distance from User<000001>: 19.68482378334341
Distance from User<000013>: 31.009916563081028

Results for request: MidpointRequest<000005>
Suggested activity: Activity<The Saloon>
Distance from User<000001>: 19.68482378334341
Distance from User<000013>: 31.009916563081028
~~~

</details>
