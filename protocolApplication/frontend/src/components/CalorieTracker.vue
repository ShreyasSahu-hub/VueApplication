<template>

   <NavBar/>


   <!--This is the form to provide recipes that is based on the user's diet preferences-->
   <div class="p-3 mb-2 bg-light text-dark rounded shadow-sm animated-background">


     <!--This is the form title-->
     <br><legend><b>Diet Plan</b></legend>


     <!--This is the form that has got form fields for the user to fill in the their diet preferences-->
     <!--As soon as the user fills in the form and clicks the form button, the function called handleEDAMAMAPI and its code gets executed-->
     <form v-on:submit.prevent="handleEDAMAMAPI();">
            <div class="mb-3">
                <br>



                <!--This is the text field used for the user to enter the food items that he/she prefers-->
                <!--It will be stored in a variable called query using the v-model syntax.-->

                <h2 class="my-4">Enter the food items</h2>
                <input class="form-control" type="text" placeholder="query" v-model="query" id="query" name="query" required/><br>
            </div>
            <div class="mb-3">
                <br>



                <!--This is the text field used for the user to enter their desired amount of calories that they want to intake-->
                <!--It will be stored in a variable called amountOfCalories using the v-model syntax-->

                <h2 class="my-4">Enter the maximum amount of calories that you want to intake</h2>
                <input class="form-control" type="text" placeholder="amount of calories in kcal" v-model="amountOfCalories" id="amountOfCalories" name="amountOfCalories" required/><br>
            </div>
            <div class="mb-3">
            <!--This is the option field that provides a list of all types of diet options that the user should select-->
               <h2 class="my-4">Diet Type</h2>
                 <select name="dietType" v-model="dietType" id="dietType" required>
                    <option value="balance">Balance</option>
                    <option value="high-fiber">High-Fiber</option>
                    <option value="high-protein">High-Protein</option>
                    <option value="low-carb">Low-Carb</option>
                    <option value="low-fat">Low-Fat</option>
                    <option value="low-sodium">Low-Sodium</option>
                 </select>
            </div>
            <div class="mb-3">
            <!-- This is the option field that provides a list of all meal type options that the user should select-->
            <h2 class="mb-4">Meal Type</h2>
                <select name="mealType" v-model="mealType" id="mealType" required>
                   <option value="breakfast">Breakfast</option>
                   <option value="brunch">Brunch</option>
                   <option value="lunch">Lunch</option>
                   <option value="dinner">Dinner</option>
                   <option value="snack">Snack</option>
                   <option value="teatime">TeaTime</option>
                   </select>
            </div>

            <!--This is where the user can click the submit button to submit their inputs.-->
            <br><button class="btn btn-sm btn-primary mt-3 custom-btn" type="submit">Submit</button>
     </form>
     <br>
     <!--This is the placeholder to display all the available recipes that are returned from the EDAMAM API-->
     <div id="content" class="row"></div><br>
   </div><br>

   <div class="p-3 mb-2 bg-light text-dark rounded shadow-sm animated-background">
   <div>
     <br>
     <h2 class="my-4">Calorie tracker</h2>


     <!--This is the form where the user can enter the food item and its quantities on a text field and  it will stored in the variable called listOfFoodItems-->
     <!--Once the user has filled in the text field, they can submit the form by clicking the submit button.-->
     <!--This is will call the function called calorieTracker and its code will be executed-->

     <form v-on:submit.prevent="calorieTracker();">
       <label>Enter the food items here</label>
          <div class="mb-3">
              <input class="form-control" type="text" placeholder="Enter the food item" v-model="listOfFoodItems" id="listOfFoodItems" name="listOfFoodItems" required/>
          </div><br>
          <button class="btn btn-sm btn-primary mt-3 custom-btn" type="submit">Fetch the amount of calories intaken</button>
     </form>
     <br>
     <div id="calorietracker"></div><br>          <!--This is the placeholder the calorie content of the food item that the user has typed.-->
   </div>
   </div>



   <!--A button is created that is labelled as See your Calorie History. When the user clicks the button, then it will redirect the user to the calorie history page.-->

   <div class="p-3 mb-2 bg-light text-dark rounded shadow-sm animated-background">

   <a href="/caloriehistory/"><button class="btn btn-sm btn-primary mt-3 custom-btn" type="submit">See your Calorie Histroy</button></a>

   </div>

   <br>

</template>

