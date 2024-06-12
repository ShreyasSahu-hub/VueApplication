<template>

    <!--This is the link to the bootstrap library, to allow to import necessary classes for the navigation bar.-->
    <head>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>


    <!--This is the HTML elements to develop the navigation bar. The <a> tag is used to create four links to four different web page.-->
    <header>
    <nav class="navbar navbar-expand-lg navbar-light bg-light w-100">
    <div class="container-fluid">
      <a class="navbar-brand" href="/mainPage">Navbar</a>
      <button class="navbar-toggler custom-btn" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
            <li class="nav-item">
                <a class="nav-link" href="/CalorieTracker">Calorie Tracker</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="/FetchingExercisingVideos">Fetching exercise videos</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="/automatedTesting">Testing</a>
            </li>
        </ul>
      </div>
    </div>
    </nav>
    </header>

</template>


<!--This the CSS for making the shape of the navigation bar to be as wide as possible to cover the web page width.-->
<!--It ensures that the navbar position should always be at the top of the web page-->
<!--It also ensures that the buttons on the navigation bar should have a spacing between-->
<!--them using the padding syntax and the text size should be big enough so its more readable-->
<style scope>

header {
  position: fixed;
  width: 100%;
  top: 0;
  z-index: 1000;
}

.navbar {
  width: 100%;
}

.custom-btn {
  padding: 10px 20px; /* Adjust padding for button size */
  font-size: 1.25rem; /* Adjust font size */
}

</style>