### What I learned at BuildMadison and in making CitySolver

Back in September I had the chance to participate in an event called  [Build Madison](http://buildmadison.org/), a weekend event that brought tinkerers, hackers and idea people together to build things.

At the event, myself and Paul Klemstine and another took up the challenge of building on a pitch to come up with a way to submit quality of life issues -- graffiti, potholes, sidewalks in need of repair -- to the city of Madison from a mobile device. Pictures were a must, as was the ability to add a user's location.

![CitySolver](http://www.projects.chrislkeller.com/images/city_solver/city_solver_incident.png)

The Build Madison pitch also positioned this project as something that would tie in with the city's existing "Report a Problem" infrastructure."

Paul and I developed had a good time hacking together a project we called [City Solver](https://github.com/chrislkeller/CitySolver)… It could aspire to be more -- a foundation for an open-source [See, Click, Fix](http://seeclickfix.com/) or a tool for smaller municipalities -- or less and left to lessons learned, of which there were many that apply to many things I find myself involved in on a daily basis.

1. From different angles and perspectives keep asking, "Should this problem need to be solved?"

  The original pitch wanted to tie an application into the city of Madison "Report a Problem" system. Needless to say that is an exponentially difficult task, and one not easily tackled by a hackathon team with 24 hours to work with. 
	
	And nevermind that the city of Madison has a comprehensive website that city residents can use to report specific issues and wasn't looking to extend the system in the manner the pitch stated.
	
	But the project led to some great conversations with city officials and some insight into their future plans, some of which include mobile access and user feedback that we had in mind.

2. Know who else has "solved" or attempted to "solve" this problem.

	Had in been better in touch with Code For America, I would have known that developers have open-sourced similar applications, code that we could have built upon. 


3. Spend more time on knowing the following: 

	- Who are your users?
	- What are their needs?
	- What can we do for them?

	To this point, after presenting and thinking about this project as something "long-term" I was able to come up with the following:

	- City residents have the power, know-how and -- I believe -- a want to work together to solve some common problems.
	- That said, that power and ability is limited when a distinction is made between a resident's fence that is in disrepair, a street with potholes and a malfunctioning street light.
	- Success in building a coalition-based platform might best come if based around a singular idea, similar to Boston's Adopt a Hydrant.
	- Privacy is a real concern and offers a very real hurdle to overcome when considering the idea of neighbors reporting on issues with neighbors.

4. That last one is a biggie, hence even if everything at this point is coming up roses, would anyone use this thing?

	There are privacy aspects to keep in mind, and very real hurdles to overcome when considering the idea of neighbors reporting on issues with neighbors. For instance, "Thank you, I'd like to repair my broken fence, but I'm without work and my wife is sick and I haven't made the time, so thank you for posting a photo of it online with your brutish comment."

### Build Madison Presentation Bullet Points

![CitySolver](http://www.projects.chrislkeller.com/images/city_solver/city_solver_web.png)

City Solver is a multi-device platform that allows everyday citizens to submit information about quality of life issues and problems they feel a municipality could or should address.

Whether using a web app, a native Android app, or their laptop, desktop computer or tablet, city residents could send images and descriptions of these issues and opportunities.

A rating system is Phase One of furthering the platform to allow neighborhood residents to band together to solve issues or to clean up the neighborhood.

#### Features

- Native Android app pulls geolocation and user information to auto-populate data fields, and sends photo and photo location to a database.
- Thumbs up and thumbs down ranking of issues to gauge interest from others.
- Interface thats works on devices and browsers.
- Photo uploads work on Android and laptop, desktop web browsers. Photo uploads will be possible for users on iOS 6 Safari.

![CitySolver](http://www.projects.chrislkeller.com/images/city_solver/city_solver_mobile.png)

#### Wishlist

- Coalition building. Sign up to band together to fix this problem.
- Use geolocation of an issue to query against aldermanic districts to add more context, or partner with OpenBallotBox?
- Allow user to submit information via SMS
- Use email to submit information.
- Full screen map with geolocation to find issues near you.
- Filtering & Search.
- Admin view of database to assign issues, mark as resolved or not feasible and communicate back with user if needed.