<script>
import NavBar from '../components/NavBar.vue';
export default{
       components:{
           NavBar,
       },
       data(){
           //These are all the variables created to store the user input from the form fields.
           return{
              query:"",
              amountOfCalories:"",
              dietType:"",
              mealType:"",
              listOfFoodItems:"",
           }
       },

       methods:{



       //This javascript function returns a list of recipes that are based on the what the kind of the diet that the user has entered in the form.

       async handleEDAMAMAPI() {
        let APP_ID = "f0809293";            //The the API ID is stored.
        let API_KEY = "4c9901ef9b16a44f50887e1926d8a00b";                //The API Key is stored.



        //The EDAMAM API is called to fetch the list of recipes based on the user's diet preference,
        //which is stored in the query variable that is concatenated to the query parameter, which is denoted by q.
        //The user's preferred diet type, amount of calories intake, and the meal type are also concatenated.

        const URL = "https://api.edamam.com/api/recipes/v2?type=public&q=" + this.query + "&app_id=f0809293&app_key=4c9901ef9b16a44f50887e1926d8a00b&diet=" + this.dietType + "&calories=" + this.amountOfCalories + "&mealType=" + this.mealType;

        const response = await fetch(URL);                     //The API's response are stored in the response variable.
        const data = await response.json();                    //The API's response are converted to the JSON format and it's stored to the data variable.
        console.log(data);

        document.querySelector("#content").innerHTML = "";                  //The div tag with the id called content initializes its HTML content to an empty string.

        try{



        //The if statement checks if the API's response is empty or not. If not, then a nested for loop is used to access each fields that each recipes has got.
        //The HTML tag elements are used to display the recipe details. The predefined Bootstrap classes are imported and used, which are called card, card-title, and card-text.
        //This is necessary to display the recipe's details in a white box that looks like cards. The recipe details are its image, the source of the recipe,
        //the diet type, the amount of calorie, and its link to the recipe website.

        if(data.hits.length>0){



        //The first for loop is used to iterate the recipes.

        for (let i = 0; i < data.hits.length; i++) {



          //The seconds for loop is used to iterate each recipe's detail, by accessing its fields and display it using the HTML tag elements.
          //The HTML tag elements are stored in the div tag with the id called content.
          //This will display the recipe's details in the placeholder that was explained earlier.

          for (let j = 0; j < data.hits[i].recipe.dishType.length; j++) {
            document.querySelector("#content").innerHTML += `
            <div class="card" style="width: 18rem;">
                <img src="${data.hits[i].recipe.image}" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">${data.hits[i].recipe.label}</h5>
                    <p class="card-text">Source: ${data.hits[i].recipe.source}</p>
                    <p class="card-text">Meal Type: ${data.hits[i].recipe.mealType}</p>
                    <p class="card-text">Diet Type: ${data.hits[i].recipe.dietLabels}</p>
                    <p class="card-text">Calories in Kcal: ${Math.round(data.hits[i].recipe.calories)} kcal</p>
                    <a href="${data.hits[i].recipe.url}" class="btn btn-primary">Click here to find more information about that recipe</a>
                </div>
            </div>
            `;
            break;
          }
        }
        }
        else{



            //If the API's response it empty, then a messages gets displayed in the placeholder to the user saying that the recipes are not available based on your preferences.
            //The HTML tags that are used to display the message are executed in the placeholder to display it to the user.

            document.querySelector("#content").innerHTML = `<h3 class="card-text">No recipes available based on your preferences</h3>`;
        }
        }
        catch(err){



           //If the user types invalid answers in the form, then an error message will be displayed in the placeholder to the user stating that they have filled in the form called diet form wrong.
           //The HTML tags that are used to display the error message are executed in the placeholder to display it to the user.

           document.querySelector("#content").innerHTML = `<h3 class="card-text">Invalid input. Please enter the right input</h3>`;
        }
       },



       //This function is where the EDAMAM API is called to fetch how much calories that the user consumes based what food item and its quantity that the user has typed in the text field
       //and display it on the web page.

       async calorieTracker(){

         //const data = ``;

         //try{



         //The EDAMAM API is fetched with the ingredients that the user has entered.

         const URLCalories = "https://api.edamam.com/api/nutrition-data?app_id=c5d32486&app_key=edd240211b6512dcb06d0ee3069929d3	&ingr=" + this.listOfFoodItems
         const response = await fetch(URLCalories);
         const data = await response.json();                 //Whatever calories that the API returned gets converted to the JSON format.
         console.log(data);



         //If the API response is not empty then the HTML tag elements is used to display the amount of calorie are stored in the div tag with the id called calorietracker.
         //This will execute the HTML tag elements in the placeholder that was explained earlier to display the amount of calories.
         //If the API response is empty, then a message is displayed to the user by executing the given HTML code on the placeholder. That HTML code is <h3 class="card-text">Calories unavailable</h3>.



         if(data.calories!=0){
         document.querySelector("#calorietracker").innerHTML = `<h3 class="card-text">Calories in Kcal: ${data.calories}</h3>`;
         console.log("calorie value:"+data.calories)
         }

         else{
         document.querySelector("#calorietracker").innerHTML = `<h3 class="card-text">Calories unavailable</h3>`;
         }

         //console.log("calorie value:"+data.calories)



         //If the API returned a calorie value for the ingredients that the user provided in the text field

         if(data.calories!=0){



         //The today's date is captured by the Date object and converted to the UK date format.

         var today = new Date();
         var dd = String(today.getDate()).padStart(2,'0');
         var mm = String(today.getMonth()+1).padStart(2,'0');
         var yyyy = today.getFullYear();

         var today = `${dd}/${mm}/${yyyy}`



         //The user's ingredients and the time the user has submitted the from to fetch the amount of calories are passed to the python function in the view.py file called
         //CalorieTrack, which will then store the passed details to the database.
         //The credentials field stores the include value that will store the details along with the storing the logged in user's username.

         var fd = new FormData();
         fd.append('listoffooditems', data.calories)
         fd.append('dateinserted', today)
         let response1 = await fetch("http://localhost:8000/CalorieTracker/",{
            method: 'POST',
            credentials: "include",
            body: fd
         })

         }

         //var data= await response.json()

       }

       }

}

</script>


<!--This is the CSS where its properties makes the background of the form to change its colour frequently-->
<!--It also adds blue colour to the form button and makes the button label white. It makes the button's colour to change to dark blue when the user hovers the button-->
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