<template>

   <NavBar/> <!--The HTML elements from the NavBar.vue file are executed in this template tag-->

   <!--This form consists of one text field that allows the user to type any exercising videos.-->
   <!--Once the user submits the form, the function called handleVideos is called and its code gets executed-->
   <div class="p-3 mb-2 bg-light text-dark rounded shadow-sm animated-background">
   <br>
   <h2 class="my-4">Find exercise videos</h2>
   <div>
     <div class="form-group">
     <form v-on:submit.prevent="handleVideos();">
      <legend>Enter the exercise videos that you want:</legend>
         <div class="mb-3">
             <input class="form-control" type="text" placeholder="query" v-model="queryForVideos" id="queryForVideos" name="queryForVideos"/>
         </div><br>
         <button class="btn btn-sm btn-primary mt-3 custom-btn" type="submit">Fetch videos</button>
     </form>
     </div>
   </div>
   <br>
   <br>
   <!--This is a placeholder, where the 5 youtube videos are displayed in rows based on what the user has typed in the text form field in rows.-->
   <div class="card-body d-flex flex-column justify-content-between gap-4">
        <div id="returnedVideos" class="row">
        </div>
   </div>
   </div><br>

</template>

<script scope>
import NavBar from '../components/NavBar.vue';         //importing the HTML and CSS code from the NavBar.vue file
//The export keyword is used to import the code from the NavBar.vue file
export default{
    components:{
           NavBar,
    },
    data(){
       //The queryForVideos variable is created to store the user input from the text form field.
       return{
              queryForVideos:"",
       }
    },

    methods:{


       //This javascript function is where the Youtube API is called based on the what the user has typed to return the top 5 vidoes.
       async handleVideos(){



        //This code locates the div tag with the id called returnedVideos and initialized its HTML content to an empty string.
        document.getElementById("returnedVideos").innerHTML = ``;


        //This prints out the user input from the text field on the console
        console.log(this.queryForVideos)


        //The Youtube API is called. Its URL gets concatenated with the user input to the query parameter which is denoted by the symbol q. Its output is returned and it gets stored in the response variable.
        let response = await fetch('https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=5&q=' + this.queryForVideos + '&type=video&key=AIzaSyA20OFgpO9qgwShY_S5PBzh3_Uw2-o3v4k')
        .then(result => result.json())      //The API's output is converted to the JSON format using the json function, because it's easier to display the video's details, due its simple readable structure.
        .then(data=>{
           console.log(data)
           data.items.forEach(a => {
               document.getElementById("returnedVideos").innerHTML += `
               <p class="card-text">
               <a href="https://www.youtube.com/watch?v=${a.id.videoId}" class="yt-=video">
                   <img src="${a.snippet.thumbnails.high.url}"/>
                   <h3>${a.snippet.title}</h3>
               </a>
               </p><br><br>
               `
           })
        })

        //The videos in the API response are iterated through the forEach build-in function. The HTML elements are used to display the video's details by using the paragraph tag, and the anchor tag.
        //THe predefined Bootstrap class called card-text is imported to display the video details on a white box that looks like cards.
        //The url field and the title of the each Youtube videos are accessed, in order to display the image of the video, the title of the video and the link to the video.
        //ALl the HTML elements that are used to display the video's details are stored in the div tag with the id called returnedVideos,
        //in order to execute that HTML elements in the placeholder that was mentioned earlier.

        //let data = await response.json()
        //console.log(data)

       },

    },

}

</script>

//This css style where it executes the colour change in the background form and makes the colour of the form buttons blue.
//When you hover the form buttons, the button colour changes from the normal blue to dark blue.

<style scoped>

@keyframes gradientAnimation {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}

.animated-background {
    background: linear-gradient(270deg, #ff7e5f, #feb47b);
    background-size: 400% 400%;
    animation: gradientAnimation 15s ease infinite;
}

.shadow-sm {
  box-shadow: 0 0.125rem 0.25rem rgba(0.5, 0.5, 0.5, 0.5);
}

.custom-btn {
  background-color: #007bff; /* Primary color */
  border-color: #007bff;
  font-weight: bold;
  padding: 10px 20px;
  font-size: 16px;
  border-radius: 5px;
  transition: background-color 0.3s, box-shadow 0.3s;
}

.custom-btn:hover {
  background-color: #0056b3; /* Darker shade for hover effect */
  border-color: #004085;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.custom-btn:focus {
  outline: none;
  box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.5);
}

.custom-btn:active {
  background-color: #004085;
  border-color: #003366;
}

</style>